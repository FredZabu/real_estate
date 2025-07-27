
from django.urls import path
from . import views
urlpatterns = [
    path("", view= views.listing_list, name="listings")
]
