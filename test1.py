import urllib.request
import socket
import datetime
import pandas_datareader.data as pdr
import quandl
#from read_nikkei import get_jstock


def web_get():
	host = socket.gethostname()
	print(host)

	url = 'http://192.168.11.1'

	with urllib.request.urlopen(url) as res :

		body = print(res.read())

def date_transfer(box):
	print(box)
	year, month, day = box.split("-")
	print(year,"年",month,"月",day,"日")
	transfer = datetime.date(int(year),int(month),int(day))
	print(transfer)
	return transfer

#def get_invester(s_date,e_date):
#	pd_data = pdr.DataReader('2427.jp','stooq',s_date,e_date)	
#	pd_data = pdr.get_data_yahoo('2427',s_date,e_date)	
#	print(pd_data)

#	gd_nikkei = get_jstock(2427,'W',s_date,e_date)
#	print(gd_nikkei)

def get_quandl(s_date,e_date):
	print("satrt=",s_date,"  end=",e_date)
	data = quandl.get("YC/USA10Y",s_date,e_date)
	print(data)
#	data.head()

def main():
	arraw1 = [5,3,2,5,3,1,0]
	print("length=",len(arraw1))

#	for a in arraw1:
#		print(a)

	for num in range(7):
		if num % 5:
			print (arraw1[num])
		else:
			print ("*",arraw1,"----",arraw1[num])

	start = date_transfer("2011-3-22")
	end = date_transfer("2011-4-08")
#	get_invester(start,end)


if __name__ == ("__main__"):
	main()

