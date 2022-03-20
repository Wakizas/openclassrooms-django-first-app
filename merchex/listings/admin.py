from django.contrib import admin
from .models import Band, Listing

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed')
    
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'sold')
    
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
