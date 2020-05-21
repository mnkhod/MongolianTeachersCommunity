from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns as lang

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TeachersCommunityProject.MainWeb.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
