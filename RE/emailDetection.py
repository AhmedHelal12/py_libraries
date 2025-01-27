import re

text='hsoubAcademy9874@mail.net'
'''
        hsoub_academy@gmail.net
        hsoubAcademy@gmail.edu
        hsoubAcademy123@yahoo.com
        hsoub-academy9874@mail.net
'''
valid=re.search(r'\w+[\._-]?\w+@[a-zA-Z]+.[a-z]{2,}',text)

print(valid)