import time
import tweepy
import bot_keys
from tweepy.streaming import StreamListener
from tweepy import Stream


#Class to Print Tweets
class StdOutListener(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(bot_keys.CONSUMER_TOKEN, bot_keys.CONSUMER_SECRET)
    auth.set_access_token(bot_keys.ACCESS_TOKEN, bot_keys.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    stream = Stream(auth, listener)

    # Post a Tweet
    api.update_status('I am following a Tweepy Tutorial')

    # Information about Users
    user = api.me()
    user1 = api.get_user('gillerickKE')
    location = user1.location
    user_id = user1.id
    description = user1.description.encode('unicode-escape').decode('utf-8')

    # Display Tweets Based on Keywords
    keyword = 'Python'
    for tweet in api.search(q=keyword, lang='en', rpp=10):
        tweet.text = tweet.text.encode('unicode-escape').decode('utf-8')
        print(f'(tweet.user.name):(tweet.text)')

    # Display Trends
    trends = api.trends_place(1)
    for trend in trends[0]['trends']:
        print(trend['name'])

    for follower in tweepy.Cursor(api.followers).items():
        if follower.name == 'Gill Erick':
            print(follower.name)

    search = 'Javascript'
    nTweets = 500

    for tweet in tweepy.Cursor(api.search, search).items(nTweets):
        try:
            print('Tweet Liked')
            tweet.favorite()
            tweet.retweet()
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break