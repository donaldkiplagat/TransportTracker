from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^$',views.singIn),
    url(r'^postsign/',views.postsign),
    url(r'^index/',views.index,name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
