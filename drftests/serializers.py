__author__ = 'wjessen'

from drftests.models import Show, Venue, Band, ShowBand
from rest_framework import serializers

class ShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        depth = 1

class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue


class BandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Band


class ShowBandSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowBand
        depth = 1