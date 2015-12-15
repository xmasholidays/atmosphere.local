from django.db import models
from filer.fields.file import FilerFileField


class Song(models.Model):
    title = models.CharField(max_length=150)
    artist = models.CharField(max_length=100)
    is_background = models.BooleanField()
    rawfile = FilerFileField(null=True, blank=True,
                             related_name="song_rawfile")

    @property
    def path(self):
        if not self.rawfile:
            return None
        return self.rawfile.path


class Request(models.Model):
    song = models.ForeignKey(Song)
