from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path('edit_profile/', edit_profileView.as_view(), name='edit_profile'),
path('password/', auth_views.PasswordChangeView.as_view(template_name='registration\password_change_form.html')),
]