from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/rabbit_holes/', include('rabbit_holes.urls')),
    path('api/solutions/', include('solutions.urls')),
    path('api/images/', include('images.urls')),
    # path('media/images/', include('images.media_urls'))
]

# Allows use of working with the media folder locally
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)