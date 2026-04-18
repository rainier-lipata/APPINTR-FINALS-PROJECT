from django.urls import path
from .views import (
    StudentListCreateAPIView,
    StudentRetrieveUpdateAPIView,
    StudentDeleteAPIView,
    MentorListCreateAPIView,
    MentorRetrieveUpdateAPIView,
    MentorDeleteAPIView,
    AdminListAPIView,
    SessionListAPIView,
    ExpertiseListAPIView,
    MentorAvailabilityListAPIView,
    StudentPreferenceListAPIView,
    MentorMatchAPIView,
)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path(
    'students/<int:pk>/', StudentRetrieveUpdateAPIView.as_view(), name='student-detail-update' ),
    path('students/<int:pk>/delete/', StudentDeleteAPIView.as_view() , name='student-delete' ),
    path('mentors/', MentorListCreateAPIView.as_view(), name='mentor-detail-update' ),
    path('mentors/<int:pk>/', MentorRetrieveUpdateAPIView.as_view(), name='mentor-list-'),
    path('mentors/<int:pk>/delete/', MentorDeleteAPIView.as_view(), name='mentor-delete'),
    path('mentors/match/<int:student_id>/', MentorMatchAPIView.as_view(), name='mentor-match'),
    path('expertise/', ExpertiseListAPIView.as_view(), name='expertise-list'),
    path('mentor-availability/', MentorAvailabilityListAPIView.as_view(), name='mentor-availability-list'),
    path('student-preferences/', StudentPreferenceListAPIView.as_view(), name='student-preference-list'),
    path('admins/', AdminListAPIView.as_view(), name='admin-list'),
    path('sessions/', SessionListAPIView.as_view(), name='session-list'),
]