from django import http
from django.http.response import JsonResponse
import requests
from urllib.parse import urlencode
import os
api_url = os.getenv("api_url")
import json
import urllib3
import certifi
# scheme='https',
netloc='https://libraries.io',
http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs=certifi.where(),
    num_pools=50,
    maxsize=10
)
params='',
query='api_key=YOUR_API_KEY', 
fragment=''

api_key="306cf1684a42e4be5ec0a1c60362c2ef"

def url_lib():
    path = '/api/search'
    payload = {
        'q': 'npm',
        'sort': "rank",
        'api_key': api_key,
    }
    query = urlencode(payload)
    url=f"{api_url}{path}?{query}"
    dum_data=requests(url)
    json_fiter=dum_data.json()        
    response =json.dumps(json_fiter)  
    print(response)

    # r = http.request('GET', url,headers={
    #     'Content-Type': 'application/json',
    #     'X-Content-Type-Options':'nosniff'
    # })
    
    # printa=json.loads(r.data.decode('utf-8'))
    # s=list(printa)
    
    return response
    

class api_endpoint():
    def base_url(path,query):
        url=f"{api_url}{path}?{query}"
        dum_data=http.request('GET', url)
        # json_fiter=dum_data.json()        
        # response =json.dumps(json_fiter)  
        responses =json.loads(dum_data.data.decode('utf-8'))
        return responses

        
    def url(path):
        url=f"{api_url}{path}?{api_url}"
        dum_data=http.request('GET', url)
        # json_fiter=dum_data.json()        
        # response =json.dumps(json_fiter)  
        responses =json.loads(dum_data.data.decode('utf-8'))
        return responses



        return responses    
        # print(url)
# 

