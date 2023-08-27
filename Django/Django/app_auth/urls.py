from django.urls import path
from .views import view_login, view_profile, view_register, logout_view
urlpatterns = [
    path('login/', view_login, name='login'),
    path('profile/', view_profile, name='profile'),
    path('register/', view_register, name='register'),
    path('logout/', logout_view, name='logout')
]
