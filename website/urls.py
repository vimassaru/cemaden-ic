from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form_view, name='form'),
    path('user/', views.user_profile, name='user_profile'),
    path('school-form/', views.school_form_view, name='school_form'),
    path('form-success/', views.form_success, name='form_success'),
]
