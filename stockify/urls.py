from django.contrib import admin
from django.urls import path, include
from dashboard import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("user.urls")),
    path('', include("dashboard.urls"))
]

data.browser()