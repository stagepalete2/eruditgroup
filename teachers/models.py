from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
# class Teacher(models.Model):
#     user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
#     course = models.ForeignKey(to='school.Course', on_delete=models.CASCADE)
#     teacher_description = RichTextField(null=True, blank=True)
#     teacher_rating = models.IntegerField(null=True, blank=True)
    
#     def __str__(self):
#         return f'{self.user.name} {self.user.lastname}'