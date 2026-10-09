import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
def my_city(lat,log,name):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={log}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url)
    data = response.json()
    daily_data = data["daily"]

    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp':  daily_data['temperature_2m_max'],
        'min_temp':  daily_data['temperature_2m_min']
    })

    df['date']= pd.to_datetime(df["date"])

    print(df)

    #------------------------------


    # Create the plot
    plt.figure(figsize=(15, 8))
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temp')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('{} Weather - Past 7 Days'.format(name))
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=60)
    plt.tight_layout()

    # Save the plot
    plt.savefig('{} weather_chart.png'.format(name))
    plt.show()

    #------------data work-------------------

    # Create data folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Save to CSV
    df.to_csv('data/{}_weather.csv'.format(name), index=False)
    print("Data saved to data/{}_weather.csv".format(name))

my_city(17,78, "Hyderabad")