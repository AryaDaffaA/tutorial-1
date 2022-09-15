from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml_funct
from wishlist.views import json_funct
from wishlist.views import id_funct_json
from wishlist.views import id_funct_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_funct, name='xml_funct'),
    path('json/', json_funct, name='json_funct'),
    path('xml/<int:id>', id_funct_xml, name='id_funct_xml'),
    path('json/<int:id>', id_funct_json, name='id_funct_json'),
]