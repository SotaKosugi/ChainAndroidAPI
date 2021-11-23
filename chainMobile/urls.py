from django.contrib import admin
from django.urls import include, path

import chainApi


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chainApi.urls')),
  
]


