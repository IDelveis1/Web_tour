from django.urls import path, include
from django.contrib import admin
from tours.views import custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),
]

handler404 = custom_handler404