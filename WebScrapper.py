import requests as re
response = re.get('http://192.168.1.1')
html = response.text
print(html)