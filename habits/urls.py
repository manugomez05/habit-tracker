from django.urls import path
from .views import persona

urlpatterns = [
    path('',persona),
]