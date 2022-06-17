from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
    # user/     # CBV 는 .as_view() 추가해줘야함
    path('', views.UserView.as_view()),
    path('signup/', views.SignUp.as_view()),
]
