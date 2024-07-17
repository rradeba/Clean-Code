# Weather Forecast Application Script


class WeatherDataFetcher:
    def __init__(self, weather_city, weather_data):
        self.weather_data = weather_data
        self.weather_city = weather_city 
    def pull_city_data(self): 
        return self.weather_data.get(self.weather_city, {})
    
               
class DataParser:
    def __init__(self, fetch_weather_data):
        self.fetch_weather_data = fetch_weather_data 
    
    def parse_city_data(self):
        city_data_list = []  
        if not self.fetch_weather_data:
            return "Weather data not available"
        else:
            parsed_city = self.fetch_weather_data["city"]
            city_data_list.append(parsed_city)
            parsed_temperature = self.fetch_weather_data["temperature"]
            city_data_list.append(parsed_temperature)
            parsed_condition = self.fetch_weather_data["condition"]
            city_data_list.append(parsed_condition)
            parsed_humidity = self.fetch_weather_data["humidity"]
            city_data_list.append(parsed_humidity)
        return city_data_list

        
class UserInterface:
    def __init__(self):
        weather_interface_selections = []
        weather_city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        weather_interface_selections.append =  weather_city 
        detailed_report_inquiry = input("Do you want a detailed forecast? (yes/no): ").lower()
        weather_interface_selections.append = detailed_report_inquiry
        return weather_interface_selections
            

class ValidateUserSelections: 
    def __init__(self, weather_interface_selections, weather_data):
        self.weather_interface_selections = weather_interface_selections
        self.weather_data = weather_data
        for city_index in self.weather_interface_selections:
            if city_index != self.weather_interface_selections[0]: 
                return "City not included in report."
            elif self.weather_interface_selections[1] != "y" or self.weather_interface_selections[1] != "n":
                return "Please type 'y' or 'n'."
            

class PrintWeatherData: 
    def __init__(self, weather_length, parsed_weather_data): 
        self.parsed_weather_data = parsed_weather_data
        self.weather_length  = weather_length
    def print_short_long_weather(self): 
        if self.weather_length == 'y':
            return f"Weather in {self.parsed_weather_data[0]}: {self.parsed_weather_data[1]} degrees, {self.parsed_weather_data[2]}, Humidity: {self.parsed_weather_data[3]}"
        else: 
            return  f"Weather in {self.parsed_weather_data[0]} is {self.parsed_weather_data[2]}"
        
            

weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }



weather_interface_selections = UserInterface()

validated_user_selections = ValidateUserSelections(weather_interface_selections, weather_data)

print(validated_user_selections)

fetch_weather_data = WeatherDataFetcher(weather_interface_selections[0],weather_data)

parsed_weather_data = DataParser()

printed_weather_data  = PrintWeatherData(weather_interface_selections[1], parsed_weather_data)

print(printed_weather_data)











