### For the purposes of this exercise, we define three types of Twitter users:
    # - Layman: Users with less than 100 followers
    # - Expert: Users with 100-1000 followers
    # - Celebrity: Users with more than 1000 followers
### Using the Twitter API, and starting with the @WUSTLPoliSci Twitter user, answer the following:
# One degree of separation:
    # - Among the followers of @WUSTLPoliSci, who is the most active?
    # - Among the followers of @WUSTLPoliSci, who is the most popular -- i.e., who has the greatest number of followers?
    # - Among the friends of @WUSTLPoliSci (who the @ follows), who are the most active layman, expert, and celebrity?
    # - Among the friends of @WUSTLPoliSci, who is the most popular?
# Two degrees of separation:
    # - Among the followers of @WUSTLPoliSci and their followers, who is the most active?
    # - Among the friends of @WUSTLPoliSci and their friends, who is the most active?
    
### Setting things up 
import os
os.chdir(r'C:\Users\jorda\OneDrive\Keys')

import importlib
import tweepy

import random
import time


twitter = importlib.import_module('start_twitter_jdw')
api = twitter.client

### Some diagnostics
#limit = api.rate_limit_status()
#limit.keys() ##look at dictionary's keys

#limit["resources"] ## another dictionary
#limit["resources"].keys()
#limit["resources"]["tweets"] ## another dictionary!!

### Creating the WUSTL user we're interested in (I know there's more to WashU than political science, but this is easier)
washu = api.get_user('@WUSTLPoliSci')
#print(washu.followers_count)

### So for part 1, we're only interested in 625 (as of 8/20/21) accounts.
### Creating the list of followers -- this will take a while to run:
washu_followers = []
for item in tweepy.Cursor(api.followers, 'WUSTLPoliSci').items():
    washu_followers.append(item)
    print(item.name)
    time.sleep(random.uniform(1, 3))

#print("There are {} followers of WashU Political Science.".format(washu.followers_count))
#print()

### First, the most active followers.
followers_active = {}
for i in range(len(washu_followers)):
    name = washu_followers[i].name
    tweets = washu_followers[i].statuses_count
    followers_active[name] = tweets
#print(followers_active)

most_active_name = max(followers_active, key=followers_active.get)
most_active_tweets = followers_active[max(followers_active, key=followers_active.get)]

#print("Of the WashU Political Science followers, '{}' is the most active, with {} tweets.".format(most_active_name, most_active_tweets))
#print()

### Next, the most followed followers.
followers_followed = {}
for i in range(len(washu_followers)):
    name = washu_followers[i].name
    followed = washu_followers[i].followers_count
    followers_followed[name] = followed
#print(followers_followed)

most_followed_name = max(followers_followed, key=followers_followed.get)
most_followed_followers = followers_followed[max(followers_followed, key=followers_followed.get)]

#print("Of the WashU Political Science followers, '{}' has the most followers, with {}.".format(most_followed_name, most_followed_followers))
#print()

### Part 2: Friends
# Procedurally, this is basically the same as part 1
washu_friends = []
for item in tweepy.Cursor(api.friends, 'WUSTLPoliSci').items():
    washu_friends.append(item)
    print(item.name)
    time.sleep(random.uniform(1, 3))

#print("WashU Political Science follows {} accounts on Twitter.".format(len(washu_friends)))
#print()

# Designating the laymen, experts, and celebrities.
laymen = {}
experts = {}
celebs = {}

for i in range(len(washu_friends)):
    name = washu_friends[i].name
    followers = washu_friends[i].followers_count
    tweets = washu_friends[i].statuses_count
    
    if followers <100:
        laymen[name] = tweets

    if followers in range(100, 1000):
        experts[name] = tweets
        
    if followers > 1000:
        celebs[name] = tweets
        
#print(laymen)
#print(experts)
#print(celebs)

# The most active of each:
most_active_laymen = max(laymen, key=laymen.get)
most_active_laymen_tweets = laymen[max(laymen, key=laymen.get)]

most_active_expert = max(experts, key=experts.get)
most_active_expert_tweets = experts[max(experts, key=experts.get)]

most_active_celeb = max(celebs, key=celebs.get)
most_active_celeb_tweets = celebs[max(celebs, key=celebs.get)]

#print(most_active_laymen)
#print(most_active_expert)
#print(most_active_celeb)

#print("The most active of the laymen is '{}' with {} tweets.".format(most_active_laymen, most_active_laymen_tweets))
#print("The most active of the experts is '{}' with {} tweets.".format(most_active_expert, most_active_expert_tweets))
#print("The most active of the celebs is '{}' with {} tweets.".format(most_active_celeb, most_active_celeb_tweets))

### Part 3: Followers of Washu Followers
washu_followers_squared = []

# This doesn't work if you try to get a user with protected accounts/tweets.

for i in washu.followers_ids():
    try:
        follower = api.get_user(i)
        print(follower.name)
        print("@{}".format(follower.screen_name))
        print(follower.id)
        print("{} is followed by:".format(follower.name))
        for j in follower.followers_ids():
            follower_squared = api.get_user(j)
            #print(follower_squared.name)
            print("@{}".format(follower_squared.screen_name))
            #print(follower_squared.id)
            print()
            washu_followers_squared.append(follower_squared)
        print()
        time.sleep(random.uniform(1,3))
    except tweepy.TweepError:
        print("Failed to run the command on that user, Skipping...")

# This is basically the same as part 1
followers_squared_active = {}
for i in range(len(washu_followers_squared)):
    name = washu_followers_squared[i].name
    tweets = washu_followers_squared[i].statuses_count
    followers_squared_active[name] = tweets
#print(followers_active)

most_active_followers_squared_name = max(followers_squared_active, key=followers_squared_active.get)
most_active_followers_squared_tweets = followers_squared_active[max(followers_squared_active, key=followers_squared_active.get)]

#print("Of the WashU Political Science followers and followers of followers, '{}' is the most active, with {} tweets.".format(most_active_followers_squared_name, most_active_followers_squared_tweets))
#print()


# Part 4: Followers of WashU friends
# It's unclear why the user.friends_ids does not work
# It returns an error: AttributeError: 'User' object has no attribute 'friends_ids'
# I've included a try/except so it doesn't break the rest of the script,
# but it *should* function in basically the same manner as part 3.
# And the documentation -- https://docs.tweepy.org/en/v3.10.0/api.html -- suggests such.

washu_friends_squared = []

try:
    for i in washu.friends_ids():
        friend = api.get_user(i)
        print(friend.name)
        print("@{}".format(friend.screen_name))
        print(friend.id)
        print("WashU Politicial Science follows @{}, who follows:".format(follower.name))
        for j in friend.friend_ids():
            friend_squared = api.get_user(j)
            #print(follower_squared.name)
            print("@{}".format(friend_squared.screen_name))
            #print(follower_squared.id)
            print()
            washu_friends_squared.append(friend_squared)
        print()
        time.sleep(random.uniform(1,3))
        
    friends_squared_active = {}
    for i in range(len(washu_friends_squared)):
        name = washu_friends_squared[i].name
        tweets = washu_friends_squared[i].statuses_count
        friends_squared_active[name] = tweets
    #print(followers_active)

    most_active_friends_squared_name = max(friends_squared_active, key=friends_squared_active.get)
    most_active_friends_squared_tweets = friends_squared_active[max(friends_squared_active, key=friends_squared_active.get)]
    
    #print("Of the WashU Political Science friends and friends of friends, '{}' is the most active, with {} tweets.".format(most_active_friends_squared_name, most_active_friends_squared_tweets))
    #print()
except:
    pass

#print("Of the WashU Political Science friends and friends of friends, '{}' is the most active, with {} tweets.".format(most_active_friends_squared_name, most_active_friends_squared_tweets))
#print()

### Appendix: All results, stated:
print("There are {} followers of WashU Political Science.".format(washu.followers_count))
print()
print("Of the WashU Political Science followers, '{}' is the most active, with {} tweets.".format(most_active_name, most_active_tweets))
print()
print("Of the WashU Political Science followers, '{}' has the most followers, with {}.".format(most_followed_name, most_followed_followers))
print()
print("WashU Political Science follows {} accounts on Twitter.".format(len(washu_friends)))
print()
print("The most active of the laymen is '{}' with {} tweets.".format(most_active_laymen, most_active_laymen_tweets))
print("The most active of the experts is '{}' with {} tweets.".format(most_active_expert, most_active_expert_tweets))
print("The most active of the celebs is '{}' with {} tweets.".format(most_active_celeb, most_active_celeb_tweets))
print()
print("Of the WashU Political Science followers and followers of followers, '{}' is the most active, with {} tweets.".format(most_active_followers_squared_name, most_active_followers_squared_tweets))
print()
#print("Of the WashU Political Science friends and friends of friends, '{}' is the most active, with {} tweets.".format(most_active_friends_squared_name, most_active_friends_squared_tweets))
