from django.db import models

# Create your models here.
class CourseCategory(models.Model):
    category_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.category_name

class CourseSubcategory(models.Model):
    subcategory_name = models.CharField(max_length=150)
    course_category = models.ForeignKey(to=CourseCategory, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.subcategory_name
    
class CourseType(models.Model):
    # i.e. Express course, Fast Course, 
    type_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.type_name

class CourseGrade(models.Model):
    grade = models.IntegerField()
    
    def __str__(self):
        return self.grade
    
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_subcategory = models.ForeignKey(to=CourseSubcategory, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.course_name

class BannerImages(models.Model):
    image = models.ImageField(upload_to='banner/images/')
    redirect_to = models.URLField()

class Banner(models.Model):
    banner_name = models.CharField(max_length=150)
    images = models.ManyToManyField(to=BannerImages)
    
