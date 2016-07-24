"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from product import views # used to call functions in view to correlate with specific urls

# all url patterns a user could type
# (first parameter) - regular expressions that defines what users type
#                      ^ defines the begining, $ defines the end
# (second parameter) - calls the view for that url
# (third parameter) - names that view to be used for dynamic html coding

app_name = 'product'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^admincontrol/', views.admin, name='admin'),
    url(r'^add_product/', views.add_product, name='add_product'),
    url(r'^edit_product/', views.edit_product, name='edit_product'),
    url(r'^deleteproduct/$', views.delete_product, name='delete_product'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<product_id>[0-9]+)/create_review/$', views.create_review, name='create_review'),
    url(r'^(?P<product_id>[0-9]+)/flag_review/$', views.flag_review, name='flag_review')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)