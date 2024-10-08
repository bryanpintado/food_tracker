import requests
import ast
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
    'scope' : 'barcode'
    } 
    url = 'https://oauth.fatsecret.com/connect/token'
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        token = response.json()['access_token']
        return token
    else:
        print("Token not created",response.status_code,response.text)

def scan_barcode(barcode):
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
        return response.json()
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

def barcode_info():
    barcode = scan_barcode()

ex = scan_barcode(8076800195033)['food_id']['value']
print(ex)
#ex = ast.literal_eval(ex)
#print(ex['food_id']['value'])
#search_food('big mac')