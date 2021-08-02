import requests
import os
from timeDate import today
from difflib import SequenceMatcher
from ics import Calendar, Event



def getData():
    """
    Cette méthode reconstitue l'URL puis la requête. Les données
    reçues sont traitées pour enlever les espaces et tabulations.
    """


    url = "https://www2.assemblee-nationale.fr/agendas/ics/" + today() + "/journalier"

    try:
        # On envoie la requête
        req = requests.get(url)

    except requests.exceptions.RequestException as e:
        # Affichage ou action en cas d'erreur
        print("L'agenda n'a pas pu être récupéré")

    # On sépare les lignes dans un array
    lines = req.text.split("\n")

    # On enlève les tabulations et espaces aux extrémités
    sanitizedLines = []
    for line in lines:
        sanitizedLines.append(line.strip())

    # On retourne un string exploitable par la librairie ICS
    return '\n'.join(sanitizedLines)




def contains(event, jsonEvents):
    """
    Prend un objet Event (de la librairie ICS) ainsi que l'array qui
    contient les événements. Cherche si les noms sont similaires (plus
    de 80% de similitude.
    """
    for e in jsonEvents:
        if SequenceMatcher(None, event.name, e['name']).ratio() > 0.95:
            return True

    return False



def toJsonArray(events):
    """
    Transforme une liste d'événements parsée avec la librairie ICS
    en un array JSON, qui peut contenir plusieurs dates de début pour
    un même événement. 
    """

    jsonEvents = []

    # Pour chaque événement
    for event in events:

        # S'il (= son nom) est déjà contenu dans l'array
        if contains(event, jsonEvents):

            # On trouve l'élément de l'array qui contient le même nom
            for i in jsonEvents:
                if i['name'] == event.name:

                    # On ajoute une date de début supplémentaire aisni que la description
                    i['begin'].append(event.begin.to('Europe/Paris'))
                    #i['description'].append(event.description) #Décommenter pour garder les descriptions

        else:
            # L'événement n'est pas encore dans la liste, on ajoute :
            jsonEvents.append({
                "name": event.name, 
                "begin": [event.begin.to('Europe/Paris')],
                #"description": [event.description] #Décommenter pour garder les descriptions
            })

    return jsonEvents



def ready():
    """
    Récupère les données et les places dans un array : [{name,[begin],[description]}]
    """

    # On récupère le fichier du site de l'AN
    rawData = getData()

    # On les traite avec la librairie ICS
    c = Calendar(rawData)

    # On récupère des données JSON exploitables, sans doublons
    json = toJsonArray(c.events)

    return json




#Les fonctions suivantes (getAgenda(date) et readAgenda(file)) ne sont plus utilisées.
#Un exemple de calendrier ./ics se tronve dans /data/agendas
def getAgenda(date):
    """
    Reprend l'URL pour obtenir les données pour les enregistrer dans ./data/agendas/
    """
    url = 'https://www2.assemblee-nationale.fr/agendas/ics/'+date+'/journalier'
    #print(url)
    r = requests.get(url, allow_redirects=True)
    open('./data/agendas/'+date+'.ics', 'wb').write(r.content)
    r.close()


def readAgenda(file):
    """
    TZ : +00 (UTC 0)
    DTSTART : YYYYMMDDThhmmssZ
    [DTSTART][SUMMARY][DESCRIPTION]
    """


    try:
        c = open(file,'r', encoding='UTF-8')
        #print(c.read())
        agenda = []
        event = []

        for l in c:
            line = l.strip()
            if(line.startswith("DTSTART")):
                line = str(line.split('DTSTART:')[1])
                line = str(int(line[9]+line[10])+2)+"h"+ line[11]+line[12]
                event = []
                event.append(line)

            if(line.startswith("SUMMARY")):
                line = str(line.split('SUMMARY:')[1])
                line.replace("\\n","\n")
                event.append(line)

            if(line.startswith("DESCRIPTION")):
                line = str(line.split('DESCRIPTION:')[1])
                line.replace("\\n","\n")
                event.append(line)
                agenda.append(event)
        return agenda
    except OSError:
        print("File not Found")
        return -1



