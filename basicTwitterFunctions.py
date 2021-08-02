import twitter
from config import getApi
import os
import sys
import time

api = getApi()



def postStatus(update, replyTo):
    status = api.PostUpdate(update, in_reply_to_status_id=replyTo)
    #print(status)
    return(status.id)

def postStatusMedia(update, replyTo, media):
    status = api.PostUpdate(update,media=media, in_reply_to_status_id=replyTo)
    #print(status)
    return(status.id)

def search(keyWord,number):
    results = api.GetSearch(raw_query="q="+keyWord+"&result_type=recent&count="+number)
    return results
