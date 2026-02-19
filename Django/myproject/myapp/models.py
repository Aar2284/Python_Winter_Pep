from django.db import models

# Create your models here.

class Student(models.Model):
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science and Engineering'),
        ('ECE', 'Electronics and Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    