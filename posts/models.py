from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

def upload_location(instance, filename):
	return "photos_articles/%s/%s/%s" %(instance.categorie, instance.slug, filename)

class Post(models.Model):
	title = models.CharField(max_length=200,  verbose_name="Titre")
	slug = models.SlugField(max_length=200)
	content = RichTextField(verbose_name="Contenu")
	image = models.ImageField(upload_to=upload_location)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	categorie = models.ForeignKey('categorie.Categorie', on_delete=models.CASCADE,  verbose_name="Catégorie de rattachement")
	sous_categorie = models.ForeignKey('categorie.SubCategorie', on_delete=models.CASCADE, verbose_name="Sous-Catégorie de rattachement")
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
		verbose_name = 'Billet'
		verbose_name_plural = 'Billets'

class Comments(models.Model):
	nom = models.CharField(max_length=100, verbose_name="Pseudo")
	message = models.TextField(verbose_name="Message")
	email = models.EmailField(verbose_name="Adresse Email")
	valide = models.BooleanField(default=True, verbose_name="Autorisé")
	post_rattachement = models.ForeignKey('posts.Post', on_delete=models.CASCADE, null=True, verbose_name="Billet de rattachement")
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ["-timestamp"]
		verbose_name = 'Commentairee'
		verbose_name_plural = 'Commentaires'