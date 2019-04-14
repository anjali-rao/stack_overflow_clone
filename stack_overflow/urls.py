from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^', include('userprofile.urls')),
    url(r'^questions/', include('questions.urls')),
]
