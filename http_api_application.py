""" This is a simple demonstrating how to get googlemap api results using python
	the most appropriate way here is json. after that we harmonize the json result to what we want
In this simple demo of creating the application,

As of now the application will not bring the desired results 
due to conversion to json. I intent to work this out and update immediately. 
However it answers the desired question which is
 the ability to get info from public APIS
"""
import urllib.request
import urllib.parse
import json
# first, the api url core

apiurl= 'https://ipfind.co?='
# the client input that would be used for full url
print('enter your ip address eg 8.8.8.8')
address = input()
# completing the url
completeurl = apiurl + urllib.parse.urlencode({'ip': address})
#  requesting for information using HTTp get method
# the data returned is usually in json form thus 
json_data = urllib.request.urlopen(completeurl).json()

country = json_data['country']

languages = json_data['languages']

print()

print(country)

print(languages)