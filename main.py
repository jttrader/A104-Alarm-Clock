# Importing required libraries
from datetime import datetime   #To set date and time
import webbrowser               #To play sound by webbrowser

def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please provide the correct time format..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please provide the correct HOUR format (01-12)..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please provide the correct MINUTE format (00-59..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please provide the correct SECOND format (00-59..."
        else:
            return "OK"

while True:
    alarm_time = input("Enter the time of alarm to be set: 'HH:MM:SS AM/PM' format: \n")

    validate = validate_time(alarm_time.lower())
    if validate != "OK":
        print(validate)
    else:
        print(f"Setting Alarm for {alarm_time}...")
        break

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")

    #Checking if the hour, minute and seconds will match the alarm set
    if alarm_period == current_period:
        if alarm_hour==current_hour:
            if alarm_minute==current_minute:
                if alarm_seconds==current_seconds:
                    print("Wake Up!")
                    webbrowser.open("chicken_alarm.mp3")
                    break