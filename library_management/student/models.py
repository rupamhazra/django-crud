from django.db import models

class student(models.Model):
  reg_no= models.IntegerField(max_length=255)
  course= models.CharField(max_length=255)
  name=models.CharField(max_length=255)

class Meta:
        db_table = 'students'