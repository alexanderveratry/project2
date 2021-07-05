from django.shortcuts import render
from django.urls import reverse
from .models import Listing
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, "listing/index.html", {
        "listing": Listing.objects.all()
    })


@login_required(login_url='login')
def listing(request, listing_id):
    list = Listing.objects.get(id=listing_id)
    return render(request, "listing/list.html", {
        "flight": list,

    })
@login_required(login_url='login')
def list(request, listing_id):
    return render(request, "listing/list.html", {
        "listing": Listing.objects.get(id=listing_id),

    })


