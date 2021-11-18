import requests

url = 'http://127.0.0.1:5000/result'
inputs={
    'First_name':'abc',
    'Last_name':'def',
    'gender':'M',
    'ssc p':96,
    'ssc boe':'Central',
    'hsc p':44,
    'hsc boe':'Others',
    'hsc spec':'Commerce',
    'ug p':67,
    'ug dt':'Comm&Mgmt',
    'pg p':88,
    'pg spec':'Mkt&HR',
    'etest p':77,
    'work ex':'Yes',
}
r = requests.post(url,json=inputs)

print(r.json())