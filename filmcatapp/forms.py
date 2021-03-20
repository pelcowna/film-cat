from django import forms
from .models import Movie


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieForm(forms.ModelForm):
    BOTH = 'BT'
    NOBODY = 'NB'
    JULKASEEN = 'JK'
    PIOTREKSEEN = 'PK'
    SEEN_CHOICES = [
        (BOTH, 'both'),
        (NOBODY, 'nobody'),
        (JULKASEEN, 'Julka'),
        (PIOTREKSEEN, 'Piotrek')
    ]
    YEAR_CHOICES = reversed([(x, x) for x in range(1930, 2022)])
    title = forms.CharField(label='title', required=True)
    seen_by = forms.ChoiceField(label='seen_by', required=True, choices=SEEN_CHOICES)
    release_year = forms.ChoiceField(choices=YEAR_CHOICES, label='release_year', required=False)
    date_seen = forms.DateField(required=False, widget=DateInput)
    director = forms.CharField(label='director', max_length=50, required=False)
    tags = forms.CharField(label='tags', max_length=2500, required=False)

    class Meta:
        model = Movie
        fields = ['title', 'seen_by', 'release_year', 'date_seen', 'director', 'tags']


# class SearchMovieForm(forms.ModelForm):
