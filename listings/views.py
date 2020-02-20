from django.shortcuts import render


from .models import Listing


# Create your views here.
def index(request):
    listings = Listing.objects.all
    content = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', content)


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
