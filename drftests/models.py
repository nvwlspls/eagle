from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Show(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    venue = models.ForeignKey('Venue', default=1)
    bands = models.ManyToManyField('Band')

    class Meta:
        ordering = ('date', 'time',)

    def __unicode__(self):
        return str(self.venue.name + " " + str(self.time))

class Venue(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __unicode__(self):
        return str(self.name)

class Band(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    shows = models.ManyToManyField('Show')

    def __unicode__(self):
        return str(self.name)

class ShowBand(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    band = models.ForeignKey('Band')
    show = models.ForeignKey('Show')
    order = models.IntegerField()

    def __unicode__(self):
        return str(self.band.name + " at " + self.show.venue.name + " on " + str(self.show.date))

    class Meta:
        ordering = ('order',)
