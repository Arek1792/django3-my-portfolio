from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True) #optional

	def __str__(self):
		return self.title

class Skill(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')

	def __str__(self):
		return self.title

class Language(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')

	def __str__(self):
		return self.title

class Interest(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portfolio/images/')

	def __str__(self):
		return self.title
