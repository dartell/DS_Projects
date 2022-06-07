# Final Project
#
# - You must allow the user to lookup weather by city and/or zip code
# - You must allow the user to do as many lookups as they want of weather data
# - Readability means that weather data must be nicely output and not in Kelvin unless the user asks for Kelvin.  I don't know anyone who actually reads Kelvin.
# - You must use the API to get Fahrenheit and/or Celsius.  Do not attempt to do a code level conversion.
# - You must have your own API key
# - You must have excellent and thorough comments
# - You must have very specific try blocks (don't include huge chunks of code in a single try block)
# - You must do a lot of validation.  Points will be deducted for any exceptions
# - You must follow PEP8 and other standards which have been discussed throughout the class (example single character variable names, lack of flexibility (asking for Y but not taking y as well).
# - You must have well defined welcome message and output.  Everything must be very clear.  Think about the experience you get when you go to weather
# - You will need to review the API documentation provided by OpenWeather to get full details on how to do things
# - You will need to use the GeoCode API to look up the information for the location the user selects https://openweathermap.org/api/geocoding-api then use this information to look up the weather you must use the Current Weather API https://openweathermap.org/current.  If you would prefer to do an hourly or extended forcast feel free but you MUST use the GeoCode API first
# - You must at a bare minimum show the user the following data.  Not displaying this data will result in a points reduction
#     - Current Weather Conditions For City name
#     - Current Temp:
#     - High Temp:
#     - Low Temp:
#     - Pressure:
#     - Humidity:
#     - Cloud Cover:

import requests
import json
import string


def unit_transformation(units):
    """Asks the user to select Imperial or Metric measurements.  If the user selects '1', they want imperial measurements such as fahrenheit.
     If the user selects '2', they want metric measurements such as celsius"""
    unit_conversion = 0

    while unit_conversion == 0:
        try:
            unit_conversion = int(input('Type 1 for fahrenheit and 2 for celsius' '\n'))
        except ValueError:
            print('Please enter "1" or "2"')
            unit_conversion = 0
            print(unit_conversion)

        if unit_conversion == 1:
            units = 'imperial'
        elif unit_conversion == 2:
            units = 'metric'
        else:
            print('Please enter "1" or "2"')
            unit_conversion = 0

    return units


def weather_lookup_zip():
    """ Asks for the zip code from the user to do a GET request.  The request looks up the zip code from the open weather API to bring the weather data into the program.
    The data is then cleaned up using the clean_up function. """
    url_zip_code = "https://api.openweathermap.org/data/2.5/weather"
    api_key = '91ed41f877888fb1e6a4f20e4838de4d'
    units = str()

    zip = str(input('Please enter zip code' '\n'))

    zip_payload = {'zip': zip, 'appid': api_key, 'units': unit_transformation(units)}
    try:
        zip_response = requests.request("GET", url_zip_code, params=zip_payload)
    except requests.exceptions.RequestException as e:
        print(e)
        print('Something bad happened.  Try checking your internet connection')
        print('Returning you to the main menu')
        main()

    zip_pretty = json.loads(zip_response.text)

    pretty = zip_pretty

    try:
        clean_up(pretty)
    except IndexError:
        print('That zip doesnt exist in the United States. Try again')
        weather_lookup_zip()


def weather_lookup_city():
    """ Asks for the city and state from the user to do a GET request.  The city, state, and United States country code
     are combined into one string called query.  The query variable is passed into the api payload which then uses a GET Request
     from the open weather API. This allows the weather data to be pulled for the city by using the latitude and longitude of the location.
       The latitude and longitude are parsed from the data and passed into another open weather api to provide the current forecast.
       The data is then cleaned up using the clean_up function."""
    url_city = 'http://api.openweathermap.org/geo/1.0/direct'
    api_key = '91ed41f877888fb1e6a4f20e4838de4d'
    units = str()
    city = str(input('Please enter city name. Example "Mary Esther"' '\n'))
    city = city + ','
    state = str(input('Please enter state name. Example "Florida"' '\n'))
    state = state + ','
    query = city + state + 'US'
    print('Your inputs are ' 'City:', city, 'State:', state,)

    city_payload = {'q': query, 'limit': '1', 'appid': api_key}
    try:
        city_response = requests.request("GET", url_city, params=city_payload)
    except requests.exceptions.RequestException as e:
        print(e)
        print('Something bad happened.  Try checking your internet connection')
        print('Returning you to the main menu')
        main()

    city_pretty = city_response.text
    city_string = city_pretty

    lat_codes = city_string.find("lat")
    lat_codes_end = lat_codes+13
    latitude = city_string[lat_codes+5: lat_codes_end]

    lon_codes = city_string.find("lon")
    lon_codes_end = lon_codes+13
    longitude = city_string[lon_codes+5: lon_codes_end]

    url_geo = 'https://api.openweathermap.org/data/2.5/weather'
    geo_code_payload = {'lat': latitude, 'lon': longitude, 'units': unit_transformation(units), 'lang': 'en',
                        'appid': '91ed41f877888fb1e6a4f20e4838de4d'}
    geo_code_response = requests.request("GET", url_geo, params=geo_code_payload)

    geo_pretty = json.loads(geo_code_response.text)

    pretty = geo_pretty

    try:
        clean_up(pretty)
    except IndexError:
        print('No results found, please re-enter your city and state.')
        weather_lookup_city()


def clean_up(pretty):
    """Cleans each significant weather item into one separate variable. Removes various characters and punctuations.
      Passes the results into the pretty_print function"""
    city_name = str(pretty.get('name'))

    weather_conditions = str(pretty.get('weather'))
    weather_conditions = weather_conditions.replace('main', '')
    weather_conditions = weather_conditions.replace('description', '')
    weather_conditions = weather_conditions.replace("'", "")
    weather_conditions = weather_conditions.strip()
    weather_conditions = weather_conditions.replace(':', '')
    weather_conditions = weather_conditions.split(',')

    conditions = weather_conditions[1]
    clouds = weather_conditions[2]

    temperature = str(pretty.get('main'))
    temperature = temperature.strip(string.punctuation)
    temperature = temperature.replace('feels_like', '')
    temperature = temperature.replace('temp', '')
    temperature = temperature.replace('_', '')
    temperature = temperature.replace(':', '')
    temperature = temperature.replace("'", '')
    temperature = temperature.replace('min', '')
    temperature = temperature.replace('max', '')
    temperature = temperature.replace('pressure', '')
    temperature = temperature.replace('humidity', '')
    temperature = temperature.strip()
    temperature = temperature.split(',')

    current_temperature = temperature[0]
    feels_like_temperature = temperature[1]
    min_temperature = temperature[2]
    max_temperature = temperature[3]
    pressure = temperature[4]
    humidity = temperature[5]

    pretty_print_weather(city_name, conditions, clouds, current_temperature, feels_like_temperature, min_temperature, max_temperature, pressure, humidity)


def pretty_print_weather(city_name, conditions, clouds, current_temperature, feels_like_temperature, min_temperature,
                         max_temperature, pressure, humidity):
    """Prints the weather data in a clean,readable format.  Strips the whitespaces from each variable and prints the output
    in a summary view as well as in a weather forecast view"""
    header = 'Overview Forecast'
    print(header)
    print ('__________________________')
    city_name = city_name.strip()
    conditions = conditions.strip()
    clouds = clouds.strip()
    current_temperature = current_temperature.strip()
    feels_like_temperature = feels_like_temperature.strip()
    min_temperature = min_temperature.strip()
    max_temperature = max_temperature.strip()
    pressure = pressure.strip()
    humidity = humidity.strip()

    print(
          'City: ', city_name.format(), '\n'
          'Conditions:', conditions, '\n'
          'Clouds:', clouds, '\n'
          'Current Temperature:', current_temperature, '\n'
          'Feels Like:', feels_like_temperature, '\n'
          'Low:', min_temperature, '\n'
          'High:', max_temperature,'\n'
          'Pressure:', pressure, '\n'
          'Humidity:', humidity, )
    print(' Weather Forecast: The current weather conditions in', city_name, 'are', conditions,
          '. The current temperature is', current_temperature, 'with a high of', max_temperature, 'and a low of',
          min_temperature, '. It feels like', feels_like_temperature, 'with a humidity of', humidity, '. ' 'Pressure of',
          pressure, '. The sky is showing', clouds)


def main():
    """ Insert function documentation here:"""
    user_input = 0
    while user_input == 0:
        print('Welcome to United States weather lookup program.  You can look up weather in your city by name or zipcode.')
        try:
            user_input = int((input('1.) Enter "1" to lookup weather by zip code' '\n'
                                    '2.) Enter "2" to lookup weather by city and state' '\n'
                                    '3.) Enter "3" to close the program' '\n')))
        except ValueError:
            print('Please enter "1", "2", or "3"')
            main()
        if user_input == 1:
            print('Thank you.  You chose the zip code option.')
            weather_lookup_zip()
        elif user_input == 2:
            print('Thank you.  You chose the city option')
            weather_lookup_city()
        elif user_input == 3:
            print('Closing Program.')
            exit()
            break
        else:
            print('Please enter "1", "2", or "3"')
            main()
        if user_input == 1 or user_input == 2:
            try:
                user_input = int(input('If you would like to look up another location press "0", otherwise enter another number' '\n'))
            except ValueError:
                print('You did not enter a number.  Bringing you back to the main menu to give you more time to decide')
                main()
            if user_input == 0:
                print('Returning you to the main menu')
                main()
            else:
                user_input = -1
                break
    print('Closing Program')


if __name__ == "__main__":
    main()

# Change#:1
# Change(s) Made: Initial file that uses the Open Weather API to pull weather data based on zip code or city and state
# Date of Change: 6/4/2022
# Author: Darius Dinkins
# Change Approved by: Darius Dinkins
# Date Moved to Production: 6/4/2022
