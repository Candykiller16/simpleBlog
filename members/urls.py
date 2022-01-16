from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path('reqister/', UserRegisterView.as_view(), name='register'),
]