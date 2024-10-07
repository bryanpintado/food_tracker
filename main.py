import requests
from dotenv import load_dotenv
import os

load_dotenv()
cl_id = os.getenv('client_id')
cl_secret = os.getenv('client_secret')

auth_url = 'https://oauth.fatsecret.com/connect/token'

def auth():
    payload = {
    'grant_type' : 'client_credentials',
    'client_id' : cl_id,
    'client_secret' : cl_secret,
    'scope' : 'basic'
    } 
    response = requests.post(auth_url, data=payload)
    token = response.json()['access_token']
    return token

def get_barcode(f_id):
    token = auth()
    barcode = str(f_id)
    url = f'https://platform.fatsecret.com/rest/food/barcode/find-by-id/v1'
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    params = {
        'barcode' : barcode
    }
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code,response.text)

get_barcode(8076800195033)