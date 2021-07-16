from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/myapp',views.my_model,name="my_model"),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('cars/', include('cars.urls')),
    path('accounts/', include('accounts.urls')),
    path('socialaccounts/', include('allauth.urls')),
    path('contacts/', include('contacts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
