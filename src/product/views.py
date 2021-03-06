from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DeleteReviewForm, DeleteProductForm, FlagReviewForm, ProductForm, ReviewForm, UserForm
from .models import Product, Review
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment

# View for the Admin Control Panel
def admin(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        return render(request, 'admin.html')

# View for the Admin Product Panel
def adminProduct(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = DeleteProductForm
        products = Product.objects.all()
        context = {
                'products': products,
                'form': form
            }

        return render(request, 'admin_product.html', context)

# View for the Admin Review Panel
def adminReview(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = DeleteReviewForm
        # Filter to reviews which are flagged
        reviews = Review.objects.filter(flag=True)
        context = {
                'reviews': reviews,
                'form': form
            }

        return render(request, 'admin_review.html', context)

# View for adding a product
def add_product(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            products = Product.objects.all()
            context = {
                'products': products,
            }
            messages.success(request, 'Product added successfully')
          
            return redirect(reverse('admin_product'), context=context)

        else:
            context = {
                'form': form
            }

            return render(request, 'add_product.html', context)

# View for creating a review
def create_review(request, product_id):
    form = ReviewForm(request.POST or None, request.FILES or None)
    product = get_object_or_404(Product, pk=product_id)

    # Check if the current user has already submitted a review for the product
    for review in Review.objects.filter(product=product_id):
        if review.user == request.user:
            context={
                'userCommented': True,
                'product': product,
            }
            messages.info(request, 'You have already submitted a comment for this product')

            return redirect(reverse('detail', kwargs={'product_id': product_id}), context=context)

    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.review_text = form.cleaned_data['review_text']
        review.user = request.user

        # Pass the review text through the sentiment analysis
        s = vaderSentiment(review.review_text)
        if s['compound'] < 0:
            review.score = 5 - ((s['compound'] * -1) * 5)
        elif s['compound'] > 0:
            review.score = 5 + (s['compound'] * 5)
        else:
            review.score = 0

        review.save()

        # Compute the new average score of the product after adding the review
        product.average_score = product.review_set.aggregate(Avg('score')).get('score__avg', 0.00)
        if product.average_score != None:
            product.average_score = round(product.average_score, 1)
            product.save()

        context={
            'product': product
        }
        messages.success(request, 'Comment submitted')

        return redirect(reverse('detail', kwargs={'product_id': product_id}), context=context)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'create_review.html', context)

# View for deleting a product
def delete_product(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        product_id = (str(request.POST.get('product_id')))
        product = get_object_or_404(Product, pk=product_id)

        if request.method == 'POST':
            form = DeleteProductForm(request.POST)

            if form.is_valid():
                product.delete()

        else:
            form = DeleteProductForm()

        products = Product.objects.all()
        context = {
                'products': products,
                'form': form,
            }
        messages.success(request, 'Product removed successfully')
          
        return redirect(reverse('admin_product'), context=context)

# View for deleting a review
def delete_review(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        review_id = (str(request.POST.get('review_id')))
        review = get_object_or_404(Review, pk=review_id)

        if request.method == 'POST':
            form = DeleteReviewForm(request.POST)

            if form.is_valid():
                review.delete()

                product_id = (str(request.POST.get('product_id')))
                product = get_object_or_404(Product, pk=product_id)

                # Compute the new average score after deleting the review
                product.average_score = product.review_set.aggregate(Avg('score')).get('score__avg', 0.00)
                print(str(product.average_score))
                if product.average_score != None:
                    product.average_score = round(product.average_score, 1)
                else:
                    product.average_score = -1
                product.save()                

        else:
            form = DeleteReviewForm()

        reviews = Review.objects.filter(flag=True)
        context = {
                'reviews': reviews,
                'form': form,
            }
        messages.success(request, 'Comment removed successfully')
          
        return redirect(reverse('admin_review'), context=context)

# View for viewing a product's details
def detail(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        context = {
            'user': request.user,
            'product': get_object_or_404(Product, pk=product_id),
        }

        return render(request, 'detail.html', context)

# View for editing a product
def edit_product(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        product_id = (str(request.GET.get('product_id')))
        product = get_object_or_404(Product, pk=product_id)
        form = ProductForm(request.POST or None, request.FILES or None, instance=product)

        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            products = Product.objects.all()
            context = {
                'products': products,
            }
            messages.success(request, 'Product edited successfully')
          
            return redirect(reverse('admin_product'), context=context)

        else:
            context = {
                'form': form
            }

            return render(request, 'edit_product.html', context)

# View for flagging a review
def flag_review(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        review_id = (str(request.POST.get('review_id')))
        review = get_object_or_404(Review, pk=review_id)

        if request.method == 'POST':
            form = FlagReviewForm(request.POST)

            if form.is_valid():
                review.flag = True
                review.save()
                messages.success(request, 'Comment has been marked for review')

        else:
            form = FlagReviewForm()
                
        context = {
            'product': product,
            'user': user
        }

        return redirect(reverse('detail', kwargs={'product_id': product_id}), context=context)

# View for the index
def index(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')

    else:
        products = Product.objects.all()
        return render(request, 'index.html', {'products': products})

# View for logging in a user
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                products = Product.objects.all()
                context = {
                    'products': products
                }
                messages.info(request, 'Welcome, {name}!'.format(name=username))

                return redirect(reverse('index'), context=context)
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, 'login.html')

# View for logging out a user
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }

    return render(request, 'login.html', context)

# View for registering a user
def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                products = Product.objects.all()
                return render(request, 'index.html', {'products': products})

    context = {
        "form": form,
    }

    return render(request, 'register.html', context)

# View for unflagging a review
def unflag_review(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        review_id = (str(request.POST.get('review_id')))
        review = get_object_or_404(Review, pk=review_id)

        if request.method == 'POST':
            form = FlagReviewForm(request.POST)

            if form.is_valid():
                review.flag = False
                review.save()
        else:
            form = FlagReviewForm()
                
        reviews = Review.objects.filter(flag=True)
        context = {
            'reviews': reviews,
        }
        messages.success(request, 'Comment was successfully unflagged')

        return redirect(reverse('admin_review'), context=context)