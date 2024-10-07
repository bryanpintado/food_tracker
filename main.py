import requests
from dotenv import load_dotenv
import os

load_dotenv()
cl_id = os.getenv('client_id')
cl_secret = os.getenv('client_secret')



def auth():
    payload = {
    'grant_type' : 'client_credentials',
    'client_id' : cl_id,
    'client_secret' : cl_secret,
    'scope' : 'basic'
    } 
    url = 'https://oauth.fatsecret.com/connect/token'
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        print("Token not created",response.status_code,response.text)


def get_barcode(barcode):
    token = auth()
    if not token: 
        print("token error")
        return
    url = f'https://platform.fatsecret.com/rest/food/barcode/find-by-id/v1'
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    params = {
        'barcode' : str(barcode)
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print(response.text)
        return
    else: 
        print(response.status_code,response.text)
        return

def search_food(food_name):
    token = auth()
    if not token:
        print("token error")
        return
    url = 'https://platform.fatsecret.com/rest/foods/search/v1'
    params = {
        'search_expression' : str(food_name),
        'format' : 'json'
    }
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code == 200:
        print(response.json())


#get_barcode(8076800195033)
search_food('big mac')