"""filmcat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include


urlpatterns = [
    path('', views.home),
    path('login/',
         LoginView.as_view(template_name='filmcatapp/login.html'), name='login'),
    path('logout/',
         LogoutView.as_view(template_name='filmcatapp/logout.html'), name='logout'),
    # path('log/', include('django.contrib.auth.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.profile),
    path('add_movie/', views.add_movie),
    path('all_movies/', views.all_movies),
    path('movies_seen_all/', views.movies_seen_all),
    path('movies_seen_nobody/', views.movies_seen_nobody),
    path('movies_seen_julka/', views.movies_seen_julka),
    path('movies_seen_piotrek/', views.movies_seen_piotrek),
]
