
from django.contrib import admin
from django.urls import path, include



admin.site.site_header = "Monk"
admin.site.site_title = "Monk Admin Portal"
admin.site.index_title = "Welcome to Monk Researcher Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
]
