# French-Natioanal-Assembly-agenda_TwitterBot
Bot Twitter tweeting the schedule of the day at the French National Assembly.

## Files/Folders
There is 6 files of code :
* getAgendaAN.py : get the agenda in .ics format from the [National Assembly](https://www2.assemblee-nationale.fr/agendas/les-agendas) website and save it the folfer ```./data/agendas```. Takes the file and saves the information in a list of lists.
* timeDate.py : 2 ways to write the date and a function time.sleep .
* image.py : Creates an image with the current date from a base image and save it in ```./data/txtImages```.
* basicTwitterFunctions.py : functions for posting tweets and searching (not used).
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
