from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import parameter
from wishlist.views import parajson
from wishlist.views import paraxmlid
from wishlist.views import parajsonid
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', parameter, name='parameter'),
    path('json/', parajson, name='parajson'),
    path('json/<int:id>', paraxmlid, name='paraxmlid'), 
    path('json/<int:id>', parajsonid, name='parajsonid'), 
]