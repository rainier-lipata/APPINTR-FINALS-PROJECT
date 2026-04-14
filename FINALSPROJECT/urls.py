from django.urls import path
from .views import (
    RoleListAPIView,
    StatusListAPIView,
    StudentListAPIView,
    MentorListAPIView,
    AdminListAPIView,
    SessionListAPIView,
)

urlpatterns = [
    path('roles/', RoleListAPIView.as_view()),
    path('status/', StatusListAPIView.as_view()),
    path('students/', StudentListAPIView.as_view()),
    path('mentors/', MentorListAPIView.as_view()),
    path('admins/', AdminListAPIView.as_view()),
    path('sessions/', SessionListAPIView.as_view()),
]