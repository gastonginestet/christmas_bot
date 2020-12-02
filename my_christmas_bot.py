#! python
import tweepy
import time
import datetime

CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
ACCESS_KEY = 'your_access_key :)'
ACCESS_SECRET = 'your_access_secret :O'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def countdown_until_christmas():
    present = datetime.datetime.now()
    future = datetime.datetime(2020, 12, 24, 21, 0, 0)
    difference = future - present
    minutes = difference.total_seconds() / 60
    hours = minutes / 60
    message='Para Nochebuena falta ' + str(int(difference.days)) + ' dias, ' + str(int(hours)) + ' horas, ' + str(int(minutes)) + ' minutos.'
    return message

message=str(countdown_until_christmas())
print(message)
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return



def retrieve_actual_date(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_actual_date(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
    

def reply_totweets():
    print('Retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # usar 1189312810599243777
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')


    for mention in reversed(mentions):
        print(mention.user.screen_name + ' - ' + mention.full_text)
        print(mention.created_at)
        print(mention.id)
        print(' ')
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME) 
        if '#cuantofalta' in mention.full_text.lower():
            print('found #cuantofalta!')
            print('responding back...')
            message=str(countdown_until_christmas())
            print(mention.id)
            api.update_status('@'+ mention.user.screen_name + ' Hola ' +mention.user.name +'!! '+ message, mention.id )

while True:
        reply_totweets()
        time.sleep(10)

