from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView

# at top of file with other imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect("city_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)