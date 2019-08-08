from django.conf.urls import url

# from .views import (
# 		home,
# 		article,
# 		contact,
# )

# urlpatterns = [
#     url(r'accueil/$', home),
#     url(r'article/(?P<slug>.+)-(?P<id>\d+)$', article),
#     url(r'contact/$', contact),
#     #url(r'^posts/$', <nom de l'application, ici posts>.view.<nom de la fonction dans la vue>,
# ]

from posts import views

urlpatterns = [
    url(r'^/?$', views.home, name='home'),
    url(r'article/(?P<slug>.+)-(?P<id>\d+)$',  views.article, name='article'),
    url(r'portfolio/(?P<slug>.+)-(?P<article>\d+)$',  views.portfolio, name='portfolio'),
    url(r'carte/(?P<slug>.+)-(?P<article>\d+)$',  views.map, name='map'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'categories/(?P<slug>.+)-(?P<id>\d+)$', views.souscategorie_display, name='souscategorie_display'),
    url(r'categories/$', views.categorie_display, name='categorie_display'),
    url(r'a-propos/$', views.apropos, name='apropos'),
    url(r'budget/(?P<slug>.+)-(?P<article>\d+)$', views.budget, name='budget'),
]
