from concurrent.futures import ProcessPoolExecutor
import requests
import time
import numpy as np
from datetime import datetime

def madefolder(): #未実装
	# 新たなファイルを作る
	print("madefolder")

def mainloop():
	# 時刻確認
	if get_day_of_week() < 5:
		print("Business day(営業曜日)")
		print(datetime.today().hour,"hor")

		if 11 <= int(datetime.today().hour) < 14:
			print("Business hours(営業時間)")
			with ProcessPoolExecutor(max_workers=3) as executor:
				executor.submit(GET_Narashino1)
				executor.submit(GET_Narashino2)
				executor.submit(GET_Tsudanuma)
			time.sleep(np.random.randint(5,10))
			mainloop()
		else:
			print("Not in Service")
			# 時間外処理を入れる
			loop_out()

	else:
		print("Not in Service")
		# 時間外処理を入れる
		loop_out()

def loop_out():
	print("loop_out")
	time.sleep(200)
	mainloop()

def get_day_of_week():
	print("get_day_of_week-(曜日を取得)")
	# '0' = "Mon."
	# '1' = "Tue."
	# '2' = "Wed."
	# '3' = "Thu."
	# '4' = "Fri."
	# '5' = "Sat."
	# '6' = "Sun."
	return datetime.today().weekday() 

def get_today():
	print("get_today-(取得時間)" ,datetime.today())
	return datetime.today()

def GET_Tsudanuma():
	# https://www.cit-s.com/i_catch/dining/tsudanuma.jpg
	# 採取してくるURL
	url = "https://www.cit-s.com/i_catch/dining/tsudanuma.jpg"
	date = str(datetime.now()).replace(' ', '-').replace('.', '-').replace(':', '-')
	file_name = "Tsudanuma/Tsudanuma_IMG" + str(date) + ".jpg"
	response = requests.get(url)
	image = response.content

	with open(file_name, "wb") as aaa:
		aaa.write(image)
	print("GET_IMG_Tsudanuma")

def GET_Narashino1():
	# https://www.cit-s.com/i_catch/dining/narashino1.jpg
	# 採取してくるURL
	url = "https://www.cit-s.com/i_catch/dining/narashino1.jpg"
	date = str(datetime.now()).replace(' ', '-').replace('.', '-').replace(':', '-')
	file_name = "Narashino1/Tsudanuma_IMG" + str(date) + ".jpg"
	response = requests.get(url)
	image = response.content

	with open(file_name, "wb") as aaa:
		aaa.write(image)
	print("GET_IMG_Narashino1")

def GET_Narashino2():
	# https://www.cit-s.com/i_catch/dining/narashino2.jpg
	# 採取してくるURL
	url = "https://www.cit-s.com/i_catch/dining/narashino2.jpg"
	date = str(datetime.now()).replace(' ', '-').replace('.', '-').replace(':', '-')
	file_name = "Narashino2/Tsudanuma_IMG" + str(date) + ".jpg"
	response = requests.get(url)
	image = response.content

	with open(file_name, "wb") as aaa:
		aaa.write(image)
	print("GET_IMG_Narashino2")

if __name__ == '__main__':
	mainloop()
