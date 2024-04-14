# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),  #パスがsignup/の時にSignUpクラスベースのビューを呼び出す nameは{% url signup %}で利用
]