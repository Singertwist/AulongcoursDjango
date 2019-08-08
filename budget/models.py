from django.db import models

class Budget(models.Model):
    TRANSPORT = 'TRANSPORT'
    HÉBERGEMENTS = 'HÉBERGEMENTS'
    RESTAURATION = 'RESTAURATION'
    VISITES = 'VISITES'
    SANTÉ = 'SANTÉ'
    AUTRES = 'AUTRES'
    CATEGORIE_DEPENSES_CHOICES = (
        (TRANSPORT, 'Transport'),
        (HÉBERGEMENTS, 'Hébergements'),
        (RESTAURATION, 'Restauration'),
        (VISITES, 'Visites'),
        (SANTÉ, 'Santé'),
        (AUTRES, 'Autres'),
    )
    catégorie_dépenses = models.CharField(max_length=255,
        choices=CATEGORIE_DEPENSES_CHOICES,
        )
    nom_de_la_dépense = models.CharField(max_length=255)
    montant_de_la_dépense = models.DecimalField(max_digits=19, decimal_places=10)
    categoriebudget = models.ForeignKey('Categoriebudget', on_delete=models.CASCADE)

class Categoriebudget(models.Model):
	title = models.CharField(max_length=100)
	article = models.OneToOneField('posts.Post', on_delete=models.CASCADE)

	def __str__(self):
		return self.title
