from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('events/', include('events.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    url('^api/vl/', include('social_django.urls', namespace='social'))

         ]
