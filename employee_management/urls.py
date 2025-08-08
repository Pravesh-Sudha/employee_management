from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def health(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # Include the employees app routes
    path('health', health, name='health'),  # No trailing slash for ALB
    path('health/', health, name='health_slash'),  # With trailing slash
]
