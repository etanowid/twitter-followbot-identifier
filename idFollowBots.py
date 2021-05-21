"""
Program will automatically identify follow-bots for any given Twitter account using Twitter API 
and the Tweepy library. 
"""

import tweepy
import time

 
# Access codes from Twitter

consumerkey = ''

consumersecret = ''

accesstoken = ''

accesstokensecret = ''


# Create API handle

auth = tweepy.OAuthHandler(consumerkey, consumersecret)

auth.set_access_token(accesstoken, accesstokensecret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

count = 0

# Retrieve all the followers of a Twitter account, -- can be modified
# Default is Twitter's official account (@twitter)
# Use the Cursor object to handle pagination work. 
# Pass the parameters into the Cursor constructor method.
# 40 specifies the number of items (followers) checked. -- can be modified

for follower in tweepy.Cursor(api.followers, id='twitter').items(40):
    user_dic = follower._json
    screen_name = user_dic['screen_name']
    num_follower = user_dic['followers_count']  
    num_following = user_dic['friends_count']
    num_tweet = user_dic['statuses_count']
    profile_image = user_dic['default_profile_image']
    date_of_creation = user_dic['created_at']

    print('Examining @%s...' % (screen_name))
    
    # Set conditions to narrow down all the followers to find follow-bots
    
    # Follow-bots typically have few followers
    if num_follower <= 20:
        
        # Follow-bots typically follow few others
        if num_following <= 20:
            
            # Follow-bots typically have few tweets
            if num_tweet <= 10:
                
                # Follow-bots typically do not have a profile picture. 
                # Returns True when the profile picture is the default picture, 
                # and False when the profile picture is not the default.
                if profile_image is True:
                    
                    # Follow-bots typically were created recently.
                    # We limit it from the last year and current year (2018 - 2019).
                    if '2018' in date_of_creation or '2019' in date_of_creation:
                        count += 1
                        print('Found follow-bot #%d: twitter.com/%s' % (count, screen_name))
    
    # Use this between network calls to avoid hitting the API limit
    time.sleep(60)

