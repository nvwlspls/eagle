from django.contrib import admin

from models import Show, Band, ShowBand, Venue
# Register your models here.
admin.site.register(Show)
admin.site.register(Band)
admin.site.register(ShowBand)
admin.site.register(Venue)