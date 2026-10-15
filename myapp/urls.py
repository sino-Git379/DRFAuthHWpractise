from django.urls import path
from .views import RegisterAPIView, LoginAPIViw, ProfileAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIViw.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile')
]
