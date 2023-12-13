from django.urls import path, include
app_name = 'accounts'
from . import views
urlpatterns = [
    # Login page.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]