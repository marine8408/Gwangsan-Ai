import streamlit as st
import json
import xmltodict
import pandas as pd
import requests
from urllib.request import Request, urlopen 
from urllib.parse import urlencode, quote_plus

def main():
    apiurl = 'https://api.vworld.kr/req/address?'
    params = {
	    'service': 'address',
	    'request': 'getcoord',
	    'crs': 'epsg:4326',
	    'address': '광주광역시 광산구 신가동 1306',
	    'format': 'json',
	    'type': 'parcel',
	    'key': 'AF338F49-6AAA-3F06-BD94-FB6CB6817323' }

    response = requests.get(apiurl, params=params, verify=False)
    
    if response.status_code == 200:
        print(response.json())
        print("좌표추출끝")



#여기부터 토지이용속성 조회

    url = 'http://api.vworld.kr/ned/wfs/getLandUseWFS'
    queryParams = '?' + urlencode({ 'key' : '86DD225C-DC5B-3B81-B9EB-FB135EEEB78C', 'domain' : 'https://refactored-rotary-phone-975v95j496w62ppqx-8501.app.github.dev/', 'typename' : 'dt_d154', 'bbox' : '35.181171572168196,126.81539362917458,35.181171572168196,126.81539362917458,EPSG:4326', 'maxFeatures' : '10', 'resultType' : 'results', 'srsName' : 'EPSG:4326', 'output' : 'text/xml; subtype=gml/2.1.2'})   

    request = Request(url + queryParams)    
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read()
    print(response_body.decode('utf-8'))

main()