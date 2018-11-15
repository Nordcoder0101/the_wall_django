from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^register_account$', views.register_account),
  url(r'^success$', views.show_success),
  url(r'^login$', views.validate_and_login),
]