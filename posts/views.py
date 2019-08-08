#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from .models import Post
from portfolio.models import Portfolio, Categorieport
from categorie.models import Categorie, SubCategorie
from map.models import Categoriemap, Map
from budget.models import Categoriebudget, Budget
#from categorieportfolio.models import Categorieportfolio
from .forms import ContactForm

def home(request):
    articles_list = Post.objects.filter(publier = 1) # Permet de montrer que les articles pas en brouillon
    paginator = Paginator(articles_list, 10) # Permet de modifier le nombre d'articles affiché par page

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'tous_articles': articles})

def article(request, article=None, slug=None, id=None):
    afficher = get_object_or_404(Post, slug=slug, id=id)
    try :
        portfolio = afficher.categorieport
    except ObjectDoesNotExist:
        portfolio = None

    try : 
        map = afficher.categoriemap
    except ObjectDoesNotExist:
        map = None

    try : 
        budget = afficher.categoriebudget
    except ObjectDoesNotExist:
        budget = None

    return render(request, 'article.html', {'afficher': afficher, 'portfolio': portfolio, 'map': map, 'budget': budget})

def portfolio(request, slug=None, article=None):
    slug = get_object_or_404(Post, slug=slug)
    portfolio = get_object_or_404(Categorieport, article=article)
    image_portfolio = portfolio.portfolio_set.all()

    try :
        map = slug.categoriemap
    except ObjectDoesNotExist:
        map = None

    try : 
        budget = slug.categoriebudget
    except ObjectDoesNotExist:
        budget = None

    paginator = Paginator(image_portfolio, 10)

    page = request.GET.get('page')
    try:
        image_portfolio = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        image_portfolio = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        image_portfolio = paginator.page(paginator.num_pages)
        
    return render(request, 'portfolio.html', {'portfolio': portfolio, 'image_portfolio': image_portfolio, 'slug': slug, 'map': map, 'budget':budget})

def map(request, slug=None, article=None):
    slug = get_object_or_404(Post, slug=slug)
    map = get_object_or_404(Categoriemap, article=article)
    coordonnees_map = map.map_set.all()

    try :
        portfolio = slug.categorieport
    except ObjectDoesNotExist:
        portfolio = None

    try : 
        budget = slug.categoriebudget
    except ObjectDoesNotExist:
        budget = None

    return render(request, 'map.html', {'map': map, 'coordonnees_map': coordonnees_map, 'portfolio': portfolio, 'budget':budget})

def budget(request, slug=None, article=None):
    slug = get_object_or_404(Post, slug=slug)
    budget = get_object_or_404(Categoriebudget, article=article)
    chiffres_budget = budget.budget_set.all()

    try :
        portfolio = slug.categorieport
    except ObjectDoesNotExist:
        portfolio = None

    try :
        map = slug.categoriemap
    except ObjectDoesNotExist:
        map = None

    return render(request, 'budget.html', {'budget': budget, 'chiffres_budget': chiffres_budget, 'portfolio': portfolio, 'map': map})

def categorie_display(request, categorie=None):
    categorie = Categorie.objects.all()
    return render(request, 'categorie.html', {'categorie': categorie})

def souscategorie_display(request, id=None, categorie=None, slug=None):
    souscategorie = get_object_or_404(SubCategorie, id=id)
    articles_list = Post.objects.filter(pays=souscategorie)
    paginator = Paginator(articles_list, 10)

    page = request.GET.get('page')
    try:
        article_souscategorie = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        article_souscategorie = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        article_souscategorie = paginator.page(paginator.num_pages)

    return render(request, 'souscategorie.html', {'souscategorie': souscategorie, 'article_souscategorie': article_souscategorie})

def apropos(request):
    return render(request,'a-propos.html')

def contact(request):
    # Construire le formulaire, soit avec les données postées,
    # soit vide si l'utilisateur accède pour la première fois
    # à la page.
    form = ContactForm(request.POST or None)
    # Nous vérifions que les données envoyées sont valides
    # Cette méthode renvoie False s'il n'y a pas de données 
    # dans le formulaire ou qu'il contient des erreurs.
    if form.is_valid(): 
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        # Nous pourrions ici envoyer l'e-mail grâce aux données 
        # que nous venons de récupérer
        template = get_template('contact_template.txt')
        context = Context({
                'sujet': sujet,
                'envoyeur': envoyeur,
                'message': message,
            })
        content = template.render(context)

        email = EmailMessage(
        "New contact form submission",
        content,
        "Your website" +'',
        ['youremail@gmail.com'],
        headers = {'Reply-To': envoyeur })

        email.send()
        envoi = True
        form = ContactForm()
    # Quoiqu'il arrive, on affiche la page du formulaire.
    return render(request, 'contact.html', locals())

