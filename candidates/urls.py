from django.contrib.auth.views import LogoutView
from django.urls import path

from config import settings

from .views import (
    HomeView,
    LoginUser,  # ContactsView,; CreateProfileView,
    RegisterUser,
    SkillCreateView,
    SkillSetCreateView,
    logout_user, CreateProfileView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("new_skill/", SkillCreateView.as_view(), name="skill_new"),  # new
    path("new_skillset/", SkillSetCreateView.as_view(), name="skillset_new"),  # new
    path("profile_page/", CreateProfileView.as_view(), name="profile_page"),
    path("signin/", LoginUser.as_view(), name="signin"),
    path("signup/", RegisterUser.as_view(), name="signup"),
    path("logout/", logout_user, name="logout"),
    path(
        "signout/",
        LogoutView.as_view(),
        {"next_page": settings.base.LOGOUT_REDIRECT_URL},
        name="signout",
    ),
]
