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
	    'address': '광주광역시 광산구 송정동 833-8',
	    'format': 'json',
	    'type': 'parcel',
	    'key': 'AF338F49-6AAA-3F06-BD94-FB6CB6817323' }

    response = requests.get(apiurl, params=params, verify=True)
    
    if response.status_code == 200:
        print(response.json())
        data = response.json()

        # 브이월드 서버 지오코더에서 받아온 데이타 중 좌표 x, y 값 출력
        x = data['response']['result']['point']['x']
        y = data['response']['result']['point']['y']
        address = data['response']['input']['address']   #입력한 주소 보여주기
        st.write(address)
        #print(x, y)

        
        # Extracting data for table
        #result_info = data['response']['result']
        #point_info = result_info['point']

        #df = pd.DataFrame([
        #['Service Address', result_info['point']],
        #['Longitude', point_info['x']],
        #['Latitude', point_info['y']]
        #], columns=['Key', 'Value'])
        #print(df)

        #print("좌표추출끝")
        
        #st.write(data)          #json 구조 확인 중요


        #여기부터 토지이용속성 조회
        pbbox = f'{y},{x},{y},{x},EPSG:4326'    #pbbox 변수에 지오코더 좌표 값 문자열 받기

        url = 'https://api.vworld.kr/ned/wfs/getLandUseWFS'

        
        #queryParams = '?' + urlencode({
        #    'key' : '86DD225C-DC5B-3B81-B9EB-FB135EEEB78C',
        #    'typename' : 'dt_d154',
        #    'bbox' : pbbox,
        #    'maxFeatures' : '10',
        #    'resultType' : 'results',
        #    'srsName' : 'EPSG:4326',
        #    'output' : 'text/xml; subtype=gml/2.1.2'})   

        #request = Request(url + queryParams)
        #request.get_method = lambda: 'GET'
        #response_body = urlopen(request).read()
        #print(response_body.decode('utf-8'))
        

        params = {
            'key' : '86DD225C-DC5B-3B81-B9EB-FB135EEEB78C',
            'typename' : 'dt_d154',
            'bbox' : pbbox,
            'maxFeatures' : '10',
            'resultType' : 'results',
            'srsName' : 'EPSG:4326',
            'output' : 'application/json'}

        
        response = requests.get(url, params=params, verify=True)
        data = response.json()          
        #st.write(data)           #json 구조 확인 중요

        geodata = data['features'][0]['properties']['prpos_area_dstrc_nm_list']
        geopdata = f'{geodata}'
        st.write(geopdata)
main()