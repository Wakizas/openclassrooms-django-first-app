from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Band, Listing
from .forms import ContactUsForm
from .forms import BandForm

# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_create(request):
    if request.method == 'POST':
        bandform = BandForm(request.POST)
        if bandform.is_valid():
            band = bandform.save()
            return redirect('band-detail', band.id)
    else:
        bandform = BandForm()
    return render(request, 'listings/band_create.html', {'bandform': bandform})


def about(request):
    return render(request, 'listings/about.html')


def listing_list(request):
    merchs = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'merchs': merchs})


def listing_detail(request, listing_id):
    merch = get_object_or_404(Listing, id=listing_id)
    return render(request, 'listings/listing_detail.html', {'merch': merch})


def related_listing(request, band_id):
    band = get_object_or_404(Band, id=band_id)
    return render(request, 'listings/related_listings.html', {'band': band})


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['melvindogbo@protonmail.com', 'melvindogbo@tutanota.com'],
        )
            return redirect('band-list')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html', {'form': form})
