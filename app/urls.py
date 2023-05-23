from django.urls import path
from . import views

# App URL conf
urlpatterns = [
    path('', views.index)
]
