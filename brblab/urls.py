from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('access.urls', namespace='access')),
    path('', include('event.urls', namespace='event')),
    path('', include('users.urls', namespace='users')),
]
