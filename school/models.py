from django.db import models
from djmoney.models.fields import MoneyField
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class CourseCategory(models.Model):
    # Детям, софтскиллся, 1-4 класс
    category_name = models.CharField(max_length=150)
    category_description = models.CharField(max_length=34, default='Нужные навыки для школы подготовка')
    
    def __str__(self):
        return self.category_name

class CourseSubcategory(models.Model):
    # Подготовка к вуз, Подготовка к ЕНТ, подготовка к Айлтс
    subcategory_name = models.CharField(max_length=150)
    course_category = models.ForeignKey(to=CourseCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subcategory_name
    
class CourseType(models.Model):
    # online, offline, gibrid 
    type_name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.type_name
    

class CourseGrade(models.Model):
    # 1 Grade, 2 Grade etc.
    grade = models.IntegerField()
    
    def __str__(self):
        return self.grade
    
class Course(models.Model):
    course_name = models.CharField(max_length=150)
    course_description = RichTextField(null=True, blank=True, default='')
    course_content = RichTextField(null=False, blank=False, default='')
    course_main_image = models.ImageField(upload_to='course_images/main_images/', blank=True)
    course_sub_image = models.ImageField(upload_to='course_images/sub_images/', blank=True)
    course_slug = models.SlugField(default='', null=False)

    ''
    course_subcategory = models.ForeignKey(to='school.CourseSubcategory', on_delete=models.CASCADE, null=True, blank=True)
    course_type = models.ForeignKey(to='school.CourseType', on_delete=models.CASCADE, null=True, blank=True)
    course_grade = models.CharField(choices={'1': '1 Класс', '2' : '2 Класс' , '3' : '3 Класс', '4' : '4 Класс', '5' : '5 Класс', '6' : '6 Класс', '7' : '7 Класс', '8' : '8 Класс', '9' : '9 Класс', '10' : '10 Класс', '11' : '11 Класс', '12' : '12 Класс'}, max_length=33, default='1', null=True)
    # course_reviews
    course_language = models.CharField( choices={'KZ' : 'Казахский', 'RU' : 'Русский', 'EN' : 'English'}, max_length=33, default='KZ')
    course_duration = models.DurationField(null=True, default='01:00:00')
    
    # course_available_week_days
    # course_teachers
    # course_schedule
    
    
    # course 
    course_price = MoneyField(max_digits=14, decimal_places=2, null=True, default_currency='KZT')
    
    def save(self, *args, **kwargs):
        if not self.id and not self.course_slug:
            self.course_slug = slugify(self.course_name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.course_name
        

class BannerImages(models.Model):
    image = models.ImageField(upload_to='banner/images/')
    redirect_to = models.URLField()

class Banner(models.Model):
    banner_name = models.CharField(max_length=150)
    images = models.ManyToManyField(to=BannerImages)
    banner_title = models.CharField(max_length=255)
    banner_content = RichTextField()
    
    button_title = models.CharField(max_length=100)
    button_url = models.URLField()
    
