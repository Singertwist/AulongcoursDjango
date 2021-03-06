# Generated by Django 2.2.7 on 2019-12-01 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0002_auto_20191201_1155'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ['nom_categorie'], 'verbose_name': 'Catégorie Générale', 'verbose_name_plural': 'Catégories Générales'},
        ),
        migrations.AlterModelOptions(
            name='subcategorie',
            options={'ordering': ['nom_subcategorie'], 'verbose_name': 'Sous-Catégorie', 'verbose_name_plural': 'Sous-Catégories'},
        ),
        migrations.AlterField(
            model_name='categorie',
            name='nom_categorie',
            field=models.CharField(max_length=255, verbose_name='Nom de la catégorie'),
        ),
        migrations.AlterField(
            model_name='subcategorie',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorie.Categorie', verbose_name='Catégorie de rattachement'),
        ),
        migrations.AlterField(
            model_name='subcategorie',
            name='nom_subcategorie',
            field=models.CharField(max_length=255, verbose_name='Nom de la sous-catégorie'),
        ),
    ]
