from rest_framework import serializers
from .models import  Student, Mentor, Admin, Session


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'student_number',
            'last_name',
            'first_name',
            'middle_initial',
            'college',
            'department',
            'course',
            'gender',
            'email',
            'phone',
            'photo',
            'created_at',
        ]

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = [
            'id',
            'mentor_number',
            'last_name',
            'first_name',
            'middle_initial',
            'department',
            'expertise',
            'email',
            'phone',
            'photo',
            'created_at',
        ]

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = [
            'id',
            'admin_number',
            'last_name',
            'first_name',
            'email',
            'created_at',
        ]

class SessionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source='student.last_name',
        read_only=True
    )
    mentor_name = serializers.CharField(
        source='mentor.last_name',
        read_only=True
    )

    class Meta:
        model = Session
        fields = [
            'id',
            'student',
            'student_name',
            'mentor',
            'mentor_name',
            'session_date',
            'start_time',
            'end_time',
            'created_at',
        ]