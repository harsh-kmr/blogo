from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class edit_profileView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('user_profile')
    template_name = 'profile_edit.html'

    def get_object(self):
        return self.request.user