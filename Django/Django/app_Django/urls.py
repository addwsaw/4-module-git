from django.urls import path
from .views import index, top_sellers, advertisement_post, login, profile, register

urlpatterns = [
    path('index/', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
]
