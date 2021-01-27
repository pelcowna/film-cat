from django.contrib import admin
from .models import Movie, UserProfile


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ["title", "release_year"]
    # exclude = ["seen"]
    list_display = ["title_year", "date_seen", "seen_by"]  # array
    list_filter = ("date_seen", "release_year", "seen_by")  # tuple


admin.site.register(UserProfile)
