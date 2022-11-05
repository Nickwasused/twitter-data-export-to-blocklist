# !/usr/bin/python3
from pathlib import Path
from time import sleep
from json import loads
from tqdm import tqdm
import requests
import logging
import os.path

logging.basicConfig(level=logging.INFO)


def loadfile(file):
    f = open(file, encoding="utf8")
    return f.read()


def writefile(file, data):
    with open(file, 'w') as f:
        f.write(data)


def get_user_id(username):
    response = requests.post("https://tweeterid.com/ajax.php", data={
        "input": username
    }, headers={
        "Origin": "https://tweeterid.com",
        "Referer": "https://tweeterid.com/",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
    })
    print(response.text)
    print(response.status_code)
    if response.status_code != 200:
        return None
    else:
        return response.text


ad_files = [
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
for ad_file in ad_files:
    path = Path(__file__).parent.absolute().joinpath(ad_file["file"])
    content = loadfile(path).replace(ad_file["replace"], "")
    temp_json_element = loads(content)
    for temp_json in temp_json_element:
        json_element.append(temp_json)

total_engagements = []

for element in json_element:
    try:
        cur_engagements = element["ad"]["adsUserData"]["adEngagements"]["engagements"]
    except KeyError:
        cur_engagements = element["ad"]["adsUserData"]["adImpressions"]["impressions"]
    for cur in cur_engagements:
        total_engagements.append(cur)

advertising = []
for element in total_engagements:
    try:
        advertising.append(element["impressionAttributes"]["advertiserInfo"]["screenName"])
    except KeyError:
        try:
            advertising.append(element["advertiserInfo"]["screenName"])
        except Exception:
            pass

# sort
advertising = list(dict.fromkeys(sorted(advertising)))
temp_advertising = []
for ad in advertising:
    temp_advertising.append(ad.replace("@", ""))

advertising = temp_advertising

logging.info(f"You have been engaged or impressed by {len(advertising)} advertisers!")

final_list = dict()
logging.info("requesting user ids")
for user_name in tqdm(advertising):
    user_id = get_user_id(user_name)
    if user_id == "error" or None:
        logging.warning("we hit a rate limit, waiting 60 seconds")
        sleep(60)
    final_list[user_name] = user_id
    print(final_list)
    # we don`t want to spam this free service as it is going to block us
    sleep(0.75)

export_file = Path(__file__).parent.absolute().joinpath("export.csv")
if os.path.exists(export_file):
    logging.info(f"removing file: {export_file}")
    os.remove(export_file)

logging.info(f"writing to file: {export_file}")
with open(export_file, 'w') as f:
    for item in final_list:
        try:
            f.write("{},\"{}\"\n".format(item["id"], item["name"]))
        except Exception:
            pass
    f.close()
