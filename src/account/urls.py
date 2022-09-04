
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('register', views.account_register, name='register'),
    path('active/<uidb64>/<token>/', views.account_activate, name='activate'),
    path('login/', views.account_login, name='login'),
    path('logout/', views.account_logout, name='logout'),

    # reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='account/account_reset/password_form.html',
        email_template_name='account/account_reset/password_email.html',
        success_url='/account/password_reset_done'), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/account_reset/password_done.html'),
        name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/account_reset/password_reset_confirm.html',
        success_url='/account/password_reset_complete'), name='password_reset_confirm'
    ),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/account_reset/password_complete.html'), name='password_reset_complete')

]
