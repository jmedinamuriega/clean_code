
class WeatherFetcher:
    def __init__(self):
        self.data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }

    def fetch_weather_data(self, city):
        return self.data.get(city, {})


class WeatherParser:
    def parse_weather_data(self, city, data):
        if not data:
            return f"Weather data not available for {city}"
        return f"Weather in {city}: {data['temperature']} degrees, {data['condition']}, Humidity: {data['humidity']}%"


class WeatherDisplay:
    def __init__(self, fetcher, parser):
        self.fetcher = fetcher
        self.parser = parser

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(city, data)
            print(weather_report)