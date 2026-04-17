from django.urls import path
from .views import (
    StudentListAPIView,
    MentorListAPIView,
    AdminListAPIView,
    SessionListAPIView,
    ExpertiseListAPIView,
    MentorAvailabilityListAPIView,
    StudentPreferenceListAPIView,
    MentorMatchAPIView,
)

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='student-list'),

    path('mentors/', MentorListAPIView.as_view(), name='mentor-list'),

    path('mentors/match/<int:student_id>/', MentorMatchAPIView.as_view(), name='mentor-match'),

    path('expertise/', ExpertiseListAPIView.as_view(), name='expertise-list'),

    path('mentor-availability/', MentorAvailabilityListAPIView.as_view(), name='mentor-availability-list'),

    path('student-preferences/', StudentPreferenceListAPIView.as_view(), name='student-preference-list'),

    path('admins/', AdminListAPIView.as_view(), name='admin-list'),

    path('sessions/', SessionListAPIView.as_view(), name='session-list'),
]