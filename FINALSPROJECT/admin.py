from django.contrib import admin
from .models import (
    Student,
    Mentor,
    Admin,
    Session,
    Expertise,
    MentorAvailability,
    StudentPreference
)

# =========================
# STUDENT PREFERENCE INLINE
# =========================
class StudentPreferenceInline(admin.StackedInline):
    model = StudentPreference
    extra = 0


# =========================
# STUDENT ADMIN
# =========================
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

    inlines = [StudentPreferenceInline]


# =========================
# EXPERTISE ADMIN
# =========================
@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


# =========================
# MENTOR ADMIN
# =========================
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'mentor_number',
        'last_name',
        'first_name',
        'department',
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

    filter_horizontal = ('expertise',)


# =========================
# MENTOR AVAILABILITY ADMIN
# =========================
@admin.register(MentorAvailability)
class MentorAvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'mentor',
        'day_of_week',
        'start_time',
        'end_time',
    )

    list_filter = ('day_of_week',)
    search_fields = ('mentor__last_name',)


# =========================
# STUDENT PREFERENCE ADMIN
# =========================
@admin.register(StudentPreference)
class StudentPreferenceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'student',
        'preferred_department',
        'preferred_expertise',
        'preferred_gender',
    )

    search_fields = (
        'student__last_name',
        'preferred_expertise',
    )

    list_filter = (
        'preferred_department',
        'preferred_gender',
    )


# =========================
# ADMIN
# =========================
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


# =========================
# SESSION
# =========================
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