import uuid

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect

from .forms import Signup, Login
from .models import User


class User_signup(FormView):
    form_class = Signup
    template_name = 'authentication/signup.html'

    def dispatch(self, request):
        if request.user.is_authenticated:
            messages.info(request, 'You are alreay logeed in')

            return HttpResponseRedirect(reverse('blog:home'))

        return super().dispatch(request)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()

        messages.success(
            self.request, 'Account created successfully. Please Login!')

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('registration:log_in')


class User_login(FormView):
    form_class = Login
    template_name = 'authentication/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are alreay logeed in')

            return HttpResponseRedirect(reverse('blog:home'))

        return super(User_login, self).dispatch(request)

    def form_valid(self, form):
        email, password = form.cleaned_data.values()
        user = authenticate(email=email, password=password)

        if user is not None:
            login(self.request, user)
            if 'next' in self.request.POST:
                return redirect(self.request.POST.get('next'))

            return HttpResponseRedirect(reverse('blog:home'))

        return super(User_login, self).form_valid(form)


@login_required
def User_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))
