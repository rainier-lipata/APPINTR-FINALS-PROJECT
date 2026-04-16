from django.contrib import admin
from .models import Student, Mentor, Admin, Session



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student_number',
        'last_name',
        'first_name',
        'college',
        'department',
        'course',
        'gender',
        'email',
        'created_at',
    )

    search_fields = (
        'student_number',
        'last_name',
        'first_name',
        'email',
    )

    list_filter = (
        'college',
        'department',
        'course',
        'gender',
    )



@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'mentor_number',
        'last_name',
        'first_name',
        'department',
        'expertise',
        'email',
        'created_at',
    )

    search_fields = (
        'mentor_number',
        'last_name',
        'first_name',
        'email',
    )

    list_filter = (
        'department',
        'expertise',
    )



@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'admin_number',
        'last_name',
        'first_name',
        'email',
        'created_at',
    )

    search_fields = (
        'admin_number',
        'last_name',
        'first_name',
        'email',
    )



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'mentor',
        'session_date',
        'start_time',
        'end_time',
        'created_at',
    )

    search_fields = (
        'student__last_name',
        'mentor__last_name',
    )

    list_filter = (
        'session_date',
    )