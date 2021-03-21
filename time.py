import datetime
from time import sleep
celebs = ["La Fête de la Vertu", "La Fête du Génie", "La Fête du Travail", "La Fête de l'Opinion", "La Fête des Récompenses", "La Fête de la Révolution"]
weeks = ["primidi", "duodi", "tridi", "quartidi", "qunitidi", "sextidi", "nonidi", "décadi"]
months = ["Vendémiaire", "Brumaire", "Frimaire", "Nivôse", "Pluviôse", "Ventôse", "Germinal", "Floréal", "Prarial", "Messidor", "Thermidor", "Fructidor"]

last = ""
if datetime.datetime.now().month > 8 and datetime.datetime.now().day > 21:
    d1 = datetime.date(datetime.datetime.now().year, 9, 22)
    d0 = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    year = datetime.datetime.now().year - 1793
else:
    d1 = datetime.date(datetime.datetime.now().year - 1, 9, 22)
    d0 = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    year = datetime.datetime.now().year - 1792

date = (d0 - d1).days

while True:
    second = datetime.datetime.now().second
    minute = datetime.datetime.now().minute
    hour = datetime.datetime.now().hour

    month = (date // 30) + 1
    day = (date % 30) + 1
    weekday = int(str(day)[-1])
    if date > 359:
        month = "-"
        day = celebs[day - 1]

    current = str((second + (minute * 60) + (hour * 60 * 60)) / 0.864)
    if last != current and date < 360:
        print("0" + current[0], ":", current[1:3], ":", current[3:5], "on the" , day, weeks[weekday - 1], months[month - 1], year)
        last = current
    elif date > 359:
        print("0" + current[0], ":", current[1:3], ":", current[3:5], "on" , day, year)
        last = current

    sleep(0.4)
