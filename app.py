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
if st.button("Get Weather"):
    if city:
        # Fetch weather data


        if response["cod"] == "404":
            st.error("City not found. Please enter a valid city name.")
        else:
            # Display weather information
            st.subheader(f"Weather information for {city}:")
            st.write(f"Temperature:    {(response['main']['temp'])-273.15:.2f}C/{((response['main']['temp'])-273.15)*1.8 + 32:.2f}F ")
            st.write(f"Humidity: {response['main']['humidity']}%")
            st.write(f"Wind Speed: {response['wind']['speed']} m/s")
            st.write(f" Sunset Time: {dt.datetime.utcfromtimestamp(response['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S UTC')}")
            st.write(f" Sunrise Time:   {dt.datetime.utcfromtimestamp(response['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S UTC')}")


            def convert_dateTime(local_dateTime, destination_Latitude, destination_Longitude):
                # Convert and display the date and time for the specified location
                city_timezone_str = TimezoneFinder().timezone_at(lng=int(response['coord']['lon']),
                                                                 lat=response['coord']['lat'])
                city_timezone = pytz.timezone(city_timezone_str)
                city_local_time = local_dateTime.astimezone(city_timezone)
                formatted_destination_datetime = city_local_time.strftime("%Y-%m-%d %H:%M:%S ")
                formatted_current_datetime = local_dateTime.strftime("%Y-%m-%d %H:%M:%S ")
                msg = (
                    f"\nYour current date and time: {formatted_current_datetime}\nDate and time in {city}: {formatted_destination_datetime}")
                return msg


            st.write(convert_dateTime((dt.datetime.now()), (response['coord']['lat']), (response['coord']['lon'])))


    else:
        with open('settings.json', 'r') as file:
            json_string = file.read()

        print(json_string)
def set_Default_cities(cities_list, json_file, Celsius_Fahrenheit):
    file_content = []
    for default_city in cities_list:
        def_response = requests.get(f"{basic_url}appid={api_key}&q={default_city}").json()
        temp_unit = [
            f"{(def_response['main']['temp']) - 273.15:.2f}C" if Celsius_Fahrenheit == "C" else
            f"{((def_response['main']['temp']) - 273.15) * 1.8 + 32:.2f}F"
        ]
        weather = (
            f" Weather description for {default_city}: {def_response['weather'][0]['description']}\n "
            f"Humidity:       {def_response['main']['humidity']}%\n "
            f"Temperature:    {temp_unit[0]}\n "
            f"Sunset Time:    {dt.datetime.utcfromtimestamp(def_response['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S UTC')}\n "
            f"Sunrise Time:   {dt.datetime.utcfromtimestamp(def_response['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S UTC')}"
        )
        city_weather = {default_city: weather}
        file_content.append(city_weather)

    data_representation = json.dumps(file_content)
    with open(json_file, 'w') as f:
        json.dump(data_representation, f)

def main():
    st.subheader("Please write a default cities list ")

    # Create two columns to display inputs side by side
    col1, col2 = st.columns(2)
    with col1:
        cities_list = st.text_input("Enter cities (comma-separated):")
    with col2:
        unit = genre = st.radio("Preferred Temperature Unit", ["C", "F"])

    # Display the user inputs
    st.write(f"Cities List: {cities_list}")
    st.write(f"Preferred Temperature Unit: {unit}")

    # Button to save settings
    if st.button("Save"):
        set_Default_cities(cities_list, "settings1.json", str(unit))

if __name__ == "__main__":
    main()