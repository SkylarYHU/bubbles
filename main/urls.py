from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('home',views.home,name="home"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("create-post", views.create_post, name="create_post")
]
