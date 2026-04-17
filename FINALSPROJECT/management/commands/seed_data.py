from django.core.management.base import BaseCommand
<<<<<<< HEAD
from datetime import date, time

from FINALSPROJECT.models import (
    Student,
    Mentor,
    Admin,
    Session,
    Expertise
)
=======
from FINALSPROJECT.models import Student, Mentor, Admin, Session
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3


class Command(BaseCommand):
    help = "Insert dummy data"

    def handle(self, *args, **kwargs):

<<<<<<< HEAD
        expertise_obj, _ = Expertise.objects.get_or_create(
            name="Web Development"
        )

        self.stdout.write(self.style.SUCCESS("Expertise inserted"))


=======
        # ---------- STUDENTS ----------
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
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


<<<<<<< HEAD
=======
        # ---------- MENTORS ----------
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
        mentor_list = [
            {
                "mentor_number": "M-0001",
                "last_name": "Santos",
                "first_name": "Maria",
                "middle_initial": "L",
                "department": "IT",
<<<<<<< HEAD
=======
                "expertise": "Web Development",
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
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
<<<<<<< HEAD

            obj.expertise.add(expertise_obj)

=======
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
            mentors.append(obj)

        self.stdout.write(self.style.SUCCESS("Mentors inserted"))


<<<<<<< HEAD
=======
        # ---------- ADMIN ----------
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
        Admin.objects.get_or_create(
            admin_number="ADM-0001",
            defaults={
                "last_name": "Admin",
                "first_name": "System",
                "email": "admin@example.com",
            }
        )

        self.stdout.write(self.style.SUCCESS("Admin inserted"))


<<<<<<< HEAD
=======
        # ---------- SESSION ----------
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
        if students and mentors:
            Session.objects.get_or_create(
                student=students[0],
                mentor=mentors[0],
<<<<<<< HEAD
                session_date=date(2026, 5, 1),
                defaults={
                    "start_time": time(9, 0),
                    "end_time": time(10, 0),
=======
                session_date="2026-05-01",
                defaults={
                    "start_time": "09:00",
                    "end_time": "10:00",
>>>>>>> 48a72de28a5aae4ac1c56b6a0e35961a47aefad3
                }
            )

        self.stdout.write(self.style.SUCCESS("Session inserted"))
        self.stdout.write(self.style.SUCCESS("ALL DATA SEEDED SUCCESSFULLY"))