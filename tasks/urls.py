from django.urls import path
from . import views
urlpatterns = [
    path('index/<str:uname>',views.index, name ='tasks'),
    path('signin/<str:uname>', views.signin2)

]
