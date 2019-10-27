import pyowm
from datetime import datetime
import datetime

monday_reminders = []
tuesday_reminders = []
wednesday_reminders = []
thursday_reminders = []
friday_reminders = []
saturday_reminders = []
sunday_reminders = []
command_continue = True

def get_weather():
    owm = pyowm.OWM("653ae96c89b55a1cccf01e7243d6b94b")
    location = owm.weather_at_place("Toronto")
    weather = location.get_weather()
    temp = weather.get_temperature("celsius")
    print("The temperature is currently " + str(int(temp["temp"])) + " degrees celsius, with a high of " + str(int(temp["temp_max"])) + " and a low of " + str(int(temp["temp_min"])) + " degrees celsius.")

def get_date():
    date = str(datetime.date(datetime.now()))
    year = date[:4]
    day = date[-2:]
    month = date[5:7]
    if month == "01":
        month = "January"
    elif month == "02":
        month = "February"
    elif month == "03":
        month = "March"
    elif month == "04":
        month = "April"
    elif month == "05":
        month = "May"
    elif month == "06":
        month = "June"
    elif month == "07":
        month = "July"
    elif month == "08":
        month = "August"
    elif month == "09":
        month = "September"
    elif month == "10":
        month = "October"
    elif month == "11":
        month = "November"
    else:
        month = "December"
    if day in ["1", "21", "31"]:
        day_sub = "st"
    elif day in ["2", "22"]:
        day_sub = "nd"
    elif day in ["3", "23"]:
        day_sub = "rd"
    else:
        day_sub = "th"
    print("The date is the " + day + day_sub + " of " + month + ", " + year + ".")

def make_reminder():
    command = input("What reminder would you like me to set?: ")
    if command[3:9] == "Monday":
        monday_reminders.append(command[23:])
        print("Will remind you to " + monday_reminders[-1] + " on Monday.")
    elif command[3:10] == "Tuesday":
        tuesday_reminders.append(command[24:])
        print("Will remind you to " + tuesday_reminders[-1] + " on Tuesday.")
    elif command[3:12] == "Wednesday":
        wednesday_reminders.append(command[26:])
        print("Will remind you to " + wednesday_reminders[-1] + " on Wednesday.")
    elif command[3:11] == "Thursday":
        thursday_reminders.append(command[25:])
        print("Will remind you to " + thursday_reminders[-1] + " on Thursday.")
    elif command[3:9] == "Friday":
        friday_reminders.append(command[23:])
        print("Will remind you to " + friday_reminders[-1] + " on Friday.")
    elif command[3:11] == "Saturday":
        saturday_reminders.append(command[25:])
        print("Will remind you to " + saturday_reminders[-1] + " on Saturday.")
    elif command[3:9] == "Sunday":
        sunday_reminders.append(command[23:])
        print("Will remind you to " + sunday_reminders[-1] + " on Sunday.")

def show_reminders_today():
    day_of_the_week = datetime.date.today().strftime("%A")
    if day_of_the_week == "Monday":
        for task in monday_reminders:
            print(task)
    elif day_of_the_week == "Tuesday":
        for task in tuesday_reminders:
            print(task)
    elif day_of_the_week == "Wednesday":
        for task in wednesday_reminders:
            print(task)
    elif day_of_the_week == "Thursday":
        for task in thursday_reminders:
            print(task)
    elif day_of_the_week == "Friday":
        for task in friday_reminders:
            print(task)
    elif day_of_the_week == "Saturday":
        for task in saturday_reminders:
            print(task)
    else:
        for task in sunday_reminders:
            print(sunday_reminders)

def show_reminders_date():
    if "Monday" in command:
        for task in monday_reminders:
            print(task)
    elif "Tuesday" in command:
        for task in tuesday_reminders:
            print(task)
    elif "Wednesday" in command:
        for task in wednesday_reminders:
            print(task)
    elif "Thursday" in command:
        for task in thursday_reminders:
            print(task)
    elif "Friday" in command:
        for task in friday_reminders:
            print(task)
    elif "Saturday" in command:
        for task in saturday_reminders:
            print(task)
    elif "Sunday" in command:
        for task in sunday_reminders:
            print(sunday_reminders)

while True:
    command = input()
    if command == "end":
        break
    elif command == "How is the weather?":
        get_weather()
        continue
    elif command == "What is the date?":
        get_date()
        continue
    elif command == "Set a reminder":
        make_reminder()
        continue
    elif command == "Show me my reminders for today":
        show_reminders_today()
        continue
    elif "Show me my reminders for" in command:
        show_reminders_date()
        continue
    else:
        print("Put in a valid command.")
        continue