"""spot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.urls import include
from rest_framework import routers

from playlist.viewsets import Record_ViewSet, Genre_ViewSet, Band_ViewSet, Music_ViewSet, Playlist_ViewSet

router = routers.DefaultRouter()
router.register(r'Record', Record_ViewSet, base_name='Record')
router.register(r'Genre', Genre_ViewSet, base_name='Genre')
router.register(r'Band', Band_ViewSet, base_name='Band')
router.register(r'Music', Music_ViewSet, base_name='Music')
router.register(r'Playlist', Playlist_ViewSet, base_name='Playlist')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
