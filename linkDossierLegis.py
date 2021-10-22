import csv
import json
from difflib import SequenceMatcher
import requests

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, delimiter=";") 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding="utf-8") as jsonf: 
        sort = sorted(jsonArray, key=lambda x : x['Date initiale'], reverse=True)
        jsonString = json.dumps(sort, indent=4)
        jsonf.write(jsonString)



def findLegisURL(spletedStr):
    """
    Regarde si la chaine de caratère contient le mot clé 'discussion', si oui rechcher le dossier législatif correspondant puis
    ajoute dans le tableau de retour, sinon ajoute seulement la chaine de caractère (pas de dossier législatif)

    spletedStr : String[]
    """
    ret =[]
    js = json.loads(open('./data/doss.json', encoding="utf-8").read()) #JSON de tous les dossiers législatifs
    for s in spletedStr:
        if "discussion" in s.lower(): #A probablement un doss. légis.
            discIdx = s.lower().index("discussion")+14 #Index du mot "discussion" dans le paragraphe + 14 (après 'discussion du ')
            s2 = s[discIdx:].lower()
            i = 0
            find = True
            while find and i<len(js):
                if SequenceMatcher(None, s2, js[i]['Titre'].lower()).ratio() > 0.80:
                    ret.append(s+".\nDossier législatif: "+js[i]['URL du dossier'])
                    find = False
                i+=1
            if find == True: #Pas de doss. legis. trouvé
                ret.append(s)
        else: #N'as pas de doss. legis.
            ret.append(s)
    return ret

    
def getDossiersLois():
    """
    Requête, récupère et enreigitre la liste de tous les textes de loi promulgués et en cours de discussion
    La Fabrique de la Loi: https://www.lafabriquedelaloi.fr/
    """

    url = "https://www.lafabriquedelaloi.fr/api/dossiers.csv"

    try:
        # On envoie la requête
        req = requests.get(url)

    except requests.exceptions.RequestException as e:
        # Affichage ou action en cas d'erreur
        print("dossiers.csv de La Fabrique de la Loi n'a pas pu être récupéré")
    
    open('./data/lawTxts/dossiers.csv', 'wb').write(req.content)
    req.close()
