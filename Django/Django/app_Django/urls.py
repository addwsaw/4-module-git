from django.urls import path
from .views import index, top_sellers

urlpatterns =[
    path('index/', index),
    path('top-sellers/', top_sellers),
]