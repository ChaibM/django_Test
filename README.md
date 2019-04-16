# Creation d'une application par la commande 
python manage.py startapp pages

$tree pages
admin.py : Fichier de configuration de l'application intégrée Django Admin
apps.py  : Fichier de configuration pour l'application
migrations :garde la trace de toutes les modifications apportées à notre modèles.py
   └── __init__.py
models.py: la définition du modèles de base de données, que Django traduit automatiquement en tables de base de données
tests.py : Concernant le test de l'application
views.py : les pages de l'application

2)ajouter la ligne suivant dans le fichier {{helloworld_project/settings.py}}
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig', # nouveau ligne à ajouter qui permet a django de connaitre notre application déja creer {{pages}}
]
 
3)dans le fichier {{pages/views.py}} ajouter le code suivant qui permet d'importer la classe HttpResponse et d'afficher un message 
lord d'appel de la fonction {{homePageView}}
============================================
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse('Hello, World!')
    
=============================================

4) dans le fichier {{pages/urls.py}} ajouter le code suivant qui permet d'importer la classe path et le la view homePageView 
en utilisant urlpatterns 
=============================================
from django.urls import path

from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]

=============================================
5) dans le fichier {{helloworld_project/urls.py}} ajouter le code suivant qui permet d'importer path et include et définit 
le fichier url de notre application
=============================================
from django.contrib import admin
from django.urls import path, include # Nouveau 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')), # Nouveau
]
=============================================

6) lancer la commande suivant {{python manage.py runserver}}
et visiter http://127.0.0.1:8000
