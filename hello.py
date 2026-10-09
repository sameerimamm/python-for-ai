import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude={}&hourly=temperature_2m".format(77.23)
)


weather = response.json()
hourly_data = weather["hourly"]["temperature_2m"]
hour_count =0
day_count = 1
print(f"Day {day_count}:-------------------------")
for i, j in enumerate(hourly_data):
    if (hour_count+1)%24== 0:
        day_count += 1
        hour_count = 0
        print(f"Day {day_count}:")
    hour_count +=1
    print(f"Hour {hour_count}: Temperature {j}°C")
