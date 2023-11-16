from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", AuthLoginView.as_view(), name="login"),
    path("logout/", AuthLogoutView.as_view(), name="logout"),
    path(
        "confirm_logout",
        AuthConfirmLogoutView.as_view(),
        {"next_page": None},
        name="confirm_logout",
    ),
    path(
        "register/",
        AuthRegisterUserView.as_view(),
        {"next_page": None},
        name="register",
    ),
    path("u/<str:username>/", UserProfileView.as_view(), name="profile"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'auth/password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'auth/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'auth/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'auth/password_reset_complete.html'), name='password_reset_complete'),
]
