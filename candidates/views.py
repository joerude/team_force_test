from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginUserForm, RegisterUserForm, AddSkillForm
from .models import Profile, Skill, SkillSet


class CreateProfileView(LoginRequiredMixin, CreateView):
    template_name = "candidates/profile_page.html"
    form_class = AddSkillForm
    success_url = reverse_lazy("home")
    login_url = reverse_lazy("home")
    raise_exception = True


def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    context["user_data"] = Profile.objects.filter(user=self.request.user.id)
    return context


class SkillCreateView(CreateView):
    model = Skill
    template_name = "candidates/skill_new.html"
    fields = ["skill_name", "skill_set"]

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super(SkillCreateView, self).form_valid(form)


class SkillSetCreateView(CreateView):
    model = SkillSet
    template_name = "candidates/skill_new.html"
    fields = ["name"]

    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super(SkillSetCreateView, self).form_valid(form)


class HomeView(ListView):
    template_name = "home.html"
    model = Profile


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "candidates/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "candidates/signin.html"

    def get_success_url(self):
        return reverse_lazy("home")


def logout_user(request):
    logout(request)
    return redirect("login")
