from django.db import models
from student.models import student

# Create your models here.
class Books(models.Model):
  book_name= models.CharField(max_length=255)
  book_publisher= models.CharField(max_length=255)
  book_publish_date=models.DateField(max_length=255)
  class Meta:
        db_table = 'books'


class Issue(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE,related_name='book',blank=True,null=True)
    issue_date = models.DateField()
    student = models.ForeignKey(student, on_delete=models.CASCADE,related_name='student',blank=True,null=True)
    class Meta:
          db_table='issue'


