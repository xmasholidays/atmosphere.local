from django.db import models
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField


class Audio(models.Model):
    title = models.CharField(max_length=250)
    is_background = models.BooleanField()
    rawfile = FilerFileField(null=True, blank=True,
                             related_name="song_rawfile")
    picture = FilerImageField(null=True, blank=True,
                           related_name="song_picture")

    @property
    def path(self):
        if not self.rawfile:
            return None
        return self.rawfile.path

    @property
    def image(self):
        if not self.picture:
            return None
        return self.picture.path

    def __str__(self):
        return self.title


class Request(models.Model):
    audio = models.ForeignKey(Audio)
