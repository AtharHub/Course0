import requests

url = 'https://jsonplaceholder.typicode.com/posts'

try:
    response = requests.get(url)
    if response.status_code < 400:
        posts = response.json()
        for i in range(5):
            print(posts[i])
    else:
        print("Didn't get the required response for the http request!!")
except Exception as e:
    print(e)