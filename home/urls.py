from django.contrib import admin
from django.urls import path, include
from home import views
from django.views.static import serve
from django.conf.urls import url
from Monk import settings
urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path('accounts/', include('allauth.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':        settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
    # path("submitcontact", views.contact, name='contact'),
  

