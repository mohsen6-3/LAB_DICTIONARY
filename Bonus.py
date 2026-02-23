weather_date = {}
def input_weather_data():
    city_input = input("Enter the name of a city: ")
    date_input = input("Enter a date (YYYY-MM-DD): ")
    temperature_input = input("Enter the temperature : ")
    humidity_input = input("Enter the humidity percentage: ")
    weather_condition_input = input("Enter the weather condition (sunny, rainy, cloudy): ")

    if city_input not in weather_date:
        weather_date[city_input] = {}

    weather_date[city_input][date_input] = {
        "temperature": temperature_input+"°C",
        "humidity": humidity_input+" %",
        "weather_condition": weather_condition_input
    }
    print(f"Weather data for {city_input} has been added.")
def search_weather_data():
    search_city = input("Enter the name of a city to retrieve weather information: ")
    if search_city in weather_date:
        print("-" * 25)
        print(f'Weather information for {search_city} :')
        for date_input, value in weather_date[search_city].items():
            print(f"Date: {date_input}")
            for key, value in value.items():
                print(f"{key}: {value}")

        print("-" * 25)
    else:
        print(f"No weather data found for {search_city}.")
    
    
def update_weather_data():
    city_to_update = input("Enter the name of the city to update its weather data: ")
    date_to_update = input("Enter the date of the weather data to update (YYYY-MM-DD): ")
    if city_to_update in weather_date and date_to_update in weather_date[city_to_update]:
        print("-" * 25)
        print(f"Current weather data for {city_to_update}:")
        for key, value in weather_date[city_to_update][date_to_update].items():
            print(f"{key}: {value}")
        print("-" * 25)
        print("Enter new weather data")
        new_temperature_input = input("Enter a new temperature: ")
        new_humidity_input = input("Enter a new humidity percentage: ")
        new_weather_condition_input = input("Enter a new weather condition (sunny, rainy, cloudy): ")

        weather_date[city_to_update][date_to_update] = {
            "temperature": new_temperature_input+"°C",
            "humidity": new_humidity_input+" %",
            "weather_condition": new_weather_condition_input
        }
        print(f"Weather data for {city_to_update} has been updated.")
    else:
        print(f"No weather data found for {city_to_update}.")
def delete_weather_data():
    city_to_delete = input("Enter the name of the city to delete its weather data: ")
    date_to_delete = input("Enter the date of the weather data to delete (YYYY-MM-DD): ")

    if city_to_delete in weather_date and date_to_delete in weather_date[city_to_delete]:
        del weather_date[city_to_delete]
        print(f"Weather data for {city_to_delete} has been deleted.")
    else:
        print(f"No weather data found for {city_to_delete}.")

while True:
    print("-" * 25)
    print("Options:")
    print("1. Add weather data")
    print("2. Search weather data")
    print("3. Update weather data")
    print("4. Delete weather data")
    print("5. Exit")
    print("-" * 25)
    choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

    if choice == '1':
        input_weather_data()
    elif choice == '2':
        search_weather_data()
    elif choice == '3':
        update_weather_data()
    elif choice == '4':
        delete_weather_data()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break

