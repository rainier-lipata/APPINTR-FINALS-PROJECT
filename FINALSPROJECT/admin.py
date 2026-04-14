from django.contrib import admin
from .models import Role, Status, Student, Mentor, Admin, Session



@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name')
    search_fields = ('role_name',)



@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
    search_fields = ('status_name',)



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
        'role',
        'status',
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
        'role',
        'status'
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
        'role',
        'status',
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
        'role',
        'status'
    )



@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'admin_number',
        'last_name',
        'first_name',
        'email',
        'role',
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
        'status',
        'created_at',
    )

    search_fields = (
        'student__last_name',
        'mentor__last_name',
    )

    list_filter = (
        'session_date',
        'status',
    )