import requests
import os
from timeDate import today, datetime
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

        #Si ce n'est pas une réunion
        if(not event.name.startswith("Réunion - ")):
                # L'événement n'est pas encore dans la liste, on ajoute :
                jsonEvents.append({
                    "name": event.name, 
                    "begin": datetime.strptime(event.begin.to('Europe/Paris').strftime('%Y-%m-%d %X'), '%Y-%m-%d %X'), #suppression du time zone + formater
                    "description": event.description
                })

    return jsonEvents



def ready():
    """
    Récupère les données et les places dans une arrayliste : [{name,begin,description}]
    """

    # On récupère le fichier du site de l'AN
    rawData = getData()

    # On les traite avec la librairie ICS
    c = Calendar(rawData)

    # On récupère des données JSON exploitables, sans doublons
    json = toJsonArray(c.events)

    return sorted(json, key=lambda x : x['begin']) #retourne l'array triée par date (heure)

