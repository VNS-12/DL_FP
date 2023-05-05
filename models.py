from django.db import models


# Create your models here.
class onlineuser(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	zip=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);


class graph(models.Model):
	naive=models.FloatField()
	nn=models.FloatField()
	cnn=models.FloatField()
	svm=models.FloatField()
	dt=models.FloatField()

	
