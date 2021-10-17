from django.shortcuts import render, redirect, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Profile, City, Post
from .forms import SignupForm, ProfileForm



# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signupform"] = SignupForm()
        context["loginform"] = AuthenticationForm()
        return context

class Login(View):
    
    def get(self, request):
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "registration/login.html", context)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', pk=user.id)
        else:
            form = AuthenticationForm()
            context = {"form": form}
            return render(request, "registration/login.html", context)

class Signup(View):
    
    def get(self, request):
        form = SignupForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=self.request.user.pk)
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

class ProfilePage(TemplateView):
    model = Profile
    template_name = "profile.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.get(pk=pk)
        context["post"] = Post.objects.all()
        return context

class ProfileUpdate(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "profile_update.html"
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_details.html"

class CityList(TemplateView):
    template_name = "cities_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["cities"] = City.objects.filter(name__icontains=name)
        else:
            context["cities"] = City.objects.all()
        return context
    
# class City(TemplateView):
#     model = Post
#     template_name = "cities.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post"] = Post.objects.all()
#         return context

class Post_Create(CreateView):
    model = Post
    fields = ['title', 'description']
    template_name = "post_create.html"
    success_url ="/cities/"

class Post_Update(UpdateView):
    model = Post
    fields = ['title', 'description']
    template_name = "post_update.html"
    success_url ="/cities/"

class Post_Detail(DetailView):
    model = Post
    template_name = "post_details.html"
    success_url = "/cities/"
    
class Post_Delete(DeleteView):
    model = Post
    fields = ['title', 'description']
    template_name = "post_delete_confirmation.html"
    success_url ="/cities/"
