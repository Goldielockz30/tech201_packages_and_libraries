# API

# Application Programming Interface

# How software can communicate with one another
# The API is the translator between the Client and the Server

# get means request the date, which is the main use of the API

# The API formats the returned data in JSON

import requests
import json

#
# post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
#
# print(post_codes_req) # <Response [200]>
#
# print(post_codes_req.status_code) # 200
#
# print(post_codes_req.headers) # http headers returned
# print(post_codes_req.content) # raw content
# print(post_codes_req.json) # json content
# print(type(post_codes_req.json())) # <class 'dict'>


# If I want specific details
# I'ts important to look at API documentation when sending something over, to get the rules right

json_body = json.dumps({"postcodes": ["PR8 5DB", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_red = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body) # we don't need the end code because we are asking for specific things from the API,
# this is the data we want to send

print(post_multi_red.json())


