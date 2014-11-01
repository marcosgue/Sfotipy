from django.contrib import admin

from .models import Artist

from tracks.models import Track


class TrackInline(admin.StackedInline):
    model = Track
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
    inlines = [TrackInline, ]

admin.site.register(Artist, ArtistAdmin)
