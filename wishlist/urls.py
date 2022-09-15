from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import parameter
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', parameter, name=’parameter’),
]