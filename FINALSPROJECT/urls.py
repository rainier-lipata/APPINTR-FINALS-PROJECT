from django.urls import path
from .views import (
    StudentListAPIView,
    MentorListAPIView,
    AdminListAPIView,
    SessionListAPIView,
<<<<<<< HEAD
    ExpertiseListAPIView,
    MentorAvailabilityListAPIView,
    StudentPreferenceListAPIView,
    MentorMatchAPIView,  # optional but recommended
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
=======
)

urlpatterns = [
    path('students/', StudentListAPIView.as_view()),
    path('mentors/', MentorListAPIView.as_view()),
    path('admins/', AdminListAPIView.as_view()),
    path('sessions/', SessionListAPIView.as_view()),
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
]