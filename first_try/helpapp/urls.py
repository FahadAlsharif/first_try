from logging import root
from django.urls import path

from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new',views.new),
    path('blogs/<number>',views.num),
    path('blogs/<number>/edit',views.edit),
    path('blogs/<number>/delete',views.destroy)
]
