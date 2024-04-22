'''
Task 1: Identifying and Creating Classes

Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. 
Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, 
and user interaction.

Problem Statement:

The existing script for the weather forecast application is written in a procedural style and lacks organization.

Code Example:

Before Refactoring:
'''
# Example code and bellow is my code 


# def fetch_weather_data(city):
#     # Simulated function to fetch weather data for a given city
#     print(f"Fetching weather data for {city}...")
#     # Simulated data based on city
#     weather_data = {
#         "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
#         "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
#         "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
#     }
#     return weather_data.get(city, {})

# def parse_weather_data(data):
#     # Function to parse weather data
#     if not data:
#         return "Weather data not available"
#     city = data["city"]
#     temperature = data["temperature"]
#     condition = data["condition"]
#     humidity = data["humidity"]
#     return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

# def get_detailed_forecast(city):
#     # Function to provide a detailed weather forecast for a city
#     data = fetch_weather_data(city)
#     return parse_weather_data(data)

# def display_weather(city):
#     # Function to display the basic weather forecast for a city
#     data = fetch_weather_data(city)
#     if not data:
#         print(f"Weather data not available for {city}")
#     else:
#         weather_report = parse_weather_data(data)
#         print(weather_report)

# def main():
#     while True:
#         city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
#         if city.lower() == 'exit':
#             break
#         detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
#         if detailed == 'yes':
#             forecast = get_detailed_forecast(city)
#         else:
#             forecast = display_weather(city)
#         print(forecast)

# if __name__ == "__main__":
#     main()




class WeatherDataFetcher:
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
        return weather_data.get(city, {})


class WeatherDataParser:
    def parse_weather_data(self, data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city = data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"


class WeatherForecast:
    def __init__(self):
        self.fetcher = WeatherDataFetcher()
        self.parser = WeatherDataParser()

    def get_basic_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)


class UserInterface:
    def __init__(self):
        self.forecast = WeatherForecast()

    def display_weather(self, city, detailed=False):
        if detailed:
            return self.forecast.get_detailed_forecast(city)
        else:
            return self.forecast.get_basic_forecast(city)


def main():
    ui = UserInterface()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = ui.display_weather(city, detailed=True)
        else:
            forecast = ui.display_weather(city)
        print(forecast)


if __name__ == "__main__":
    main()

