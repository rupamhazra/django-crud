from django.db import models
from student.models import Student
from datetime import datetime,timedelta

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.PositiveIntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
      return str(self.name) + " ["+str(self.isbn)+']'
    class Meta:
      db_table = 'books'

def expiry():
    return datetime.today() + timedelta(days=15)
class Issue(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.CharField(max_length=13)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)
    class Meta:
          db_table='issue'


