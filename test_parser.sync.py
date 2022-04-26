import requests
from datetime import datetime


start_time = datetime.now()


response = requests.get(url=input("url = "), params= input("params = "))
answer = response.json
answer_page = response.json()
print (answer_page)
print (answer)
print(datetime.now() - start_time)
