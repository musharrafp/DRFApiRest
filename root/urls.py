from django.contrib import admin
from django.urls import path, include
from root.settings import STATIC_ROOT, STATIC_URL
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("api/", include("apps.urls")),
                  path("api/auth", include("rest_framework.urls")),
                  path("api/v1/", include("dj_rest_auth.urls")),
                  path("api/v1/register/", include("dj_rest_auth.registration.urls")),
              ] + static(STATIC_URL, document_root=STATIC_ROOT)
