from django.conf.urls import url
from django.urls import path
from posts import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'article/<str:slug>-<int:id>',  views.article, name='article'),
    path(r'portfolio/<str:slug>-<int:article>',  views.portfolio, name='portfolio'),
    path(r'contact/', views.contact, name='contact'),
    path(r'categories/<str:slug>-<int:id>', views.souscategorie_display, name='souscategorie_display'),
    path(r'categories/', views.categorie_display, name='categorie_display'),
    path(r'a-propos/', views.apropos, name='apropos'),
]
