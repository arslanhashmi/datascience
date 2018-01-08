
from InstagramAPI import InstagramAPI

api = InstagramAPI("03218800067", "narrow12")
api.login() # login
#print(api.getProfileData())
#print(api.LastJson)
print(api.getSelfUserFeed())
#print(api.LastJson)
for k in api.LastJson['items']:
    print(k)

print(api.getSelfUserFeed())
#print(api.LastJson)
for k in api.LastJson['items']:
    print(k)

#api.tagFeed("lifestory") # get media list by tag #cat
#media_id = api.LastJson # last response JSON
#print(media_id)
#api.like(media_id["ranked_items"][0]["pk"]) # like first media
#api.getUserFollowers(media_id["ranked_items"][0]["user"]["pk"]) # get first media owner followers
