from rest_framework import serializers
from .models import Role, Status, Student, Mentor, Admin, Session

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    status_name = serializers.CharField(source='status.status_name', read_only=True)

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
            'role',
            'role_name',
            'status',
            'status_name',
            'created_at',
        ]

class MentorSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    status_name = serializers.CharField(source='status.status_name', read_only=True)

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
            'role',
            'role_name',
            'status',
            'status_name',
            'created_at',
        ]

class AdminSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)

    class Meta:
        model = Admin
        fields = [
            'id',
            'admin_number',
            'last_name',
            'first_name',
            'email',
            'role',
            'role_name',
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
    status_name = serializers.CharField(
        source='status.status_name',
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
            'status',
            'status_name',
            'created_at',
        ]