"""project_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from wishlist.views import id_funct_json, id_funct_xml, show_wishlist, xml_funct, json_funct


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('example_app.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('', xml_funct),
    path('', json_funct),
    path('', id_funct_xml),
    path('', id_funct_json),


]
