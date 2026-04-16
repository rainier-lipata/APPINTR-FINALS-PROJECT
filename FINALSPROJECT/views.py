from rest_framework import generics
from .models import  Student, Mentor, Admin, Session
from .serializers import (
    StudentSerializer,
    MentorSerializer,
    AdminSerializer,
    SessionSerializer,
)

class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all().order_by('last_name', 'first_name')
    serializer_class = StudentSerializer


class MentorListAPIView(generics.ListAPIView):
    queryset = Mentor.objects.all().order_by('last_name', 'first_name')
    serializer_class = MentorSerializer



class AdminListAPIView(generics.ListAPIView):
    queryset = Admin.objects.all().order_by('last_name', 'first_name')
    serializer_class = AdminSerializer



class SessionListAPIView(generics.ListAPIView):
    queryset = Session.objects.select_related(
        'student',
        'mentor',
    ).all().order_by('session_date')

    serializer_class = SessionSerializer