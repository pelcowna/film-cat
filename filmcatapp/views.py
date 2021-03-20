from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import MovieForm


def home(request):
    template_name = 'filmcatapp/home.html'
    return render(request, template_name)


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/all_movies')
    else:
        form = MovieForm()
        args = {'form': form}
        template_name = 'filmcatapp/add_movie.html'
        return render(request, template_name, args)


def all_movies(request):
    movies_all = Movie.objects.all().order_by('-date_seen')
    args = {'movies': movies_all}
    template_name = 'filmcatapp/all_movies.html'
    return render(request, template_name, args)


def find_movie(request):
    template_name = 'filmcatapp/find_movie.html'
    # if request.method == 'POST':
    #     form = SearchMovieForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         movies_found = Movie.objects.filter(seen_by='BT')
    #         args = {'movies_found': movies_found}
    #         return redirect('/find_movie_results', args)

    return render(request, template_name)


# def find_movie_results(request):
#     template_name = 'filmcatapp/find_movie_results.html'
#     return render(request, template_name)


def movies_seen_by(request, person):
    pers = 'BT'
    if person == 'nobody':
        pers = 'NB'
    if person == 'Julka':
        pers = 'JK'
    if person == 'Piotrek':
        pers = 'PK'
    movies_seen = Movie.objects.filter(seen_by=pers).order_by('-date_seen')
    args = {'movies_seen': movies_seen, 'person': person}
    template_name = 'filmcatapp/movies_seen_by.html'
    return render(request, template_name, args)


def edit_movie(request, title):
    movie = get_object_or_404(Movie, pk=title)
    template_name = 'filmcatapp/edit_movie.html'

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)

        if form.is_valid():
            movie.title = form.cleaned_data['title']
            movie.seen_by = form.cleaned_data['seen_by']
            movie.director = form.cleaned_data['director']
            movie.release_year = form.cleaned_data['release_year']
            movie.date_seen = form.cleaned_data['date_seen']
            movie.tags = form.cleaned_data['tags']
            movie.save()
            return redirect('/all_movies')
    else:
        form = MovieForm(initial={
                            'title': movie.title,
                            'seen_by': movie.seen_by,
                            'director': movie.director,
                            'release_year': movie.release_year,
                            'date_seen': movie.date_seen,
                            'tags': movie.tags})

        args = {'form': form}
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
