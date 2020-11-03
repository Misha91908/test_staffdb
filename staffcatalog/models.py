from django.db import models

# Create your models here.

from django.urls import reverse


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    job_assign = models.DateField()
    job_end = models.DateField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    ans = 42

    def get_absolute_url(self):
        return reverse('person', args=[str(self.id)])

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic


class Alphabet(models.Model):
    id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=False)

    def get_last_name_first_letter(self):
        return self.objects.get(last_name=self.last_name)

    def get_absolute_url(self):
        return reverse('alphabet', kwargs={'last_name': str(self.last_name)})

    def __str__(self):
        return self.last_name
