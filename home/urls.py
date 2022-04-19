from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.homepage, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]