from django.contrib import admin

from .models import General_University,General_University_requirement,Medical_College,Science_And_Technology
from .models import Engineering_University,Science_And_Technology_requirement


# Register your models here.
#class General_UniversityAdmin(admin.ModelAdmin):

#    fields=['uid','uName''']




admin.site.register(General_University)
admin.site.register(General_University_requirement)
admin.site.register(Medical_College)
admin.site.register(Science_And_Technology)
admin.site.register(Science_And_Technology_requirement)
admin.site.register(Engineering_University)
