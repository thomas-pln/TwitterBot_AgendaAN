from datetime import date, datetime
import time


def today():
    """
    Date actuelle format standard :
    YYYY-MM-DD
    """
    today = date.today()
    #print(today)
    return str(today)
    #return "2021-05-20"


def todayFR():
    """
    Date actuelle format français :
    DD / MM / YYYY
    """
    todaty = date.today()
    todaty = todaty.strftime('%d / %m / %Y')
    return str(todaty)


def sleep():
    """
    Déclencher tous les matins à 6h.
    Fonction non utilisée : ajouter une boucle dans le main et sleep() au tout début 
    ou à la toute fin de la boucle?
    """
    t =datetime.now()
    t = t.hour
    if(t>=0 and t<6):
        timeToSleep = 6-t*3600
        print(timeToSleep)
        time.sleep(timeToSleep)
    else:
        timeToSleep = (24-(t-6))*3600
        time.sleep(timeToSleep)
