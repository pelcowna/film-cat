from django.shortcuts import render, redirect
from .models import Movie
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import AddMovieForm


def home(request):
    template_name = 'filmcatapp/home.html'
    return render(request, template_name)


def add_movie(request):
    if request.method == 'POST':
        form = AddMovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/all_movies')
    else:
        form = AddMovieForm()
        args = {'form': form}
        template_name = 'filmcatapp/add_movie.html'
        return render(request, template_name, args)


def all_movies(request):
    movies_all = Movie.objects.all().order_by('title')
    args = {'movies': movies_all}
    template_name = 'filmcatapp/all_movies.html'
    return render(request, template_name, args)


def movies_seen_all(request):
    movies_seen = Movie.objects.filter(seen_by='BT').order_by('-date_seen')
    args = {'movies_seen': movies_seen}
    template_name = 'filmcatapp/movies_seen_all.html'
    return render(request, template_name, args)


def movies_seen_nobody(request):
    movies_seen = Movie.objects.filter(seen_by='NB')
    args = {'movies_seen': movies_seen}
    template_name = 'filmcatapp/movies_seen_nobody.html'
    return render(request, template_name, args)


def movies_seen_julka(request):
    movies_seen = Movie.objects.filter(seen_by='JK').order_by('-date_seen')
    args = {'movies_seen': movies_seen}
    template_name = 'filmcatapp/movies_seen_julka.html'
    return render(request, template_name, args)


def movies_seen_piotrek(request):
    movies_seen = Movie.objects.filter(seen_by='PK').order_by('-date_seen')
    args = {'movies_seen': movies_seen}
    template_name = 'filmcatapp/movies_seen_piotrek.html'
    return render(request, template_name, args)


def profile(request):
    logged_in_user = request.user
    args = {'user': logged_in_user}
    template_name = 'filmcatapp/profile.html'
    return render(request, template_name, args)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'filmcatapp/signup.html'
