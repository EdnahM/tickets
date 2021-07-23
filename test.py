## requests for API's
import requests

BASE = 'http://127.0.0.1:5001'
PORT = '27017'

response = requests.get(BASE + '/tickets' )


print(response.json())