import requests
import json

url = "https://opsgenie.status.atlassian.com/api/v2/status.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

dictionary1=json.loads(response.text)

print("Current system status: ",end='')
print(dictionary1['status']['description'])

url = "https://opsgenie.status.atlassian.com/api/v2/incidents.json"

payload={}
headers = {}

response2 = requests.request("GET", url, headers=headers, data=payload)

dictionary2=json.loads(response2.text)

print('\n')
print("Last three incidents:","\n")

for value in range (0,3):
 print("Issues: ",end='')
 print(dictionary2['incidents'][value]['name'])
 print("Created: ",end='')
 date_time_str = dictionary2['incidents'][value]['created_at']
 print(date_time_str[11]+date_time_str[12]+':'+date_time_str[14]+date_time_str[15]+' '+date_time_str[8]+date_time_str[9]+'/'+date_time_str[5]+date_time_str[6]+'/'+date_time_str[0]+date_time_str[1]+date_time_str[2]+date_time_str[3])
 print("Status: ",end='')
 print(dictionary2['incidents'][value]['status'])
 print("___")
