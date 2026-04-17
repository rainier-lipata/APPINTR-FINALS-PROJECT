from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD

    # API routes (connects to FINALSPROJECT/urls.py)
=======
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
    path('api/', include('FINALSPROJECT.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )