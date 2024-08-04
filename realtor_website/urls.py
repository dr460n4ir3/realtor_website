from django.contrib import admin
from django.urls import path

from listings.views import (
    listing_list, 
    listing_retrieve, 
    listing_create, 
    listing_update, 
    listing_delete
)

# from users.views import registered_list, registered_retrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list), # This will call the listing_list view when the home page is visited
    path('listing/<pk>/', listing_retrieve), # This will call the listing_retrieve view when a listing is visited
    #path('register/', registered_list), # This will call the listing_list view when the register page is visited
    #path('user/<pk>/', registered_retrieve), # This will call the listing_retrieve view when a user is visited
    path('create/', listing_create), # This will call the listing_create view when the create page is visited
    path('listing/<pk>/update/', listing_update), # This will call the listing_update view when a listing is updated
    path('listing/<pk>/delete/', listing_delete), # This will call the listing_delete view when a listing is deleted
]
