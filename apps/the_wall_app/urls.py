from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/post_message$', views.create_message),
    url(r'^/post_comment$', views.create_comment),
    url(r'^/logout$', views.logout)
]
