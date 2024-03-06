from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name='index'),
    path("<int:x>", views.cal , name='cal'),
    path("tax", views.tax , name='tax'),
]