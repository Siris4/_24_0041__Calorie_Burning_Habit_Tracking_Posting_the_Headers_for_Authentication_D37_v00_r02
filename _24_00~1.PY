import requests, os

USERNAME = os.environ.get('USERNAME')    #encrypted
print(f"The USERNAME is: {USERNAME}")


TOKEN = os.environ.get('TOKEN')    #encrypted
print(f"The TOKEN is: {TOKEN}")
# Step 1):

pixela_endpoint = "https://pixe.la/v1/users"  # everything before the space and -d

'''
token	string	[required] A token string used to authenticate as a user to be created. The token string is hashed and saved.
Validation rule: [ -~]{8,128}
username	string	[required] User name for this service.
Validation rule: [a-z][a-z0-9-]{1,32}
agreeTermsOfService	string	[required] Specify yes or no whether you agree to the terms of service.
Please see: Terms of service - Japanese version / Terms of service - English version
notMinor	string	[required] Specify yes or no as to whether you are not a minor or if you are a minor and you have the parental consent of using this service.
'''

user_params = {
    "token": TOKEN,  # user generated, so make it up yourself.
    "username": USERNAME,     # pick a username. Let's stay consistent with the dev account naming convention, but no periods in the username.
    "agreeTermsOfService": "yes",   # remember that Keys have to be IDENTICAL to any and all CAPS involved, so copy and paste Key names.
    "notMinor": "yes",   # 4 total service agreements to POST a request, up to this point
}

# pixela_response = requests.post(url=pixela_endpoint, json=user_params)
# print(pixela_response.text)  # give it back to me in a peice of text, instead of JSON format, which we just want to visually see it quickly, so no need to keep in JSON for now, if data manipulation is not being done with it.
# print(pixela_response.json)  # if you really do want the data back in a JSON format.
#{"message":"Success. Let's visit https://pixe.la/@siris1dev , it is your profile page!","isSuccess":true}
#<bound method Response.json of <Response [200]>>

# If you run it a second time:
#{"message":"This user already exist.","isSuccess":false}
#<bound method Response.json of <Response [409]>>

# Step 2): $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 'X-USER-TOKEN:thisissecret' -d '{"id":"test-graph","name":"graph-name","unit":"commit","type":"int","color":"shibafu","timezone":"Asia/Tokyo","isSecret":true,"publishOptionalData":true}'
# {"message":"Success.","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# [required] It is an ID for identifying the pixelation graph.
# Validation rule: ^[a-z][a-z0-9-]{1,16}
graph_config = {    #similar to params, but for the graph part of the POST REQUEST:
    "id": "graph1",
    "name": "Calorie Burning Graph",
    "unit": "calorie(s)",
    "type": "int",
    "color": "sora"   # (blue color, in their Japanese variable names)
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Make another POST REQUEST within the HEADER:
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(graph_response.text)
#{"message":"This graphID already exist."