import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', include('app.urls'))
]
if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]