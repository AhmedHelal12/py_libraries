import requests,json


response=requests.get(api)
my_api_list=json.loads(response.text)

if my_api_list['cod']!=404:
    description=my_api_list['weather'][0]['description']
    temp=my_api_list['main']['temp']
    humidity=my_api_list['main']['humidity']
    print(f'The description of the weather: {description}')
    print(f'The temperatue of the weather: {temp}')
    print(f'The humidity of the weather: {humidity}')



else:
    print('Please enter a valid city')
