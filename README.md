# weather_project

Weather Forest is a Python project that allows you to fetch and display weather data for any specified location.

The project contains a Streamlit weather app allows users to enter a city and view its weather details. It uses the OpenWeatherMap API to fetch real-time weather information.
## Table of Contents
- [Project Overview](#project-overview)
- [Project Setup](#project-setup)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Project Overview

The Weather Forest project is designed to provide users with accurate and up-to-date weather information for a specified location. 
The project utilizes Python and leverages a weather API to fetch real-time weather data.

## Project Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.x)
- Pip (Python package installer)

### API Key Setup

To fetch weather data, you need to create an API key from a weather data provider. Follow these steps:

1. Visit the [Weather Data Provider](https://openweathermap.org/) website.
2. Sign up for an account and create an API key.
3. Copy the API key.

4. Replace `api_key` with the API key you obtained.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Anael22/weather_project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather_project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use Weather Forest, follow these steps:

1. Enter the location for which you want to fetch the weather data when prompted.

2. Run the main script:

    ```bash
    python main.py
    ``` 

3. View the weather information displayed on the console.

4. use the functions:

- **convert_dateTime(local_dateTime, destination_Latitude, destination_Longitude)**

This function takes the local date and time of the user, as well as the latitude and longitude of the specified weather location, and converts the date and time considering time zone differences.
set_Default_cities(cities_list, json_file, Celsius_Fahrenheit)
This function allows the user to set default cities and preferences. It takes a list of cities, the path to the settings JSON file, and a preference flag (Celsius or Fahrenheit).

Example usage:
convert_dateTime((dt.datetime.now()),(response['coord']['lat']),(response['coord']['lon'])


- **set_Default_cities(cities_list, json_file, Celsius_Fahrenheit)**
This function allows the user to set default cities and preferences. It takes a list of cities, the path to the settings JSON file, and a preference flag (Celsius or Fahrenheit).
After you set the default setting you can copy the "small code" and paste under the city input line "city=input("your city")"
and when no input is provided from the user , the weather for the default locations should be displayed.

Example usage:
set_Default_cities(['New York', 'london'], 'settings.json', 'Celsius')


- **read_settings_file(json_file)**
This function reads and retrieves the settings from the specified JSON file.

Example usage:
settings = read_settings_file('settings.json')

To Use streamlit app run

   
 ```bash
   streamlit run app.py
   ``` 
or access thr url-

 ```bash
https://weatherdataforyou.streamlit.app/
   ``` 

## Default Settings and Favorites

Weather Forest allows users to set default preferences and manage multiple favorite locations. 
These settings are stored persistently using file I/O in JSON format. 
To manage these settings:

- use the function set_Default_cities
- manage the list "cities_list" by adding or removing a default city.  

## Dependencies

The project relies on the following Python libraries, :

- **requests**: This library is used for making HTTP requests to the weather API.

- **timezonefinder**: This library is employed to determine the timezone of a specific location, enabling accurate conversion of local and destination times.

- **datetime (as dt)**: This standard library is used for handling date and time operations. In the project, it is used to work with the local and destination date and time.

- **pytz**: This library is used to work with time zones and localize the date and time information appropriately.

- **json**: This standard library is used to work with JSON data. In the project, it is used for reading and writing settings in JSON format.


you can  install the following libraries using the `pip install -r requirements.txt` command:

- requests==2.31.0
- timezonefinder==6.2.0
- pytz==2023.3.post1
- streamlit==1.29.0

The json and datetime libraries are not necessary because they are part of the Python standard library, and you don't need to install them separately.