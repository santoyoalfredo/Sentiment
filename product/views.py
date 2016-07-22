from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404
from .forms import UserForm, ReviewForm
from .models import Product, Review
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment


def detail(request, product_id):
    if not request.user.is_authenticated():
        return render(request, 'product/login.html')
    else:
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'product/detail.html', {'product': product, 'user': user})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'product/login.html')
    else:
        products = Product.objects.all()
        return render(request, 'product/index.html', {'products': products})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'product/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                products = Product.objects.all()
                return render(request, 'product/index.html', {'products': products})
            else:
                return render(request, 'product/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'product/login.html', {'error_message': 'Invalid login'})
    return render(request, 'product/login.html')


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
                return render(request, 'product/index.html', {'products': products})
    context = {
        "form": form,
    }
    return render(request, 'product/register.html', context)


def create_review(request, product_id):
    form = ReviewForm(request.POST or None, request.FILES or None)
    product = get_object_or_404(Product, pk=product_id)
    if form.is_valid():
        review = form.save(commit=False)
        review.product = product
        review.review_text = form.cleaned_data['review_text']
        review.user = request.user
        s = vaderSentiment(review.review_text)
        if s < 0:
            review.score = 5 - ((s * -1) * 5)
        elif s > 0:
            review.score = 5 + (s * 5)
        else:
            review.score = 0


        review.save()
        return render(request, 'product/detail.html', {'product': product})

    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'product/create_review.html', context)

