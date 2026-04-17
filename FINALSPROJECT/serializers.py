from rest_framework import serializers
from .models import (
    Student, Mentor, Admin, Session,
    Expertise, MentorAvailability, StudentPreference
)


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ['id', 'name']


class StudentPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPreference
        fields = [
            'id',
            'student',
            'preferred_department',
            'preferred_expertise',
            'preferred_gender',
            'availability_notes',
        ]


class StudentSerializer(serializers.ModelSerializer):
    preferences = StudentPreferenceSerializer(
        source='studentpreference',
        read_only=True
    )

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
            'preferences',
        ]


class MentorSerializer(serializers.ModelSerializer):
    expertise = ExpertiseSerializer(many=True, read_only=True)

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


class MentorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorAvailability
        fields = [
            'id',
            'mentor',
            'day_of_week',
            'start_time',
            'end_time',
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
        source='student.__str__',
        read_only=True
    )
    mentor_name = serializers.CharField(
        source='mentor.__str__',
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