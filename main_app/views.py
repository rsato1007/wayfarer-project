from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signupform"] = UserCreationForm()
        context["loginform"] = AuthenticationForm
        return context

class Signup(View):
    
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class Profile(TemplateView):
    template_name = "profile.html"