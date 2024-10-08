from django.contrib import admin

# Register your models here.
from .models import News, HotLink, Groups, GroupCourse, TimeTable, GroupAttendance, GroupGrade, AssignmentAttachments, GroupAssignment, GroupLesson
from .admin_models import NewsAdmin

admin.site.register(News, NewsAdmin)
admin.site.register(HotLink)
admin.site.register(Groups)
admin.site.register(GroupCourse)
admin.site.register(TimeTable)
admin.site.register(GroupAttendance)
admin.site.register(GroupGrade)
admin.site.register(AssignmentAttachments)
admin.site.register(GroupAssignment)
admin.site.register(GroupLesson)