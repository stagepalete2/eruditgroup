from django.db import models

# Create your models here.
class Teacher(models.Model):
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
    course = models.ForeignKey(to='school.Course', on_delete=models.CASCADE)
    teacher_description = models.TextField()
    teacher_rating = models.IntegerField()