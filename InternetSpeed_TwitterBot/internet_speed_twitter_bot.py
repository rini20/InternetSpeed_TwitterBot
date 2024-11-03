import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')


# post tweet using tweepy api
def post_tweet(download_speed, upload_speed, promised_speed):

    message = f"@yourisp My internet speed is download: {download_speed}/ upload: {upload_speed} mbps which is less than promised {promised_speed} mbps"
    client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret_key, access_token=access_token,
                           access_token_secret=access_token_secret)

    response = client.create_tweet(text=message, user_auth=True)
    post_id = response[0]['id']
    print(post_id)

    # Optional delete tweet
    delete_post = client.delete_tweet(id=post_id, user_auth=True)
    print(delete_post[0]['deleted'])

