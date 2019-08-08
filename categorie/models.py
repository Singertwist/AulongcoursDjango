from __future__ import unicode_literals

from django.db import models

def upload_location(instance, filename):
	return "photos_categories/%s/%s/%s" %(instance.categorie, instance.nom_subcategorie, filename)

# Create your models here.
class Categorie(models.Model):
	nom_categorie = models.CharField(max_length= 255)

	def __unicode__(self):
		return self.nom_categorie

	def __str__(self):
		return self.nom_categorie

	class Meta:
		ordering = ["nom_categorie"]			

class SubCategorie(models.Model):
	nom_subcategorie = models.CharField(max_length= 255)
	slug = models.SlugField(max_length=200)
	categorie = models.ForeignKey('categorie.Categorie', on_delete=models.CASCADE)
	image = models.ImageField(upload_to=upload_location)

	def __unicode__(self):
		return self.nom_subcategorie

	def __str__(self):
		return self.nom_subcategorie

	class Meta:
		ordering = ["nom_subcategorie"]			