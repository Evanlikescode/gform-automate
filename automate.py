import requests
from bs4 import BeautifulSoup

##########################
'patent : Evan Haryo'
'version : 1.0'
##########################

print('#####################################')

print('MASUKKAN LINK MU DISINI UNTUK MENGECEK BANYAK SALAH')


links = input('masukkan link : ')


print('#####################################')

print('Output')


print('#####################################')



link = requests.get(links)

soup = BeautifulSoup(link.text, 'html.parser')

posts = soup.findAll(class_='freebirdFormviewerViewItemsRadioIncorrect')

print('banyak salah : ', len(posts))



