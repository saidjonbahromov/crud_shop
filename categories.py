import requests
from pprint import pprint

def get_all_categories():
    response = requests.get('https://fakestoreapi.com/products/categories')
    if response.status_code == 200:
        products = response.json()
        return products

def get_all_carts():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        products = response.json()
        return products

products = get_all_carts()
pprint(products)