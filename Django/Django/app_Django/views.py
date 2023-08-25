from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Advertisements
from .forms import AdvertisementsForms

def index(request):
    advertisements = Advertisements.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementsForms(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisements(**form.cleaned_data)
            advertisement.User = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementsForms()
    context = {
        'form': form
    }
    return render(request, 'advertisement-post.html', context)
def login(request):
    return render(request, 'login.html')
def profile(request):
    return render(request, 'profile.html')
def register(request):
    return render(request, 'register.html')
# Create your views here.
