
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf.urls import url
from Monk import settings


admin.site.site_header = "Monk"
admin.site.site_title = "Monk Admin Portal"
admin.site.index_title = "Welcome to Monk Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

