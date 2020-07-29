from django.db import models

# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Subjects(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    d_o_b = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class SubjectStudentMap(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        student = f"{self.student.first_name} {self.student.last_name}"
        subject = self.subject.name
        return f"{subject} - {student}"
    