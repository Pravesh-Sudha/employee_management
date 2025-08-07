from django.contrib import admin
from django.urls import path, include

def health(request):
    return HttpResponse("OK", status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),  # Include the employees app routes
    path('health/', health, name='health'),
]
