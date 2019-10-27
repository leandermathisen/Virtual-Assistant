

command = input( )

if command == "How is the weather?":
    import pyowm
    owm = pyowm.OWM("653ae96c89b55a1cccf01e7243d6b94b")
    location = owm.weather_at_place("Toronto")
    weather = location.get_weather()
    temp = weather.get_temperature("celsius")
    print("The temperature is currently " + str(int(temp["temp"])) + " degrees celsius, with a high of " + str(int(temp["temp_max"])) + " and a low of " + str(int(temp["temp_min"])) + " degrees celsius.")
elif command == "What is the date?":
    from datetime import datetime
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