import datetime

celsius_temperatures = [20, 22, 25, 27, 30, 33]
feh_temperatures = list(map(lambda c: (c*9/5) + 32, celsius_temperatures))
print(list(filter(lambda x: x > 75, feh_temperatures)))

appended = datetime.datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
with open("time_log.txt",'a') as time_logger:
    time_logger.write(appended+"\n")

with open("time_log.txt",'r') as time_logger:
    print(time_logger.read())
