from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    subject = models.CharField(max_length=200)

    # def __str__(self):
    #     return f"{self.name} {self.age}{self.subject}"
