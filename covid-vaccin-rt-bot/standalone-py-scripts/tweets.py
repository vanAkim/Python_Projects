import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("FRjTrMdRfIs22mjJFzOAFesCl",                         # CONSUMER_KEY
    "dKT7iC2UfvtLPDifBOrxksycWfG3S6Qm7vSBmHprwKFr524Jp5")                       # CONSUMER_SECRET
auth.set_access_token("966718127076708352-tQc9kNqiRrV6shJow6wHTOBsyNIVFnX",     # ACCESS_TOKEN
    "Bwice4HoTmeuTlXBQLRjrfzmW6lvQmyhEOreq4jjritL4")                            # ACCESS_TOKEN_SECRET

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

#api.update_status("Test tweet from Tweepy Python")



