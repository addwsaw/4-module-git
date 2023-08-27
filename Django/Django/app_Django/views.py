from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from .models import Advertisements
from .forms import AdvertisementsForms

def index(request):
    advertisements = Advertisements.objects.all()
    context = {
        'advertisements': advertisements
    }
    return render(request, 'app_Django/index.html', context)
def top_sellers(request):
    return render(request, 'app_Django/top-sellers.html')
@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'app_Django/advertisement-post.html', context)
def login(request):
    return render(request, 'app_auth/login.html')
def profile(request):
    return render(request, 'app_auth/profile.html')
def register(request):
    return render(request, 'app_auth/register.html')
# Create your views here.
