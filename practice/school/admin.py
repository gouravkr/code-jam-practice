from django.contrib import admin

# Register your models here.
from .models import Subjects, Student, Teachers, SubjectStudentMap

admin.site.register(Subjects)
admin.site.register(Student)
admin.site.register(Teachers)
admin.site.register(SubjectStudentMap)

