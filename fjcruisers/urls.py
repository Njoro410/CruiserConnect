from django.contrib import admin
from django.urls import path
from fjcruisers import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'userprofiles', views.UserProfile, 'userprofile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/userprofile/', views.UserProfile, name='userProfile'),
]