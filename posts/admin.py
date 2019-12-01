from django.contrib import admin

# Register your models here.

from posts.models  import Post, Comments
from categorie.models import Categorie, SubCategorie
from portfolio.models import Portfolio, Categorieport
from map.models import Map, Categoriemap
#from categorieportfolio.models import Categorieportfolio

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "categorie", "timestamp", "publier"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content", "publier"]
	prepopulated_fields = {'slug': ('title', ), }

	class Meta:
		model = Post

class CommentsModelAdmin(admin.ModelAdmin):
	list_display = ["nom", "message", "email", "valide", "post_rattachement", "timestamp"]
	list_filter = ["post_rattachement"]

	class Meta:
		model = Comments

class PortfolioInline(admin.TabularInline):
	#list_display = ["title", "updated", "timestamp"]
	#list_filter = ["updated", "timestamp"]
	#search_fields = ["title"]
	model = Portfolio

class CategorieportAdmin(admin.ModelAdmin):
	inlines = [
		PortfolioInline,
	]

class SubCategorieModelAdmin(admin.ModelAdmin):
	list_display = ["nom_subcategorie", "categorie", "is_active"]
	list_editable = ('is_active', )
	prepopulated_fields = {'slug': ('nom_subcategorie', ), }

class MapInline(admin.TabularInline):
	list_display = ["nom", "position"]
	model = Map

class CategoriemapAdmin(admin.ModelAdmin):
	inlines = [
		MapInline,
	]

class MapModelAdmin(admin.ModelAdmin):
	list_display = ["nom", "position"]

#admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Categorie)
admin.site.register(SubCategorie, SubCategorieModelAdmin)
admin.site.register(Categorieport, CategorieportAdmin)
admin.site.register(Categoriemap, CategoriemapAdmin)
admin.site.register(Comments, CommentsModelAdmin)

#admin.site.register(Portfolio)
