from django.contrib import admin
from django.urls import path, include
import oppium_fashion.urls

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include(oppium_fashion.urls, namespace='oppium_fashion'))
]


app_name = 'oppium_fashion'