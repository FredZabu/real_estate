from django.shortcuts import render
from .models import listing
# Create your views here.

def listing_list(request):
    listings = listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "index.html", context)