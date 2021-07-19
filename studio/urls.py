from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main"),
    path("search/", views.Search, name="search"),
    path("service/", services, name="service"),
    path("studio/", views.StudioView.as_view(), name="studio"),
    path("portfolio/", views.ProjectView.as_view(), name="portfolio"),
    path("portfolio/", views.ProjectView.as_view(), name="portfolio"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("registration/", registration, name="registration"),
    path("profile/", views.Profile.as_view(), name="profile"),
    path("profile/<slug:slug>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("<slug:slug>/", views.ProjectDetailView.as_view(), name="project_detail"),
]
