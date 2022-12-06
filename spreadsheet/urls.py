from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from sheetapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload-csv/', profile_upload, name="profile_upload"),
]