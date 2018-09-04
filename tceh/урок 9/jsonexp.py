import json
import requests

def get_red():
    url = 'https://jsonplaceholder.typicode.com/comments'
    r = requests.get(url)
    return r.content

def write_to_file( content, mode='w'):
    with open('rez.json', mode=mode) as f:
        f.write(content)

data = get_red()

obj = json.loads(data)
for k,v in obj.items():
    print('{}:{}').format(k,v)


stroka = json.dumps(obj)

write_to_file(stroka)