import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("1 april 2018 = 20180401")
s = input("whats your birthday")
s_datetime = datetime.datetime.strptime(s, '%Y%m%d')
print (s_datetime)
while True:
    if s_datetime < now:
        print("you are older than 18")
        break
    else:
        print("you are younger than 18")
        break