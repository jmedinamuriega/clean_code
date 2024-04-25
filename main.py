from clean_code2 import WeatherFetcher,WeatherParser,WeatherDisplay  

def main():
    fetcher = WeatherFetcher()
    parser = WeatherParser()
    display = WeatherDisplay(fetcher, parser)

    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            display.display_weather(city)
        else:
            display.display_weather(city)

if __name__ == "__main__":
    main()