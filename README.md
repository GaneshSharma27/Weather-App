## Summary
Weather App based on Python language completely.
This app doesn't use any User Interface (UI) it uses simple Command Line Interface (CLI). For providing weather data we use OpenWeatherMap's API to fetch the data.

## How it works
First, I imported requests and JSON modules, requests module for API requests and JSON module for JSON parsing, then defined a function named "get_weather(city_name)" which takes "city_name" as function parameter. In "get_weather()" function I wrote base_url, all the API requests to the API will use the same base_url to fetch data. Then I defined a dictionary named "params".
This dictionary contains key and its values
#### Key and its values:
1. 'q' key is associated with whatever the value is stored into the variable "city_name".
2. 'appid' key asociates to the value stored in "API_KEY" variable, this variable contains API Key that'll be used to fetch data.
3. 'units' key associates to the string value 'metrics', indicating that metrics should be used.
   Although you can change units of temperature (here 'metrics' means temperature is in "celcius", if you want it in "fahrenheit" use 'imperial' in place of 'metrics')
Then I declared a variable "response" which stores the response from "requests.get()". This variable contains all the information about the server's response, including the response text, status code, and headers in the form of JSON file.
Now, using conditionals I check if the "response.status code == 200" if yes then initialize variable "data" with "response.json()" this function is used to parse the response and store it in form of lists/dictionaries (here it is stored in dictionary) which was stored into the "response" variable. The work of "json()" is that it makes the data more accessible and easier for further use. Then in if-block itself after all the parsing is done then "get_weather()" returns "data". Else, it returns "None" (which is nothing)

### Now, in main() block
First user input is made in "city_name" variable. Then another "weather_data" variable is initialized with "get_weather(city_name)".

#### The image below shows how response is stored in the form of dictionary after parsing the JSON response.
![alt text](https://github.com/GaneshSharma27/Weather-App/blob/main/response_output.png?raw=true)

Then using conditionals, if "weather_data()" returns "data" then the information is extracted and stored in variables.
Then all these variables are printed.
Else, "City not found" is printed.
