import tweepy
creds= [
        'consumer_key':'your consumer key',
        'consumer_secret': 'your consumer secret',
        'access_token': 'your access token',
        'access_token_secret': 'your access token secret'
       ]
auth=tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
auth.set_sccess_token(creds['access_token'], creds['access_token_secret'])
api=tweepy.tweepy.API(auth)
api.update_status('my tweet!')
