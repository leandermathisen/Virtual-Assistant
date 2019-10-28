import pyowm
from datetime import datetime, date
import calendar
import time
import speech_recognition as sr

r = sr.Recognizer()
monday_reminders = []
tuesday_reminders = []
wednesday_reminders = []
thursday_reminders = []
friday_reminders = []
saturday_reminders = []
sunday_reminders = []
print(int("one"))
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
    with sr.Microphone() as source:
        print("What reminder would you like me to set?: ")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
    except:
        print("Could not recognize your voice")
    if command[3:9] == "monday":
        monday_reminders.append(command[23:])
        print("Will remind you to " + monday_reminders[-1] + " on Monday.")
    elif command[3:10] == "tuesday":
        tuesday_reminders.append(command[24:])
        print("Will remind you to " + tuesday_reminders[-1] + " on Tuesday.")
    elif command[3:12] == "wednesday":
        wednesday_reminders.append(command[26:])
        print("Will remind you to " + wednesday_reminders[-1] + " on Wednesday.")
    elif command[3:11] == "thursday":
        thursday_reminders.append(command[25:])
        print("Will remind you to " + thursday_reminders[-1] + " on Thursday.")
    elif command[3:9] == "friday":
        friday_reminders.append(command[23:])
        print("Will remind you to " + friday_reminders[-1] + " on Friday.")
    elif command[3:11] == "saturday":
        saturday_reminders.append(command[25:])
        print("Will remind you to " + saturday_reminders[-1] + " on Saturday.")
    elif command[3:9] == "sunday":
        sunday_reminders.append(command[23:])
        print("Will remind you to " + sunday_reminders[-1] + " on Sunday.")

def show_reminders_today():
    my_date = date.today()
    day_of_the_week = calendar.day_name[my_date.weekday()]
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
    if "monday" in command:
        for task in monday_reminders:
            print(task)
    elif "tuesday" in command:
        for task in tuesday_reminders:
            print(task)
    elif "wednesday" in command:
        for task in wednesday_reminders:
            print(task)
    elif "thursday" in command:
        for task in thursday_reminders:
            print(task)
    elif "friday" in command:
        for task in friday_reminders:
            print(task)
    elif "saturday" in command:
        for task in saturday_reminders:
            print(task)
    elif "sunday" in command:
        for task in sunday_reminders:
            print(sunday_reminders)

def remove_task():
    task_number = 0
    with sr.Microphone() as source:
        print("On what day would you like me to remove the task for: ")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
    except:
        print("Could not recognize your voice")
    if command == "monday":
        for task in monday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(monday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Monday.")
            monday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Monday reminders.")
    elif command == "tuesday":
        for task in tuesday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(tuesday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Tuesday.")
            tuesday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Tuesday reminders.")
    elif command == "wednesday":
        for task in wednesday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(wednesday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Wednesday.")
            wednesday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Wednesday reminders.")
    elif command == "thursday":
        for task in thursday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(thursday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Thursday.")
            thursday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Thursday reminders.")
    elif command == "friday":
        for task in friday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(friday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Friday.")
            friday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Friday reminders.")
    elif command == "saturday":
        for task in saturday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(saturday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Saturday.")
            saturday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Saturday reminders.")
    elif command == "sunday":
        for task in sunday_reminders:
            task_number = task_number + 1
            print(str(task_number) + ") " + task)
        with sr.Microphone() as source:
            print("Which task would you like to remove: ")
            audio = r.listen(source)
        try:
            task_deleted = r.recognize_google(audio)
        except:
            print("Could not recognize your voice")
        if len(sunday_reminders) >= int(task_deleted):
            print("I have removed task " + task_deleted + " from your reminders on Sunday.")
            sunday_reminders.pop(int(task_deleted) - 1)
        else:
            print("That task is not in range of Sunday reminders.")
    else:
        print("Not in range of the days of the week.")

todays_date = date.today()
current_date = calendar.day_name[todays_date.weekday()]

while True:
    todays_date = date.today()
    if current_date != calendar.day_name[todays_date.weekday()]:
            print("Here are your reminders for today:")
            show_reminders_today()
            current_date = calendar.day_name[todays_date.weekday()]
    with sr.Microphone() as source:
        print("Say your command: ")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
    except:
        print("Could not recognize your voice")
    if command == "end":
        break
    elif command == "how is the weather":
        get_weather()
        continue
    elif command == "what is the date":
        get_date()
        continue
    elif command == "set a reminder":
        make_reminder()
        continue
    elif command == "show me my reminders for today":
        show_reminders_today()
        continue
    elif "Show me my reminders for" in command:
        show_reminders_date()
        continue
    elif "remove task" in command:
        remove_task()
        continue
    else:
        print("Enter a valid command.")
        continue