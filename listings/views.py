from django.shortcuts import render, redirect
from .models import listing
from .form import ListingForm
# Create your views here.

def listing_list(request):
    listings = listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "index.html", context)
def read_list(request, pk):
    item = listing.objects.get(id = pk)
    context = {
        "item": item
    }
    return render(request, "item.html", context)

def create_list(request):
    form = ListingForm()
    if request.method == "POST":       
        form = ListingForm(request.POST)      
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {
        "form": form
    }
    return render(request, "form.html", context)