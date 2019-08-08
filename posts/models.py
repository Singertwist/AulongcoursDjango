from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

def upload_location(instance, filename):
	return "photos_articles/%s/%s/%s" %(instance.categorie, instance.slug, filename)

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200)
	content = RichTextField()
	image = models.ImageField(upload_to=upload_location)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	categorie = models.ForeignKey('categorie.Categorie', on_delete=models.CASCADE)
	pays = models.ForeignKey('categorie.SubCategorie', on_delete=models.CASCADE)
	publier = models.BooleanField()

	@property
	def formatted_markdown(self):
		return markdownify(self.content)
	
	def __unicode__(self):
		return self.title

	def __str__(self):
			return self.title
			
	class Meta:
		ordering = ["-timestamp"]
