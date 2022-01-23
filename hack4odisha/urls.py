from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "Heart Beat Admin"
admin.site.site_header = "Heart Beat Admin"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
