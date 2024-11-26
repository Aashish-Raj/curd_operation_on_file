
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('document',DocumentListingView.as_view(),name='document'),
]
