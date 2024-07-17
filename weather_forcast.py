# Weather Forecast Application Script
import sys 

# class to fetch the weather data for the individual city from the list given later in the code 
class WeatherDataFetcher:
    def __init__(self, weather_city, weather_data):
        self.weather_data = weather_data
        self.weather_city = weather_city 
    def pull_city_data(self): 
        return self.weather_data.get(self.weather_city, {})
    
#class wich recieves instance citydata and parses it into a list that can be manipulated            
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

#prints the questions for the user and then stores them in a list that can be used later on 
class UserInterface:
    def get_user_input(self):
            weather_interface_selections = []
            weather_city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            weather_interface_selections.append(weather_city)
            if weather_city.lower() == "exit":
                sys.exit() 
            detailed_report_inquiry = input("Do you want a detailed forecast? (yes/no): ").lower()
            weather_interface_selections.append(detailed_report_inquiry)
            return weather_interface_selections
                
# class that vaidates the objects from the user interface and returns error messages 
class ValidateUserSelections: 
    def __init__(self, weather_interface_selections, weather_data):
        self.weather_interface_selections = weather_interface_selections
        self.weather_data = weather_data
        
    def validate(self):
        city = self.weather_interface_selections[0]
        if city not in self.weather_data: 
            return "City not included in report."
        detailed_report_inquiry = self.weather_interface_selections[1]
        if detailed_report_inquiry not in ["yes", "no"]:
            return "Please type 'yes' or 'no'."
        
        return None
            
# class receives the validated and parsed data from the user selection and then prints it out in a readable format
class PrintWeatherData: 
    def __init__(self, weather_length, parsed_weather_data): 
        self.parsed_weather_data = parsed_weather_data
        self.weather_length  = weather_length
    def print_short_long_weather(self): 
        if self.weather_length == 'yes':
            return f"Weather in {self.parsed_weather_data[0]}: {self.parsed_weather_data[1]} degrees, {self.parsed_weather_data[2]}, Humidity: {self.parsed_weather_data[3]}"
        else: 
            return  f"Weather in {self.parsed_weather_data[0]} is {self.parsed_weather_data[2]}"
        
            
# data for the weather from each city 
weather_data = {
        "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
        "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
        "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
    }


# calling the classes in an order that allows the code to work correctly 
weather_interface_selection = UserInterface()
weather_interface_selection = weather_interface_selection.get_user_input()

validator = ValidateUserSelections(weather_interface_selection, weather_data)
validation_message = validator.validate()
if validation_message:
    print(validation_message)
    sys.exit()

fetcher = WeatherDataFetcher(weather_interface_selection[0], weather_data)
city_weather_data = fetcher.pull_city_data()

parser = DataParser(city_weather_data)
parsed_weather_data = parser.parse_city_data()


printed_weather_data  = PrintWeatherData(weather_interface_selection[1], parsed_weather_data)

printer = PrintWeatherData(weather_interface_selection[1], parsed_weather_data)
print(printer.print_short_long_weather())











