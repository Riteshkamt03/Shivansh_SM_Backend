from django.contrib import admin
from .models import User, Course, Enrollment

class UserAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin interface
    list_display = ('email', 'name', 'date_of_birth', 'phone_number', 'is_active', 'is_staff')
    search_fields = ('email', 'name')
    list_filter = ('is_active', 'is_staff')

class CourseAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin interface
    list_display = ('title', 'description')
    search_fields = ('title',)
    
class EnrollmentAdmin(admin.ModelAdmin):
    # Define which fields to display in the admin interface
    list_display = ('user', 'course', 'enrollment_date')
    search_fields = ('user__email', 'course__title')
    list_filter = ('enrollment_date',)

# Register the models with the admin site
admin.site.register(User, UserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
