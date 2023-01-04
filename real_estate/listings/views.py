from django.shortcuts import redirect, render

from .forms import ListingForm
from .models import Listing


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    context ={
        "form": form
    }
    return render(request, 'listing_create.html', context)

def listing_update(request, pk):
    form = ListingForm()
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, files=request.FILES, instance=Listing)
        if form.is_valid():
            form.save()
            return redirect("/")

    context ={
        "form": form
    }
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    Listing = Listing.objects.get(id=pk)
    Listing.delete()
    return redirect('/')
