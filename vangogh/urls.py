"""vangogh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers

from album import views as album_views
from person import views as person_views
from photo import views as photo_views

routers = routers.DefaultRouter()
routers.register(r'api/photos', photo_views.PhotoViewSet)
routers.register(r'api/people', person_views.PersonViewSet)
routers.register(r'api/faces', person_views.FaceViewSet)
routers.register(r'api/people/(?P<person_id>\d+)/faces', person_views.PersonFaceViewSet, basename='face')
routers.register(r'api/albums', album_views.AlbumViewSet)
routers.register(r'api/albums/(?P<album_id>\d+)/photos', photo_views.AlbumPhotoViewSet, basename='photo')

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
