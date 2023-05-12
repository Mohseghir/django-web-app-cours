from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')  # liste les champs que nous voulons sur l'affichage de la liste


admin.site.register(Band, BandAdmin)
admin.site.register(Listing)# nous modifions cette ligne, en ajoutant un deuxième argument
# Register your models here.
