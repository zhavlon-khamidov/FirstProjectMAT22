from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Group(models.Model):
    group_code = models.CharField(max_length=10)
    department = models.CharField(max_length=25)