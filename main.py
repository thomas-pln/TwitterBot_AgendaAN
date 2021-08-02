from getAgendaAN import ready
from timeDate import todayFR, today, sleep
from basicTwitterFunctions import postStatus, postStatusMedia
from image import printTxtImage

#limit : 280 chars

def main():
    day = today()
    dayFR = todayFR()

    Diary = ready()
    
    printTxtImage() #Creates image
    tweet_id = postStatusMedia(dayFR, None, "./data/txtImages/"+day+".png") #First tweet of the thread

    for event in Diary:

        toPost = "\n ▶"+event['name']
        charEmote = 1 #1 emote = 2 chars

        """
        for date, desc in zip(event['begin'],event['description']):
            toPost +="\n ⏲ "+date.format('HH:mm')+" :\n\t"+desc
            charEmote+=1
        """

        for date in event['begin']:
            toPost +="\n ⏲ "+date.format('HH:mm')
            charEmote+=1

        print(toPost) #debug
        
        #Division des strings pour faire au plus 280 caractères : 
        if len(toPost) <=280-charEmote:
            tweet_id = postStatus(toPost, tweet_id)
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
