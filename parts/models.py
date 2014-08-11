from django.db import models

# Create your models here.


class Part(models.Model):
	number = models.CharField(max_length=50)
	package = models.CharField(max_length=25)
	description = models.CharField(max_length=200)
	cost = models.FloatField()
	quantity = models.IntegerField(default=0)

	def __unicode__(self):
		return self.number


class Bom(models.Model):
	name = models.CharField(max_length=50)
	cost = models.FloatField()
	qty = models.IntegerField(default=0)
	#need to enter a spot in for bom files to be uploaded per section

	def __unicode__(self):
		return self.name


class Worker(models.Model):
	first = models.CharField(max_length=50)
	last = models.CharField(max_length=50)
	role = models.CharField(max_length=25)
	access = models.CharField(max_length=10)

	def __unicode__(self):
		return self.first + ' ' + self.last
	

class Project(models.Model):
	name = models.CharField(max_length=50)
	client = models.CharField(max_length=75)
	# parts = models.ManyToManyField(Part)
	# workers = models.ManyToManyField(Worker)

	def __unicode__(self):
		return self.name


class Board(models.Model):
	name = models.CharField(max_length=50)
	# schematic = models.FileField(upload_to='folder')
	# board = models.FileField(upload_to='folder')
	# rev = models.FloatField()
	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ('name',)
