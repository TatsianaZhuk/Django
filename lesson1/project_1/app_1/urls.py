from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('items', views.show_all, name='main'),
    path('items_admin', views.show_all_admin, name='admin'),
    path('items/<int:item_id>', views.show_item, name='item')
]
