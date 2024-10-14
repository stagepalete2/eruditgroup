from django.http import JsonResponse
from django.db.models import Q
from users.models import User
from eruditplatform.models import GroupCourse, TimeTable

def get_free_teachers(request):
    if request.method == 'POST':
        days = list(request.POST.getlist('days[]'))
        course = request.POST.get('course')

        # Get all group courses for the specific course
        group_courses = GroupCourse.objects.filter(course=course)

        # Get all teachers associated with the course
        teachers = User.objects.filter(id__in=group_courses.values_list('teacher', flat=True))

        # Get all timetables for the specified days
        timetables = TimeTable.objects.filter(days_of_the_week__in=days)

        free_time_tables = []

        # Loop through all teachers
        for teacher in teachers:
            # Get all courses and their timetables for this teacher
            teacher_courses = group_courses.filter(teacher=teacher)
            
            # Aggregate all timetables the teacher is occupied with
            occupied_times = TimeTable.objects.filter(groupcourse__in=teacher_courses.values_list('id', flat=True))


            # Find free time slots by excluding the teacher's occupied time slots
            free_times = timetables.exclude(id__in=occupied_times.values_list('id', flat=True))

            # If the teacher has free slots, add them to the result
            if free_times.exists():
                for free_time in free_times:
                    free_time_tables.append({
                        'teacher': teacher.username,  # Use username or another field from User model
                        'day': free_time.days_of_the_week,
                        'time': free_time.hours_of_the_week
                    })

        # Return the result as JSON
        return JsonResponse(data={'free_teachers_by_day': free_time_tables}, safe=False)

    # Return error for non-POST requests
    return JsonResponse(data={'error': 'Only POST requests are allowed'}, status=400)

