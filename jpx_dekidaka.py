import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
	url = 'https://nikkei225jp.com/chart/'
	response = requests.get(url)
	print(response.encoding)
	response.encoding = response.apparent_encoding
	soup = BeautifulSoup(response.text,'html.parser')
	titel = soup.title.string
	print(titel)

	#table.widetable:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2)
	#soup_html_parser =BeautifulSoup(response,'html')
	#n = soup.select_one('html body div#wrapper-area div#main-area div#main-areaIn div#readArea div div.component-normal-table table#stocks.widetable tbody tr.json-data td.a-left').text
	te = response.text
	price = te.split('<div class=val valN>')[1].split('</div>')[0].replace(',','')
#	price = te.split('<div class=val valN>')
	print (price)


if __name__ == "__main__":
	main()
