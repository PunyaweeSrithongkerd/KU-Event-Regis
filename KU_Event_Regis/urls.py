from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from events.views import signup

from .views import redirect_events

from . import views, settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('events/', include('events.urls')),
    path('', redirect_events),
    path('admin/', admin.site.urls),
    path('accounts/', include('events.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('social_django.urls', namespace='social')),
    url('^api/vl/', include('social_django.urls', namespace='social')),
    url('signup/', signup, name='signup'),
         ]

##if settings.DEBUG:
##        urlpatterns += static(settings.MEDIA_URL,
##                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
