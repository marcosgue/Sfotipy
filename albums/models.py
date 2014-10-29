from django.db import models

from artist.models import Artist


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = models.FileField(upload_to="albums")
    artist = models.ForeignKey(Artist)
