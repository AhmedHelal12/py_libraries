import bs4
import requests
import csv

res=requests.get('https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers')
soup=bs4.BeautifulSoup(res.text,'html.parser')

table=soup.find('table')

header=table.find_all('th')
all_rows=table.find_all('tr')

data=[]
for number,x in enumerate(all_rows):
    value=[value.text.strip() for value in x if value.text.strip() !='']
    value[0]=number
    data.append(value)

print(data)


file=open('Language_file.csv','w')
writer=csv.writer(file)
writer.writerows(data)
file.close()

