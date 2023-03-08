import requests

url = 'https://strawpoll.com/isiolo-central-secretary'
data = {'vote': 'Nasir ansaar'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

for i in range(5000):
    response = requests.post(url, data=data, headers=headers)
    print(response)

