from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

dept_drop = (
    ('CHOOSE', 'CHOOSE'),
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('EEE', 'EEE'),
    ('ECE', 'ECE'),
    ('EIE', 'EIE'),
    ('ETE', 'ETE'),
    ('MECH', 'MECH'),
    ('AUTO', 'AUTO'),
    ('CIVIL', 'CIVIL'),
)
year_drop = (
    ('choose', 'CHOOSE'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
)

semester_drop = (
    ('choose', 'CHOOSE'),
    ('1', 'I'),
    ('2', 'II'),
    ('3', 'III'),
    ('4', 'IV'),
    ('5', 'V'),
    ('6', 'VI'),
    ('7', 'VII'),
    ('8', 'VIII')
)

designationdrop = (
    ('student', 'student'),
    ('faculty', 'faculty')
)


class StudentsFeedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=150, choices=dept_drop, default='choose')
    year = models.CharField(max_length=150, choices=year_drop, default='choose')
    semester = models.CharField(max_length=150, choices=semester_drop, default='choose')
    staffName = models.CharField(max_length=150)
    feedback = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username +" "+ self.department +" "+ self.year


class FacultyFeedback(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=150, choices=dept_drop, default='choose')
    year = models.CharField(max_length=150, choices=year_drop, default='choose')
    semester = models.CharField(max_length=150, choices=semester_drop, default='choose')
    feedback = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.username +" "+ self.department+" "+self.year
