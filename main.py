from bs4 import BeautifulSoup

import requests 

japan_meteorological_agency_url = 'http://www.jma.go.jp/'

response = requests.get(japan_meteorological_agency_url+'jp/yoho/319.html')
data = BeautifulSoup(response.text, 'html.parser')

weather_elements = data.find(class_="info")

weather_text = str(weather_elements)

weather_text_replaced = weather_text.replace('<br/>', '　')

textlist = []

textlist = weather_text_replaced.split('　')



print(textlist[3])

