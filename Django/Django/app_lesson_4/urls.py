from django.urls import path
from .views import index

urlpatterns =[
    path('app_lesson_4/', index)
]