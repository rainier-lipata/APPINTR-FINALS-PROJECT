from rest_framework import generics
from .models import (
    Student, Mentor, Admin, Session,
    Expertise, MentorAvailability, StudentPreference
)

from .serializers import (
    StudentSerializer,
    MentorSerializer,
    AdminSerializer,
    SessionSerializer,
    ExpertiseSerializer,
    MentorAvailabilitySerializer,
    StudentPreferenceSerializer
)


class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all().order_by('last_name', 'first_name')
    serializer_class = StudentSerializer


class MentorListAPIView(generics.ListAPIView):
    queryset = Mentor.objects.prefetch_related(
        'expertise'
    ).all().order_by('last_name', 'first_name')

    serializer_class = MentorSerializer


class ExpertiseListAPIView(generics.ListAPIView):
    queryset = Expertise.objects.all().order_by('name')
    serializer_class = ExpertiseSerializer


class MentorAvailabilityListAPIView(generics.ListAPIView):
    queryset = MentorAvailability.objects.select_related(
        'mentor'
    ).all()

    serializer_class = MentorAvailabilitySerializer


class MentorMatchAPIView(generics.ListAPIView):
    serializer_class = MentorSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']

        try:
            pref = StudentPreference.objects.get(student_id=student_id)
        except StudentPreference.DoesNotExist:
            return Mentor.objects.all()

        queryset = Mentor.objects.prefetch_related('expertise')

        if pref.preferred_department:
            queryset = queryset.filter(
                department=pref.preferred_department
            )

        if pref.preferred_expertise:
            queryset = queryset.filter(
                expertise__name__icontains=pref.preferred_expertise
            )

        return queryset.distinct().order_by('last_name')



class StudentPreferenceListAPIView(generics.ListAPIView):
    queryset = StudentPreference.objects.select_related(
        'student'
    ).all()

    serializer_class = StudentPreferenceSerializer


class AdminListAPIView(generics.ListAPIView):
    queryset = Admin.objects.all().order_by('last_name', 'first_name')
    serializer_class = AdminSerializer


class SessionListAPIView(generics.ListAPIView):
    queryset = Session.objects.select_related(
        'student',
        'mentor',
    ).all().order_by('session_date')

    serializer_class = SessionSerializer