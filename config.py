# Twitter Credentials
#
# To obtain the credentials, you must first have a Twitter account.
# Then, go to https://dev.twitter.com/, login, and click on "Manage Your Apps" to reach https://apps.twitter.com/.
# Then, click "Create New App", fill in the relevant fields, and click "Create your Twitter application".
# With the application created, navigate to the API Keys page and click "Create my access token".
# You now have the four necessary credentials. Copy the API key, API secret,
# Access token, and Access token secret here.
# NOTE: API key and API secret go in the twitter_consumer_key and twitter_consumer_secret vars.
#

twitter_consumer_key = "ggRcU15ypzao3YSBn1ZO9NdG4"
twitter_consumer_secret = "9nWFiGPCh2nBOTU4l9dvVN4hQQGGwS3KJFl5FA2IoYHPLF4Ihn"
twitter_access_token = "2911284366-0Co9YTS4atrktKRWyzV0o4S2hs2o2TCVgwJTVJj"
twitter_access_secret = "IqfjjEj9mvDNuBq8EpH7tns9ONVyjA2Z2zdbWN2wKok4y"

# Personality Insights credentials and URL
#
# You can obtain these credentials by binding a PI service to an application in bluemix and
# and clicking the "show credentials" link on the service in the application dashboard.
# Or you can use "cf env <application name>" from the command line to get the credentials.

pi_url = "https://gateway.watsonplatform.net/personality-insights/api"
pi_username = "87725ef2-e5ce-4b71-a9a6-cf3ef18fdfd8"
pi_password = "olxjgEFwsNia"


# Database information
db_username = '91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix'
db_password = "77f3fee25e14cd0c13c8ec0cf6d9b8aa364ef63c53dd5d3c257570916855a553"
db_url = "https://91819ede-4166-4871-bdb4-c58ee8e44e2c-bluemix.cloudant.com"
db_name = 'friend_db'
