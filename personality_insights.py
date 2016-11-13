import json
import os
import requests

import config as config
import twitter_helper as twitter_helper
from watson_developer_cloud import PersonalityInsightsV3


def send_pi_request(handle):
    """
    Send a request to PI given a handle name
    :return:
    JSON in python format
    """
    tweet_data = twitter_helper.process_tweets(handle)
    r = requests.post(config.pi_url + '/v2/profile',
                      auth=(config.pi_username, config.pi_password),
                      headers={
                          'content-type': 'application/json',
                          'accept': 'application/json'
                      },
                      data=tweet_data
                      )
    print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
    return json.loads(r.text)

def extract_personality(pi_data):
    """
    Extract big 5 personality traits from PI json output and places it in a dictionary
    :param pi_data:
    :return:
    """
    big5 = {}
    personality = pi_data['tree']['children'][0]['children'][0]['children']
    for trait in personality:
        name = trait['name']
        value = trait['percentage']
        big5[name] = value
    return big5

if __name__ == '__main__':
    users = ['DaveRench', 'soc_brianne', 'gravitysydney', 'KevinReuning']
    user = users[2]
#    data = send_pi_request(user)
    filename = "./data/person2.json"
    with open(os.path.join(os.path.dirname(__file__), './data/person.json')) as pi_json:
        data = json.load(pi_json)
    pdata = extract_personality(data)
    new_data = {'handle': user, 'personality': pdata}
    print(new_data)

