from django.urls import path
from wishlist.views import (
    show_wishlist,
    ajax_views,
    add_wish,
    parameter,
    parajson,
    paraxmlid,
    parajsonid,
    register,
    login_user,
    logout_user,
    
)
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', ajax_views, name='ajax_views'),
    path('ajax/submit/', add_wish, name='add_wish'),
    path('xml/', parameter, name='parameter'),
    path('json/', parajson, name='parajson'),
    path('json/<int:id>', paraxmlid, name='paraxmlid'), 
    path('json/<int:id>', parajsonid, name='parajsonid'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
]