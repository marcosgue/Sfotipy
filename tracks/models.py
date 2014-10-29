from django.db import models


class Track(models.Model):
    track = models.CharField(max_length=255)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
