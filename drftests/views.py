from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, permissions, generics

# myapp imports
from serializers import ShowSerializer, VenueSerializer, BandSerializer, ShowBandSerializer
from models import Show, Venue, Band, ShowBand

class ListAllShows(generics.ListCreateAPIView):
    """
    If there is not a show at this specific time and date, create a new show
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class ListOrCreateVenues(generics.ListCreateAPIView):
    """
    Get a list of venues or post a new venue
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = VenueSerializer
    queryset = Venue.objects.all()

class ListOrCreateBand(generics.ListCreateAPIView):
    """
    Get a list of Bands or post a new band
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = BandSerializer
    queryset = Band.objects.all()

class ListOrCreateShowBand(generics.ListCreateAPIView):
    """
    Get a list of showbands or post a new showbamd
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ShowBandSerializer
    queryset = ShowBand.objects.all()

