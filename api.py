import requests
from dotenv import load_dotenv
import os

load_dotenv()
cl_id = os.getenv('client_id')
cl_secret = os.getenv('client_secret')

#auth 2.0
def auth():
    payload = {
    'grant_type' : 'client_credentials',
    'client_id' : cl_id,
    'client_secret' : cl_secret,
    'scope' : 'barcode'
    } 
    url = 'https://oauth.fatsecret.com/connect/token'
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        print("Token not created",response.status_code,response.text)

def barcode_to_food_id(barcode):
    token = auth()
    if not token: 
        print("token error")
        return
    url = 'https://platform.fatsecret.com/rest/food/barcode/find-by-id/v1' 
    params = {
        'barcode' : str(barcode),
        'format' : 'json'
    }
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    response = requests.get(url=url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['food_id']['value']
    else: 
        print(response.status_code,response.text)

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

def barcode_info(barcode):
    food_id = int(barcode_to_food_id(barcode))
    token = auth()
    if not food_id:
        print('barcode_to_id() error')
    url = 'https://platform.fatsecret.com/rest/food/v4'
    params = {
        'food_id' : food_id,
        'format' : 'json'
    }
    headers = {
        'Authorization' : f'Bearer {token}'
    }
    response = requests.get(url=url, params=params, headers=headers)
    return response.json()

# barcode_info(8076800195033)
