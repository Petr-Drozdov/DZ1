from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from MainApp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('item/', views.items),
    path('item/', views.item_details),
]
