from django.urls import path
from . import views

urlpatterns = [
    path('chatgpt/', views.chatgtp.as_view(), name="chatgpt")
]