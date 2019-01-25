from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('feed.urls')),
    url(r'admin/', admin.site.urls),
    url(r'feed/', include('feed.urls'))
]
