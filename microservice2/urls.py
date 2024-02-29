from django.contrib import admin
from django.urls import path, include
admin.site.site_header='Microservice2-Admin'
admin.site.site_header = "Microservice2-Admin'"
admin.site.site_title = "MS2-Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]
