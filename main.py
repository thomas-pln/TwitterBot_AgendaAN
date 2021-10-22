from getAgendaAN import ready
from time import sleep
from timeDate import todayFR, today, sleep, datetime
from basicTwitterFunctions import postStatus, postStatusMedia
from image import printTxtImage

limit = 280 #chars
csvFilePath = './data/dossiers.csv'
jsonFilePath = './data/doss.json'


def main():
    day = today()
    dayFR = todayFR()

    agenda = ready()
    
    printTxtImage() #Créer l'image
    postStatusMedia(dayFR, None, "./data/txtImages/"+day+".png") #Premier tweet de la journée



    for event in agenda:

        now = datetime.now()
        diff = event['begin'] - now
        diff = diff.total_seconds() - 600   
        #600s = 10min, tweeter 10 minutes avant l'événement (ou s'il est déjà passé)
        if diff>0:
            sleep(diff)


        toPost = "▶"+event['name']+"\n⏲ "+event['begin'].strftime('%X')+event['description']
        charEmote = 1 #1 emote = 2 chars

        print(toPost) #debug
        
        #Division des strings pour faire au plus 280 caractères : 
        if len(toPost) <=280-charEmote:
            tweet_id = postStatus(toPost, None)
            print("toPost :",len(toPost)) #debug
        else:
            toPostL = toPost
            endEvent = False
            while(not endEvent):
                
                if(len(toPostL) <=280-charEmote):
                    if(len(toPostL)>0):
                        tweet_id = postStatus(toPostL, tweet_id)

                        print("toPostL 1: ",len(toPostL)) #debug

                    endEvent = True
                elif (toPostL[280-charEmote]==' '):
                    print("toPostL 2: ",len(toPostL[:280-charEmote])) #debug

                    tweet_id = postStatus(toPostL[:280-charEmote], tweet_id)
                    toPostL = toPostL[280-charEmote:]
                else:
                    i = 280-charEmote
                    while(not toPostL[i] == ' '):
                        i-=1
                    print("toPostL 3: ",len(toPostL[:i])) #debug
                    tweet_id = postStatus(toPostL[:i], tweet_id)
                    toPostL = toPostL[i:]
                

main()
