from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("calculator/", include("calculator.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]
