from django.urls import path
from .views import (
    StudentListAPIView,
    MentorListAPIView,
    AdminListAPIView,
    SessionListAPIView,
)

urlpatterns = [
    path('students/', StudentListAPIView.as_view()),
    path('mentors/', MentorListAPIView.as_view()),
    path('admins/', AdminListAPIView.as_view()),
    path('sessions/', SessionListAPIView.as_view()),
]