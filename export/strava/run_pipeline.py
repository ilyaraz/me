import requests
import json
import os
import pickle

url1 = 'http://www.strava.com/oauth/authorize?client_id=55349&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all,activity:read_all'
print('Paste {}'.format(url1)) 
print('Enter the token:')
token = input()
client_secret = pickle.load(open('token.pk', 'rb'))
payload = {'client_id': '55349', 'client_secret': client_secret, 'code': token, 'grant_type': 'authorization_code'}
response = requests.post('https://www.strava.com/oauth/token', data=payload)
token = response.json()['access_token']
page = 1
while True:
    response = requests.get('https://www.strava.com/api/v3/athlete/activities?page={}'.format(page), headers={'Authorization': 'Bearer {}'.format(token)})
    activities = response.json()
    if len(activities) == 0:
        break
    with open('data/summary_{}.json'.format(page), 'w') as summary_file:
        summary_file.write('{}\n'.format(json.dumps(activities)))
    for i in range(len(activities)):
        str_id = activities[i]['id']
        file_name = 'data/{}.json'.format(str_id)
        if os.path.exists(file_name):
            continue
        else:
            print('New: {}'.format(str_id))
        response = requests.get('https://www.strava.com/api/v3/activities/{}'.format(str_id), headers={'Authorization': 'Bearer {}'.format(token)})
        activity = response.json()
        with open(file_name, 'w') as activity_file:
            activity_file.write('{}\n'.format(json.dumps(activity)))
    page += 1
