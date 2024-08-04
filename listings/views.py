from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# Create your views here.
def listing_list(request):
    listings = Listing.objects.all() # This will get all the listings from the database
    # context is a dictionary that will be passed to the template
    context = {
        'listings': listings
    }
    return render(request, 'listings.html', context) # This will pass the listings.html to the template

def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk) # This will get the specific listing from the database
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') # This will redirect to the listing_list view after the form is submitted

    context = {
        'form': form
    }
    return render(request, 'listing_create.html', context)

def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'listing_update.html', context)

def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')