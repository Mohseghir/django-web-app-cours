from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm


def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici
    return render(request,
                  'listings/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def band_detail(request, id):
    band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    print(band)
    print(band.biography)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})  # nous mettons à jour cette ligne pour passer le groupe au gabarit


def band_list(request):  # renommer la fonction de vue
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',  # pointe vers le nouveau nom de modèle
                  {'bands': bands})


def about(request):
    return render(request, 'listings/about.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request,
                  'listings/listings.html',
                  {'listings': listings})