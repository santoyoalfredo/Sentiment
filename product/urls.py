from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views # used to call functions in view to correlate with specific urls

# all url patterns a user could type
# (first parameter) - regular expressions that defines what users type
#                      ^ defines the begining, $ defines the end
# (second parameter) - calls the view for that url
# (third parameter) - names that view to be used for dynamic html coding

app_name = 'product'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<product_id>[0-9]+)/create_review/$', views.create_review, name='create_review')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)