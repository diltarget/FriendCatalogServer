import tweepy
import time
import json
import config

def extract_tweets(screen_name):
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(config.twitter_consumer_key, config.twitter_consumer_secret)
    auth.set_access_token(config.twitter_access_token, config.twitter_access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    # save most recent tweets
    alltweets.extend(new_tweets)
    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        # save most recent tweets
        alltweets.extend(new_tweets)
        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

    return alltweets

def process_tweets(handle):
    """
    Gets a user's tweets, and converts it to JSON format usable for PI.
    :param handle:
        Handle of twitter user.
    :return:
        JSON dump to Personality Insights format.
    """
    alltweets = extract_tweets(handle)
    allcontent = []
    for tweet in alltweets:
        content = {"id": str(tweet.id_str),
                   "sourceid": "twitter",
                   "contenttype": "text/plain",
                   "language": tweet.lang,
                   "content": tweet.text,
                   "created": int(time.mktime(tweet.created_at.timetuple()))
                   }
        allcontent.append(content)
    jdump = json.dumps({"contentItems": allcontent}, sort_keys=True, indent=4)
    return jdump
