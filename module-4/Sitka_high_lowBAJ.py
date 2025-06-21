import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

    #Instructions 
    while True: 
        print("Instructions: This graphs shows temperatures from high to low.")
        print("1. High Temps")
        print("2. Low Temps")
        print("3. Exit")
        options = input("Choose 1, 2 or 3: ")
        
        #high option 
        if options == "1":
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')
            ax.set_title("Daily High Temperatures - 2018", fontsize=20)
            ax.set_xlabel('', fontsize=12)
            fig.autofmt_xdate()
            ax.set_ylabel("Temperature (F)", fontsize=12)
            ax.tick_params(axis='both', labelsize=10)
            plt.show() 

        #Low Option 
        elif options == "2":
            fig, ax = plt.subplots()
            ax.plot(dates, lows, c='royalblue')
            ax.set_title("Daily Low Temperatures - 2018", fontsize=20)
            ax.set_xlabel('', fontsize=12)
            fig.autofmt_xdate()
            ax.set_ylabel("Temperature (F)", fontsize=12)
            ax.tick_params(axis='both', labelsize=10)
            plt.show()  

        elif options == "3":
            print("Thank you for using stika's weather app! ")
            exit()

