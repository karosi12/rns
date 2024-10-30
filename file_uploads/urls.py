from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_file


urlpatterns = [
    path('', upload_file, name='files'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)