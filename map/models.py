from django.db import models

# Create your models here.
from django.db import models
from geoposition.fields import GeopositionField

class Map(models.Model):
    nom = models.CharField(max_length=100)
    adresse_complète = models.CharField(blank=True, max_length=255)
    commentaire_adresse = models.CharField(blank=True, max_length=255)
    etape = models.IntegerField()
    position = GeopositionField()
    categoriemap = models.ForeignKey('Categoriemap', on_delete=models.CASCADE)


class Categoriemap(models.Model):
	title = models.CharField(max_length=100)
	article = models.OneToOneField('posts.Post', on_delete=models.CASCADE)

	def __str__(self):
		return self.title