from django.core.management.base import BaseCommand
from FINALSPROJECT.models import Role, Status, Student, Mentor, Admin, Session


class Command(BaseCommand):
    help = "Insert dummy data"

    def handle(self, *args, **kwargs):

        roles = ["Admin", "Mentor", "Student"]
        role_objs = {}

        for r in roles:
            obj, _ = Role.objects.get_or_create(role_name=r)
            role_objs[r] = obj

        self.stdout.write(self.style.SUCCESS("Roles inserted"))


        statuses = ["Active", "Inactive", "Completed"]
        status_objs = {}

        for s in statuses:
            obj, _ = Status.objects.get_or_create(status_name=s)
            status_objs[s] = obj

        self.stdout.write(self.style.SUCCESS("Status inserted"))


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
            {
                "student_number": "2026-0002",
                "last_name": "Reyes",
                "first_name": "Ana",
                "middle_initial": "M",
                "college": "CCS",
                "department": "IT",
                "course": "BSIT",
                "gender": "Female",
                "email": "ana@example.com",
                "phone": "09170000002",
            },
        ]

        students = []
        for s in student_list:
            obj, _ = Student.objects.get_or_create(
                student_number=s["student_number"],
                defaults={
                    **s,
                    "role": role_objs["Student"],
                    "status": status_objs["Active"],
                }
            )
            students.append(obj)

        self.stdout.write(self.style.SUCCESS("Students inserted"))


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
            {
                "mentor_number": "M-0002",
                "last_name": "Garcia",
                "first_name": "Pedro",
                "middle_initial": "T",
                "department": "CS",
                "expertise": "Data Science",
                "email": "pedro@example.com",
                "phone": "09980000002",
            },
        ]

        mentors = []
        for m in mentor_list:
            obj, _ = Mentor.objects.get_or_create(
                mentor_number=m["mentor_number"],
                defaults={
                    **m,
                    "role": role_objs["Mentor"],
                    "status": status_objs["Active"],
                }
            )
            mentors.append(obj)

        self.stdout.write(self.style.SUCCESS("Mentors inserted"))


        Admin.objects.get_or_create(
            admin_number="ADM-0001",
            defaults={
                "last_name": "Admin",
                "first_name": "System",
                "email": "admin@example.com",
                "role": role_objs["Admin"],
            }
        )

        self.stdout.write(self.style.SUCCESS("Admin inserted"))


        if students and mentors:
            Session.objects.get_or_create(
                student=students[0],
                mentor=mentors[0],
                session_date="2026-05-01",
                start_time="09:00",
                end_time="10:00",
                defaults={
                    "status": status_objs["Active"],
                }
            )

        self.stdout.write(self.style.SUCCESS("Session inserted"))


        self.stdout.write(self.style.SUCCESS("ALL DATA SEEDED SUCCESSFULLY"))