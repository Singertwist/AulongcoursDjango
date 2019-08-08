from __future__ import unicode_literals

from django.db import models
from sorl.thumbnail import ImageField

def upload_location(instance, filename):
	return "photos_portfolio/%s/%s" %(instance.categorieportfolio, filename)

class Portfolio(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to=upload_location)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	categorieportfolio = models.ForeignKey('Categorieport', on_delete=models.CASCADE)


	def __unicode__(self):
		return self.title

	def __str__(self):
			return self.title
			
class Categorieport(models.Model):
	title = models.CharField(max_length=200)
	article = models.OneToOneField('posts.Post', on_delete=models.CASCADE)

	def __str__(self):
		return self.title