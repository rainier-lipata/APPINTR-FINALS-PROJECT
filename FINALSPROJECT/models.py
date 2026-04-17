from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    student_number = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=10, blank=True, null=True)

    college = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    course = models.CharField(max_length=150)

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='students/', blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_number} - {self.last_name}, {self.first_name}"


class Expertise(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    mentor_number = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=10, blank=True, null=True)

    department = models.CharField(max_length=150)
    expertise = models.ManyToManyField(Expertise)

    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='mentors/', blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mentor_number} - {self.last_name}, {self.first_name}"

class MentorAvailability(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.mentor} - {self.day_of_week}"

class StudentPreference(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    preferred_department = models.CharField(max_length=150, blank=True, null=True)
    preferred_expertise = models.CharField(max_length=150, blank=True, null=True)

    # Optional filters
    preferred_gender = models.CharField(
        max_length=10,
        choices=Student.GENDER_CHOICES,
        blank=True,
        null=True
    )

    availability_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Preferences of {self.student}"


class Admin(models.Model):
    admin_number = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.admin_number} - {self.last_name}, {self.first_name}"



class Session(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} with {self.mentor} on {self.session_date}"