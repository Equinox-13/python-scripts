import requests
import time

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    url = "http://api.icndb.com/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()['value']['joke']
    else:
        joke = "No joke"

    return joke

def divide(a, b):
    time.sleep(10)
    return a // b

class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        url = "http://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)

if __name__ == '__main__':
    print(get_joke())
