from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Futebol Arte'

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
