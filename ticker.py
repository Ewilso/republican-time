from time import sleep

days = ["primidi","duodi","tridi","quartidi","quintidi","sextidi","septidi","octidi","nonidi","décadi"]
months = ["Vendémiaire", "Brumaire", "Frimaire", "Nivôse", "Pluviôse", "Ventôse", "Germinal", "Floréal", "Prairial", "Messidor", "Thermidor", "Fructidor"]

second = 0
minute = 27
hour = 9
day = 30
month = 6
year = 229

while (True):
#for i in range(0,1):
    print(day, days[(day // 3) - 1], month, months[month - 1], year, "@", hour, ":", minute, ":", second)
    sleep(0.8295)
    second += 1
    if second == 100:
        second = 0
        minute += 1
    if minute == 100:
        minute = 0
        hour += 1
    if hour == 10:
        hour = 0
        day += 1
    if day == 31:
        day = 0
        month += 1
    if month == 12 and day == 5:
        month = 0
        day = 0
        year += 1
