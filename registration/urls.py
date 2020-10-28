from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetConfirmView

from .views import User_signup, User_login, User_logout
from .forms import ResetPasswordForm

app_name = 'registration'

urlpatterns = [
    path('signup/', User_signup.as_view(), name='sign_up'),
    path('login/', User_login.as_view(), name='log_in'),
    path('logout/', User_logout, name='log_out'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authentication/resetPasswordFlow.html', success_url=reverse_lazy('registration:password_reset_done')),
         name='password_reset'),

    path('password-reset/sent/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/resetPasswordFlow.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authentication/resetPasswordForm.html',
        success_url=reverse_lazy('registration:password_reset_complete'),
        form_class=ResetPasswordForm
    ), name='password_reset_confirm'),

    path('password-reset/success/', auth_views.PasswordResetCompleteView.as_view(
         template_name='authentication/resetPasswordFlow.html'
         ), name='password_reset_complete')
]
