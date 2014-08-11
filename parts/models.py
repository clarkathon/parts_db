from django.db import models

# Create your models here.


class Part(models.Model):
	part_number = models.CharField(max_length=50)
	package = models.CharField(max_length=25)
	desciption = models.CharField(max_length=200)
	cost = models.FloatField()
	quantity = models.IntegerField(default=0)
	projects = models.ManyToManyField(Project)

class Project(models.Model):
	worker = models.ManyToManyField(Workers)
	name = models.CharField(max_length=50)
	client = models.CharField(max_length=75)
	board = models.ManyToManyField(Boards)
	bom = models.ManyToManyField(Bom)

class Boards(models.Model):
	name = models.CharField(max_length=50)
	schematic = #need to file entry for this.
	board = #file entry on this as well.  
	rev = models.FloatField()

class Bom(models.Model):
	name = models.CharField(max_length=50)
	cost = models.FloatField()
	qty = models.IntegerField(default=0)
	#need to enter a spot in for bom files to be uploaded per section

class Workers(models.Model):
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	role = models.CharField(max_length=25)
	access = models.CharField(max_length=10)


	def __unicode__(self):
		return self.part_number




	
