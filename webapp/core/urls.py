from django.contrib import admin
from django.urls import include, path

# API_PREFIX = "api/v1" .. # oops we are using templates i forgot

urlpatterns = [
    path("admin/", admin.site.urls),
    path("chat/", include("chat.urls")),
]
