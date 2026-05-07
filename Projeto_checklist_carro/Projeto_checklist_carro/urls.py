from django.contrib import admin
from django.urls import path, include
from django.conf import settings # ADICIONADO
from django.conf.urls.static import static # ADICIONADO

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_checklist.urls')),
]

# ADICIONADO: Isso diz ao Django onde procurar as imagens durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)