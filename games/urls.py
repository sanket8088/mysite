from django.urls import path

from . import views

urlpatterns = [
    path('online-games/', views.online_game, name='oneline_games'),
    path('sum/<int:num1>/<int:num2>/', views.get_addition_number, name='addition'),
    path('addition/', views.addition_numbers, name='addition'),
    path('substract/', views.substract_number, name='substract'),
    path('login/', views.login, name='login'),
    path('login/class/', views.LoginView.as_view(), name='login'),
    path('str_count', views.StrCount.as_view(), name='login'),
    path('school', views.AddSchool.as_view(), name='login'),
]
