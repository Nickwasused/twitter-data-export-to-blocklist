from json import loads

def loadfile(file):
    f = open(file, encoding="utf8")
    return f.read()

def writefile(file, data):
    with open(file, 'w') as f:
        f.write(data)

adfiles = [
    {
        "file": "export/data/ad-engagements.js",
        "replace": "window.YTD.ad_engagements.part0 = "
    },
    {
        "file": "export/data/ad-impressions.js",
        "replace": "window.YTD.ad_impressions.part0 = "
    }
]

json_element = []
for adfile in adfiles:
    content = loadfile(adfile["file"]).replace(adfile["replace"], "")
    temp_json_element = loads(content)
    for temp_json in temp_json_element:
        json_element.append(temp_json)

total_engagements = []

for element in json_element:
    try:
        cur_engaements = element["ad"]["adsUserData"]["adEngagements"]["engagements"]
    except:
        cur_engaements = element["ad"]["adsUserData"]["adImpressions"]["impressions"]
    for cur in cur_engaements:
        total_engagements.append(cur)

advertising = []
for element in total_engagements:
    try:
        advertising.append(element["impressionAttributes"]["advertiserInfo"]["screenName"])
    except:
        try:
            advertising.append(element["advertiserInfo"]["screenName"])
        except:
            pass

# sort
advertising = list(dict.fromkeys(sorted(advertising)))
temp_advertising = []
for ad in advertising:
     temp_advertising.append(ad.replace("@", ""))

advertising = temp_advertising

print("You have been engaged or impressed by {} advertisers!".format(len(advertising)))

from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Start fetching user ids
import tweepy
  
# assign the values accordingly
consumer_key = getenv("API_KEY")
consumer_secret = getenv("API_SECRET")
access_token = getenv("ACCESS_TOKEN")
access_token_secret = getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

import time

ad_lists = [advertising[i:i+100] for i in range(0, len(advertising), 100)]

final_list = []

for ad_list in ad_lists:
    request = api.lookup_users(screen_name=ad_list)
    for account in request:
        final_list.append({
            "id": account.id,
            "name": account.screen_name
        })

with open('./export.csv', 'w') as f:
    for item in final_list:
        print(item)
        try:
            f.write("{},\"{}\"\n".format(item["id"], item["name"]))
        except:
            pass
    f.close()


