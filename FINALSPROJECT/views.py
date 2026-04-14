from rest_framework import generics
from .models import Role, Status, Student, Mentor, Admin, Session
from .serializers import (
    RoleSerializer,
    StatusSerializer,
    StudentSerializer,
    MentorSerializer,
    AdminSerializer,
    SessionSerializer,
)



class RoleListAPIView(generics.ListAPIView):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer



class StatusListAPIView(generics.ListAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer



class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.select_related(
        'role',
        'status'
    ).all().order_by('last_name', 'first_name')

    serializer_class = StudentSerializer



class MentorListAPIView(generics.ListAPIView):
    queryset = Mentor.objects.select_related(
        'role',
        'status'
    ).all().order_by('last_name', 'first_name')

    serializer_class = MentorSerializer



class AdminListAPIView(generics.ListAPIView):
    queryset = Admin.objects.select_related(
        'role'
    ).all().order_by('last_name', 'first_name')

    serializer_class = AdminSerializer



class SessionListAPIView(generics.ListAPIView):
    queryset = Session.objects.select_related(
        'student',
        'mentor',
        'status'
    ).all().order_by('session_date')

    serializer_class = SessionSerializer