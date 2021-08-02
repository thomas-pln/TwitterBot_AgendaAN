import twitter

def getApi():
    return twitter.Api(consumer_key='API Key',
                  consumer_secret='API Secret Key',
                  access_token_key='Access Token',
                  access_token_secret='Access Secret Token'
)
