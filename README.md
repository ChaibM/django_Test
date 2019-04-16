

1)Creation d'une application par la commande </br>

{{python manage.py startapp pages}}

$tree pages
admin.py : Fichier de configuration de l'application intégrée Django Admin</br>
apps.py  : Fichier de configuration pour l'application</br>
migrations :garde la trace de toutes les modifications apportées à notre modèles.py</br>
   └── __init__.py
models.py: la définition du modèles de base de données, que Django traduit automatiquement en tables de base de données</br>
tests.py : Concernant le test de l'application</br>
views.py : les pages de l'application</br>

2)ajouter la ligne suivant dans le fichier {{helloworld_project/settings.py}}</br>
INSTALLED_APPS = [</br>
    'django.contrib.admin',</br>
    'django.contrib.auth',</br>
    'django.contrib.contenttypes',</br>
    'django.contrib.sessions',</br>
    'django.contrib.messages',</br>
    'django.contrib.staticfiles',</br>
    'pages.apps.PagesConfig', # nouveau ligne à ajouter qui permet a django de connaitre notre application déja creer {{pages}}</br>
    ]</br>
   
3)dans le fichier {{pages/views.py}} ajouter le code suivant qui permet d'importer la classe HttpResponse et d'afficher un</br> message lors d'appel de la fonction {{homePageView}}</br>
</br>
</br>=====================================</br>
from django.http import HttpResponse

def homePageView(request):</br>
    return HttpResponse('Hello, World!')</br>
</br>=====================================</br>
4) dans le fichier {{pages/urls.py}} ajouter le code suivant qui permet d'importer la classe path et le la view </br> homePageView en utilisant urlpatterns</br>
</br>=====================================</br>
from django.urls import path</br>
from .views import homePageView</br>
urlpatterns = [ path('', homePageView, name='home')]</br>
</br>=====================================</br>
</br>
5) dans le fichier {{helloworld_project/urls.py}} ajouter le code suivant qui permet d'importer path et include et définit 
</br>le fichier url de notre application</br>
</br>=====================================</br>
from django.contrib import admin</br>
from django.urls import path, include # Nouveau</br> 

urlpatterns = [ path('admin/', admin.site.urls),</br>
		path('', include('pages.urls')),#Nouveau]</br>
 
</br>=====================================</br>
</br>
6) lancer la commande suivant  {{python manage.py runserver}}</br>
et visiter http://127.0.0.1:8000</br>
