from django import forms
from .models import Movie


class AddMovieForm(forms.ModelForm):
    BOTH = 'BT'
    NOBODY = 'NB'
    JULKASEEN = 'JK'
    PIOTREKSEEN = 'PK'
    SEEN_CHOICES = [
        (BOTH, 'obydwojgoro'),
        (NOBODY, 'nikt'),
        (JULKASEEN, 'Julka'),
        (PIOTREKSEEN, 'Piotrek')
    ]
    title = forms.CharField(label='title', required=True)
    seen_by = forms.ChoiceField(label='seen_by', required=True, choices=SEEN_CHOICES)
    release_year = forms.IntegerField(label='release_year', required=False, min_value=1900, max_value=2020)
    date_seen = forms.DateField(required=False)

    class Meta:
        model = Movie
        fields = ['title', 'seen_by', 'release_year', 'date_seen']
