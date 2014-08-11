from django.db import models

# Create your models here.


class Part(models.Model):
	part_number = models.CharField(max_length=50)
	package = models.CharField(max_length=25)
	desciption = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	projects = models.CharField(max_length=100)

	def __unicode__(self):
		return self.part_number




	
