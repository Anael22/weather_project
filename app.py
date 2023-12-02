import datetime as dt
import requests
from timezonefinder import TimezoneFinder
import pytz
import json
import streamlit as st

st.title('Weather App')

name = st.text_input('Enter your name', '')
if name:
    st.write(f'Hello {name}, welcome to the weather app!')


city= st.text_input("your city")
api_key="71964e4666d40691f8c7eafa0c0c1cd1" # your api key
basic_url="https://api.openweathermap.org/data/2.5/weather?"
url= (f"{basic_url}appid={api_key}&q={city}")
response= requests.get(url).json()
summarized_response= (f"""Weather description for {city}: {response['weather'][0]['description']}    
    Humidity:       {response['main']['humidity']:}%    
    Temperature:    {(response['main']['temp'])-273.15:.2f}C/{((response['main']['temp'])-273.15)*1.8 + 32:.2f}F    
    Sunset Time:    {dt.datetime.utcfromtimestamp(response['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S UTC')}    
    Sunrise Time:   {dt.datetime.utcfromtimestamp(response['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S UTC')}""")
print(summarized_response)
