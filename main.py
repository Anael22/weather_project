import datetime as dt
import requests
from timezonefinder import TimezoneFinder
import pytz
import json

city= "Paris"#(input("your city"))
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




api_key="71964e4666d40691f8c7eafa0c0c1cd1" # your api key
def get_weather_data(city_name):
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    response = requests.get(base_url).json()
    data = response
    summarized_response = (f"""Weather description for {city_name}: {response['weather'][0]['description']}    
        Humidity:       {response['main']['humidity']:}%    
        Temperature:    {(response['main']['temp']) - 273.15:.2f}C/{((response['main']['temp']) - 273.15) * 1.8 + 32:.2f}F    
        Sunset Time:    {dt.datetime.utcfromtimestamp(response['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S UTC')}    
        Sunrise Time:   {dt.datetime.utcfromtimestamp(response['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S UTC')}""")
    return summarized_response

print(get_weather_data("london"))


def convert_dateTime(local_dateTime,destination_Latitude,destination_Longitude):
  #Convert and display the date and time for the specified location
  city_timezone_str = TimezoneFinder().timezone_at(lng=int(response['coord']['lon']), lat=response['coord']['lat'])
  city_timezone = pytz.timezone(city_timezone_str)
  city_local_time = local_dateTime.astimezone(city_timezone)
  formatted_destination_datetime=city_local_time.strftime("%Y-%m-%d %H:%M:%S ")
  formatted_current_datetime=local_dateTime.strftime("%Y-%m-%d %H:%M:%S ")
  msg=(f"\nYour current date and time: {formatted_current_datetime}\nDate and time in {city}: {formatted_destination_datetime}")
  return msg

print(convert_dateTime((dt.datetime.now()),(response['coord']['lat']),(response['coord']['lon'])))



#Function to set default cities list

def set_Default_cities(cities_list,json_file,Celsius_Fahrenheit):
  # Store and manage default settings and multiple favorite locations using file I/O in JSON format.
  # the function is silence, creates the json file
  file_content=[]
  for default_city in cities_list:
    def_response= requests.get(f"{basic_url}appid={api_key}&q={default_city}").json()
    temp_unit=[f"{(def_response['main']['temp'])-273.15:.2f}C" if Celsius_Fahrenheit=="Celsius" else f"{((def_response['main']['temp'])-273.15)*1.8 + 32:.2f}F"]
    weather=(f" Weather description for {default_city}: {def_response['weather'][0]['description']}\n Humidity:       {def_response['main']['humidity']:}%\n Temperature:    {temp_unit[0]}\n Sunset Time:    {dt.datetime.utcfromtimestamp(def_response['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S UTC')}\n Sunrise Time:   {dt.datetime.utcfromtimestamp(def_response['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    city_weather={default_city:weather}
    file_content.append(city_weather)

  data_representation = json.dumps(file_content)
  with open(json_file,'w') as f:
        json.dump(data_representation, f)

#Example:

set_Default_cities((["london","New York","Jerusalem"]),('settings.json'),("Celsius"))


# After you set the default setting you can use this code under the city input line "city=input("your city")"
# and when no input is provided from the user , the weather for the default locations should be displayed.
# code name- "small code"
if city == '':
    result = json.loads(data_representation)
    for item in result:
        for a_city,desc in item.items():
            print(f"{a_city}\n{desc}\n\n\n")


#read the default settings
def read_settings_file(json_file):
  #function to read the default settings:
  with open(json_file,'r') as f:
    loaded_data={line for line in f }
  return loaded_data

print(read_settings_file('settings.json'))