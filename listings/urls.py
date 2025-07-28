
from django.urls import path
from . import views
urlpatterns = [
    path("", view= views.listing_list, name="listings"),
    path("listings/<pk>", view = views.read_list, name="list_item"),
    path("create_listing/", view = views.create_list, name="create_list")
]
