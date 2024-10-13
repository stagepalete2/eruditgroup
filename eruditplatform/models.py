from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.utils import timezone
# Create your models here.

class News(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    
    published = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)
    
    news_slug = models.SlugField(default='', null=False)
    tags = TaggableManager()
    
    def save(self, *args, **kwargs):
        if not self.id and not self.news_slug:
            self.news_slug = slugify(self.news_slug)
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.title
    
    
class HotLink(models.Model):
    new = models.ForeignKey('eruditplatform.News', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.new.title
    
class Groups(models.Model):
    group_name = models.CharField(max_length=50)
    group_participants = models.ManyToManyField(to='users.User', related_name='GroupParticipants')
    
    def __str__(self):
        return self.group_name
    
class TimeTable(models.Model):
    DAYS_OF_THE_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday')
    ]

    days_of_the_week = models.CharField(max_length=9, choices=DAYS_OF_THE_WEEK)
    hours_of_the_week = models.TimeField()

    def __str__(self):
        return f'{self.days_of_the_week} at {self.hours_of_the_week}'

class GroupCourse(models.Model):
    course = models.ForeignKey(to='school.Course', on_delete=models.CASCADE)
    group = models.ForeignKey(to='eruditplatform.Groups', on_delete=models.CASCADE)
    teacher = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    time_table = models.ManyToManyField(to='eruditplatform.TimeTable')
    group_attendence = models.ManyToManyField(to='eruditplatform.GroupAttendance', blank=True)
    group_grade = models.ManyToManyField(to='eruditplatform.AssignmentGrade', blank=True)
    group_lesson = models.ManyToManyField(to='eruditplatform.CourseLesson', blank=True)
    
    def __str__(self):
        return f'{self.course} for {self.group}'
    
class GroupAttendance(models.Model):
    ATTENDANCE_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]

    student = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    remark = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return f'{self.student} on {self.date} ({self.status})'
    
    
class AssignmentGrade(models.Model):
    student = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    assignment = models.ForeignKey(to='eruditplatform.CourseAssignment', on_delete=models.CASCADE)
    grade = models.IntegerField()
    grade_max = models.IntegerField(default=100)
    feedback = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.student}, {self.assignment} - {self.grade} ({self.feedback})' 
    

class AssignmentAttachments(models.Model):
    file = models.FileField(upload_to='attachments')

class AssignmentSubmissions(models.Model):
    file = models.FileField(upload_to='submissions')
    
class CourseAssignment(models.Model):
    assignment_name = models.CharField(max_length=255)
    assignment_detail = RichTextField()
    assignment_attachments = models.ManyToManyField(to='eruditplatform.AssignmentAttachments', blank=True)
    assignment_opened = models.DateTimeField()
    assignment_due = models.DateTimeField()
    assignemnt_note = models.CharField(max_length=50)
    assignment_lesson = models.ForeignKey(to='eruditplatform.CourseLesson', on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, blank=True)
    
    created_by = models.ForeignKey(to='users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.assignment_name}'

class CourseLesson(models.Model):
    lesson_title = models.CharField(max_length=50)
    lesson_detail = RichTextField()
    lesson_attachments = models.ManyToManyField(to='eruditplatform.AssignmentAttachments', blank=True) 
    lesson_datetime = models.DateTimeField()
    attendance = models.ManyToManyField(to='eruditplatform.GroupAttendance', blank=True)
    def __str__(self):
        return f'{self.lesson_title}'

