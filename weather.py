import requests

# 🔑 Your OpenWeatherMap API Key
API_KEY = "ced08fbc9f3ef50f60e2cec752593428"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # ❌ Error handling
        if response.status_code != 200:
            print("\n❌ Error:", data.get("message", "Something went wrong"))
            return

        # 🌍 Extract data
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        # 📊 Output
        print("\n==============================")
        print("🌦️ WEATHER REPORT")
        print("==============================")
        print(f"📍 Location  : {city_name}, {country}")
        print(f"🌡️ Temp      : {temp} °C")
        print(f"💧 Humidity  : {humidity}%")
        print(f"☁️ Condition : {condition.capitalize()}")
        print("==============================\n")

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error:", e)
    except Exception as e:
        print("⚠️ Error:", e)


def main():
    print("=================================")
    print("🌦️ CLI WEATHER APP")
    print("Type 'exit' to quit")
    print("=================================")

    while True:
        city = input("\nEnter city name or ZIP code: ")

        if city.lower() == "exit":
            print("👋 Goodbye!")
            break

        if city.strip() == "":
            print("⚠️ Please enter a valid city")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()
