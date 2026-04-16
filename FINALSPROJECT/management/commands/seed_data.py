from django.core.management.base import BaseCommand
from FINALSPROJECT.models import Student, Mentor, Admin, Session


class Command(BaseCommand):
    help = "Insert dummy data"

    def handle(self, *args, **kwargs):

        # ---------- STUDENTS ----------
        student_list = [
            {
                "student_number": "2026-0001",
                "last_name": "Dela Cruz",
                "first_name": "Juan",
                "middle_initial": "S",
                "college": "CCS",
                "department": "IS",
                "course": "BSIS",
                "gender": "Male",
                "email": "juan@example.com",
                "phone": "09170000001",
            },
        ]

        students = []
        for s in student_list:
            obj, _ = Student.objects.get_or_create(
                student_number=s["student_number"],
                defaults=s
            )
            students.append(obj)

        self.stdout.write(self.style.SUCCESS("Students inserted"))


        # ---------- MENTORS ----------
        mentor_list = [
            {
                "mentor_number": "M-0001",
                "last_name": "Santos",
                "first_name": "Maria",
                "middle_initial": "L",
                "department": "IT",
                "expertise": "Web Development",
                "email": "maria@example.com",
                "phone": "09980000001",
            },
        ]

        mentors = []
        for m in mentor_list:
            obj, _ = Mentor.objects.get_or_create(
                mentor_number=m["mentor_number"],
                defaults=m
            )
            mentors.append(obj)

        self.stdout.write(self.style.SUCCESS("Mentors inserted"))


        # ---------- ADMIN ----------
        Admin.objects.get_or_create(
            admin_number="ADM-0001",
            defaults={
                "last_name": "Admin",
                "first_name": "System",
                "email": "admin@example.com",
            }
        )

        self.stdout.write(self.style.SUCCESS("Admin inserted"))


        # ---------- SESSION ----------
        if students and mentors:
            Session.objects.get_or_create(
                student=students[0],
                mentor=mentors[0],
                session_date="2026-05-01",
                defaults={
                    "start_time": "09:00",
                    "end_time": "10:00",
                }
            )

        self.stdout.write(self.style.SUCCESS("Session inserted"))
        self.stdout.write(self.style.SUCCESS("ALL DATA SEEDED SUCCESSFULLY"))