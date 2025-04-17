from django.contrib import admin
from student.models import Profile, Result
# Register your models here.

# admin.site.register(Profile)
# admin.site.register(Result)


#------------------Dispaly database data in admin-------------
#Method 1
'''class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city')

admin.site.register(Profile, ProfileAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class')

admin.site.register(Result, ResultAdmin)
'''

#Method 2
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city')
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class')
