__author__ = 'wjessen'
from django.conf.urls import url, include
from django.contrib import admin
import drftests.views as views

urlpatterns = [
    url(r'^$', views.ListAllShows.as_view(), name="listallshows"),
    url(r'^venues/$', views.ListOrCreateVenues.as_view(), name="listallvenues"),
    url(r'^bands/', views.ListOrCreateBand.as_view(), name="listallbands"),
    url(r'^showbands/', views.ListOrCreateShowBand.as_view(), name="listallshowbands"),
]