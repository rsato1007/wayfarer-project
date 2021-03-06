from django.shortcuts import render, redirect, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Profile, City, Post, Comment
from .forms import SignupForm, LoginForm, ProfileForm, ProfilePictureForm, CreatePostForm




from django.core.mail import EmailMessage
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["signupform"] = CustomUserCreationForm()
        context["loginform"] = LoginForm()
        return context

class Login(View):
    
    def get(self, request):
        form = LoginForm()
        signupform = CustomUserCreationForm()
        context = {"loginform": form, "signupform": signupform}
        return render(request, "registration/login.html", context)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', pk=user.id)
        else:
            form = LoginForm()
            signupform = CustomUserCreationForm()
            error = "Invalid Credentials" 
            context = {"loginform": form, "signupform": signupform, "error": error}
            return render(request, "registration/login.html", context)
        
            
        

class Signup(View):
    
    def get(self, request):
        loginform = LoginForm()
        form = CustomUserCreationForm()
        context = {"signupform": form, "loginform": loginform}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=self.request.user.pk)
        else:
            loginform = LoginForm()
            context = {"signupform": form, "loginform": loginform}
            return render(request, "registration/signup.html", context)

        

class ProfilePage(TemplateView):
    model = Profile
    template_name = "profile.html"
    ordering = ['created_at']

    def get_context_data(self, pk, **kwargs):
        profile = Profile.objects.get(pk=pk)
        context = super().get_context_data(**kwargs)
        context["profile"] = profile
        context["posts"] = profile.post.all().order_by('-created_at')
        return context

class ProfileUpdate(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "profile_update.html"
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class ProfilePictureUpdate(UpdateView):
    model = Profile
    form_class = ProfilePictureForm
    template_name = "profile_picture_update.html"
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class PostDetail(DetailView):
    model = Post
    template_name = "post_details.html"

class CityList(TemplateView):
    template_name = "city_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["cities"] = City.objects.filter(name__icontains=name)
        else:
            context["cities"] = City.objects.all()
        return context

class CityDetail(TemplateView):
    template_name = "city_details.html"

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["cities"] = City.objects.filter(name__icontains=name)
            context["city_details"] = City.objects.get(pk=pk)
        else:
            context["cities"] = City.objects.all()
            context["city_details"] = City.objects.get(pk=pk)
        return context

# class City(TemplateView):
#     model = Post
#     template_name = "cities.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["post"] = Post.objects.all()
#         return context

class ProfilePostCreate(CreateView):
    model = Post
    fields = ['city', 'title', 'description', 'image']
    template_name = "profile_post_create.html"

    def form_valid(self, form, **kwargs):
        form.instance.profile = self.request.user.profile
        return super(ProfilePostCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.kwargs.get('pk')})

class ProfilePostUpdate(UpdateView):
    model = Post
    fields = ['city', 'title', 'description', 'image']
    template_name = "post_update.html"

    def form_valid(self, form, **kwargs):
        form.instance.profile = self.request.user.profile
        return super(ProfilePostUpdate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

class ProfilePostDelete(DeleteView):
    model = Post
    template_name = "profile_post_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})


class Post_Create(CreateView):
    model = Post
    fields = ['title', 'description', 'image']
    template_name = "post_create.html"

    def form_valid(self, form, **kwargs):
        form.instance.profile = self.request.user.profile
        form.instance.city = City.objects.get(pk=self.kwargs.get('pk'))
        return super(Post_Create, self).form_valid(form)

    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.kwargs.get('pk')})

class Post_Update(UpdateView):
    
    model = Post
    fields = ['title', 'description', 'image']
    template_name = "post_update.html"
    
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.kwargs.get('city_pk')})

    
class Post_Delete(DeleteView):
    model = Post
    template_name = "post_delete_confirmation.html"
    
    def get_success_url(self):
        return reverse('city_detail', kwargs={'pk': self.kwargs.get('city_pk')})

class CommentCreate(View):

    def post(self, request, pk):
        profile = self.request.user.profile
        post = Post.objects.get(pk=pk)
        description = request.POST.get("description")
        Comment.objects.create(profile=profile, post=post, description=description)
        return redirect('post_detail', pk=pk)

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['description']
    template_name = "comment_update.html"

    def form_valid(self, form, **kwargs):
        form.instance.profile = self.request.user.profile
        return super(CommentUpdate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('post_detail', kwargs={'pk': self.kwargs['post_pk']})

class CommentDelete(DeleteView):
    model = Comment
    template_name = "comment_delete_confirmation.html"

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.kwargs.get('post_pk')})