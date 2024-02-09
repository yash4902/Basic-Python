# # import time 
# # tick = time.time()
# # print(tick)
# # print(time.localtime())


# # localtime = time.localtime(time.time())
# # print(localtime)


# # formatedtime = time.asctime(time.localtime(time.time()))
# # print(formatedtime)


# # import calendar

# # cal = calendar.month(2024,2)
# # print(cal)

# # print("time altzone: ",time.altzone)


# # from datetime import date
# # date1 = date(2024,1,19)
# # print("Date: ",date1)
# # date2 = date(2024,1,31)



# # mindate = date.min
# # print("Minimum date: ",mindate)   

# # maxdate = date.max
# # print("Maximm date: ",maxdate)

# # print(date.today())
# # d1 = date.fromisoformat("2024-01-19")
# # print(d1)
# # d2 = date.fromisoformat("20240119")
# # print(d2)

# # from datetime import date
# # d = date.fromordinal(738630)
# # print(d)
# # print(d.timetuple())


# # print(d.isoformat())
# # print(d.strftime("%d/%m/%y"))
# # print(d.strftime("%A %d. %B %Y"))
# # print(d.ctime())

# # print("The {1} is {0:%d}, the {2} is {0:%B}.".format(d,"day","month"))

# # t = d.timetuple()
# # for i in t: 
# #     print(i)

# # ic = d.isocalendar()
# # for i in ic:
# #     print(i)


# # print(d.replace(month=5))


# from datetime import time 

# time1 = time(8,14,36)
# print(time1)

# time2 = time(minute=12)
# print(time2)

# time3 = time()
# print("time",time3)


# print(time.min)
# print(time.max)

# print(time.resolution)
# print(time1.hour)
# print(time1.minute)
# print(time1.second)
# print(time1.microsecond)


# from datetime import datetime 
# dt = datetime(2024,1,19)
# print(dt)

# dt = datetime(2024,1,19,11,6,30,3000)
# print(dt)


# dt = datetime.now()

# print('Day: ',dt.day)
# print("Month: ",dt.month)
# print("Year: ",dt.year)
# print("Hour: ",dt.hour)
# print("Minute: ",dt.minute)
# print("Second: ",dt.second)

# print(dt.today())


# print(datetime.now())


# from datetime import timedelta

# delta = timedelta(
#     days=100,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=12,
#     weeks=2
# )
# print(delta)


# min = timedelta.min
# print("Minimum date: ",min)


# max = timedelta.max
# print("Maximum date: ",max)

# year = timedelta(days=365)
# print(year)