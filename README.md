# TwitterBot_AgendaAN FR
Bot twitter publiant dans un seul thread tout le programme de la journée à l'Assemblée Nationale (AN).

## Fichiers et Dossiers 
6 fichiers de code :
* getAgendaAN.py : récupère l'ordre du jour au format .ics sur le site de l'[Assemblée Nationale] (https://www2.assemblee-nationale.fr/agendas/les-agendas), sauvegarde les informations dans une arrayliste
* timeDate.py : 2 façons d'écrire la date (standard et fr)
* image.py : Crée une image avec la date courante à partir d'une image de base et la sauvegarde dans ``./data/txtImages``.
* basicTwitterFunctions.py : fonctions pour publier la file de tweets.
* config.py : clés pour utiliser l'API twitter.
* main.py : lanceur.

Folders :
* data
  * agendas: les agendas au format 'YYYY-MM-DD'.ics. téléchargés (n'est plus utilisé, les agenda ne sont enregistrés)
  * txtImages: les photos avec la date au format 'YYYY-MM-DD'.png.
  * util: l'image de base et la police utilisée pour l'écriture.

## Requière
Les bibliothèques [python-twitter](python-twitter.readthedocs.io) Python suivantes :

``pip install python-twitter``

* Vous devrez également créer un autre compte twitter (si vous n'utilisez pas votre compte twitter principal) et enregistrer votre (nouveau) compte comme Développeur.
* Créez une nouvelle application/un nouveau projet.
* Dans l'application, modifiez les "Permissions de l'application" pour autoriser la lecture et l'écriture et peut-être les messages directs.
* Générez les nouveaux tokens.
* Vous avez besoin de : 'Acces Token' , 'Access Token Secret' , 'API Key' et 'API Secret Key'.

Entrez-les dans le fichier config.py :
```python
import twitter

def getApi() :
    return twitter.Api(consumer_key='API Key',
                  consumer_secret='Clé secrète de l'API',
                  access_token_key='Token d'accès',
                  access_token_secret='Token d'accès secret', access_token_secret='Token d'accès secret'.
)
```

[Bibliothèque Requests](docs.python-requests.org) :

```pip install requests``

[Bibliothèque DateTime](docs.python.org/fr/3/library/datetime.html) :

```pip install DateTime`` : ``pip install DateTime''.

[Bibliothèque Pillow](pillow.readthedocs.io) :

``pip install Pillow``

Certaines bibliothèques sont déjà installées de base avec python.



# TwitterBot_AgendaAN EN
Bot Twitter tweeting the schedule of the day at the French National Assembly.

## Files/Folders
There is 6 files of code :
* getAgendaAN.py : get the agenda in .ics format from the [National Assembly](https://www2.assemblee-nationale.fr/agendas/les-agendas) website and save it the folfer ```./data/agendas```. Takes the file and saves the information in a list of lists.
* timeDate.py : 2 ways to write the date and a function time.sleep .
* image.py : Creates an image with the current date from a base image and save it in ```./data/txtImages```.
* basicTwitterFunctions.py : functions for posting tweets.
* config.py : keys to using the twitter API.
* main.py : launcher.

Folders :
* data
  * agendas: Folder of agendas in 'YYYY-MM-DD'.ics format.
  * txtImages: the pictures with the date in 'YYYY-MM-DD'.png format.
  * util: the the base image and the font used for the writing.
  
  


## What you need ?
Python's [python-twitter](python-twitter.readthedocs.io) library:

```pip install python-twitter```

* You will also need to create antoher twitter account (if you won't use youre main twitter account) and register you (new) account as Developper.
* Create a new app/project.
* In the app, modify the "App permissions" to allow Read and Write and perhaps Direct Messages.
* Generate the new tokens.
* You need : 'Acces Token' , 'Access Token Secret' , 'API Key' and 'API Secret Key'.

Enter them into config.py :
```python
import twitter

def getApi():
    return twitter.Api(consumer_key='API Key',
                  consumer_secret='API Secret Key',
                  access_token_key='Access Token',
                  access_token_secret='Access Secret Token'
)
```

[Requests library](docs.python-requests.org):

```pip install requests```

[DateTime library](docs.python.org/fr/3/library/datetime.html):

```pip install DateTime```

[Pillow library](pillow.readthedocs.io):

```pip install Pillow```

Some libraries are already installed at the same time as python.
