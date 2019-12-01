from __future__ import unicode_literals

from django.db import models

def upload_location(instance, filename):
	return "photos_categories/%s/%s/%s" %(instance.categorie, instance.nom_subcategorie, filename)

# Create your models here.
class Categorie(models.Model):
	nom_categorie = models.CharField(max_length= 255, verbose_name="Nom de la catégorie")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_active = models.BooleanField(verbose_name="Catégorie active")

	def __unicode__(self):
		return self.nom_categorie

	def __str__(self):
		return self.nom_categorie

	class Meta:
		ordering = ["nom_categorie"]
		verbose_name = 'Catégorie Générale'
		verbose_name_plural = 'Catégories Générales'		

class SubCategorie(models.Model):
	nom_subcategorie = models.CharField(max_length= 255,  verbose_name="Nom de la sous-catégorie")
	slug = models.SlugField(max_length=200)
	categorie = models.ForeignKey('categorie.Categorie', on_delete=models.CASCADE,  verbose_name="Catégorie de rattachement")
	image = models.ImageField(upload_to=upload_location)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	is_active = models.BooleanField(verbose_name="Sous-Catégorie active")

	def __unicode__(self):
		return self.nom_subcategorie

	def __str__(self):
		return self.nom_subcategorie

	class Meta:
		ordering = ["nom_subcategorie"]
		verbose_name = 'Sous-Catégorie'
		verbose_name_plural = 'Sous-Catégories'		