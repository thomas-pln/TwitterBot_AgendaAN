from difflib import SequenceMatcher
from ics import Calendar, Event
import requests
import time


"""Retourne la date actuelle au bon format (YYYY-MM-DD)"""
def getDate():
    #return time.strftime("%Y-%m-%d")
    return "2021-05-20"


"""Cette méthode reconstitue l'URL puis la requête. Les données
reçues sont traitées pour enlever les espaces et tabulations."""
def getData():
    url = "https://www2.assemblee-nationale.fr/agendas/ics/" + getDate() + "/journalier"

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


"""Prend un objet Event (de la librairie ICS) ainsi que l'array qui
contient les événements. Cherche si les noms sont similaires (plus
de 80% de similitude."""
def contains(event, jsonEvents):
    for e in jsonEvents:
        if SequenceMatcher(None, event.name, e['name']).ratio() > 0.95:
            return True

    return False


"""Transforme une liste d'événements parsée avec la librairie ICS
en un array JSON, qui peut contenir plusieurs dates de début pour
un même événement."""
def toJsonArray(events):
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
                    i['description'].append(event.description)

        else:
            # L'événement n'est pas encore dans la liste, on ajoute :
            jsonEvents.append({
                "name": event.name, 
                "begin": [event.begin.to('Europe/Paris')],
                "description": [event.description]
            })

    return jsonEvents

"""
Récupère les données et les places dans un array : [{name,[begin],[description]}]
"""
def ready():
    # On récupère le fichier du site de l'AN
    rawData = getData()

    # On les traite avec la librairie ICS
    c = Calendar(rawData)

    # On récupère des données JSON exploitables, sans doublons
    json = toJsonArray(c.events)

    return json


agenda = ready()

for event in agenda:
    toPost = "\n ▶"+event['name']+"\n"
    for date, desc in zip(event['begin'],event['description']):
        toPost +=" ⏲ "+date.format('HH:mm')+" :\n\t"+desc
    print(toPost)

"""
# Affichage...
for elem in json:
    print("\n" + elem['name'])

    for date,desc in zip(elem['begin'],elem['description']):
        print("- "+ date.format('HH:mm'))
        print(desc)
"""