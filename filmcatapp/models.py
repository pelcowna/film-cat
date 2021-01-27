from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
# from django.db.models.signal import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Movie(models.Model):
    # making available choices - who saw the movie
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

    title = models.CharField(max_length=100, primary_key=True, unique=True)
    release_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1900), MaxValueValidator(2020)]
    )
    date_seen = models.DateField(blank=True, null=True)
    seen_by = models.CharField(
        choices=SEEN_CHOICES,
        max_length=2,
        blank=False,
        default='NB'
    )
    # filmweb search url: https://www.filmweb.pl/search?q=irishman

    def __str__(self):
        return self.title_year()
        # return self.title + ' (' + str(self.release_year) + ')'

    def title_year(self):
        return "{} ({})".format(self.title, self.release_year)
