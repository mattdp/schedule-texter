#!/usr/bin/python

import time
import datetime
from datetime import date
import holidays


weekday = {0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

date_int = datetime.datetime.today().weekday()
print date_int
date_day = time.strftime("%x")
#date_day = datetime.datetime.now()
print date_day

now = datetime.datetime.now()
year = int(now.year)
month = int(now.month)
day = int(now.day)
print year,month,day

#-----------------------------------------
#Test the weekend (date_day = 4 or 5)
#-----------------------------------------
day_week = True
print "test du WE"
if date_day == ( 5 or 6 ):
   day_week = False
#else:
#    day_week = True


#-----------------------------------------
#Test day off (2016)
#-----------------------------------------
day_off = False
print "test du day off"
from datetime import datetime


if day_week == True:
   #weekday = {0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}

   print date_int
   print weekday[date_int]
   #print "date_day originel " + date_day
   date_conv = time.strftime("%Y-%m-%d")
   print type(date_conv)
   #date_comp = datetime.date()
   #print date_comp
   print "date_conv " + date_conv

  # dt_str = '9/24/2010 5:03:29 PM'
  # dt_obj = datetime.strptime(str(date_conv),'%Y-%m-%d')
  #dt_obj = datetime.strptime(date_conv,date(yyyy,mm,dd))
  # print dt_obj

   #print type(date_conv)
   #print "Current date_conv " + date_conv

#    print "date test : '2016-07-04'"
   print "-----------"
#----date to test
#    date_conv = '2016-07-04'
   #print type(date_conv)


   for date, name in sorted(holidays.US(state='CA', years=2016).items()):
   #   print date, name
   #    print type(date) ==> <type 'datetime.date'>
   #    print type(date_conv) ==> string
       if str(date) == date_conv:
           day_off = True
          # print (day_off,  'today is a day off')
           break
       else:
           day_off = False
           #print (day_off, ' today is a school day')

   #print day_off



#-----------------------------------------
#Test holidays
#-----------------------------------------
from datetime import date
def check_schooldays(year, month, day):
   #we are going to check if the date is a schoolday or if it belongs to holidays
   #as long as it is not found in holidays, we keep on comparing the date

   print "dans la boucle"
   list_of_holidays = [('Thanksgiving', date(2015, 11, 26), date(2015, 12, 2)),
                       ('Winter Recess', date (2015, 12, 24), date(2016, 1, 5)),
                       ('Spring Break', date(2016, 4, 4), date(2016, 4, 8)),
                       ('Summer Recess', date(2016, 8, 7), date(2016, 9, 30))]


   keep_going = True
   #i=0
   for name, date_start, date_end in list_of_holidays:
       #i=i+1
       #print i
       #print "dans le for"
       if date_start <= date(year, month, day) <= date_end:
           #if the date of the day is included in the list, then we are in holydays and we don't need to keep on checking the date (set FALSE)
           #and we can leave the loop "BREAK"
           keep_going = False
           break
       else:
           keep_going = True
   print keep_going
   return keep_going



if day_off == False:
   print "appel de la fonction"
   check_schooldays(year, month, day)
   send_text = check_schooldays(year, month, day)
#    print keep_going
#    print check_schooldays(2016, 1, 6)
#    print check_schooldays(2016, 8, 30)
   print "send_text", send_text
   print "sortie de la fonction"
#-----------------------------------------
#calcul de l'heure : evenement declencheur
#-----------------------------------------
import datetime

current_time = time.strftime("%X")
print "Current_time", current_time
print "-----------"

print "declenchement heure"
if send_text == True:
   text = []
   day_start = {0: '8:00', 1: '9:20', 2: '8:00', 3: '9:20', 4: '8:00'} #1st hour of the day
   lunch_start = {0: '11:16', 1: '11:55', 2: '11:00', 3: '11:55', 4: '11:55'}

   date_int = datetime.datetime.today().weekday()
   date_day = time.strftime("%x")
   print "Current time " + time.strftime("%X")

   #---------------------------
   #find the first hour
   #---------------------------
   first_hour= day_start[date_int]
   #print first_hour
   #print type(first_hour)
   first_hour_form = datetime.datetime.strptime(first_hour,'%H:%M')
   #print first_hour_form
   #print type(first_hour_form)


   first_notif = first_hour_form - datetime.timedelta(hours=1, minutes=00, seconds=00)
   morning_trigger = datetime.datetime.time(first_notif)
   #print "morning trigger ", morning_trigger

   #---------------------------
   #after lunch (Notification 1 hour before lunch or 1 hour before the 1st lesson of the afternoon
   #---------------------------
   sec_hour= lunch_start[date_int]
   #print sec_hour
   #print type(sec_hour)
   sec_hour_form = datetime.datetime.strptime(sec_hour,'%H:%M')
   #print sec_hour
   #print type(sec_hour_form)

   sec_notif = sec_hour_form - datetime.timedelta(hours=1, minutes=00, seconds=00)
   afternoon_trigger = datetime.datetime.time(sec_notif)
   #print "afternoon trigger ", afternoon_trigger

   print "morning trigger ", morning_trigger
   print "afternoon trigger ", afternoon_trigger




#-----------------------------------------
#print the schedule with 1 course by line
#-----------------------------------------
mylist=[]
def print_notif (mylist):
   for i in mylist:
       print i

#-----------------------------------------
#define the morning schedule according the day
#-----------------------------------------
def sched_morning (date_int):
   if date_int == '0':
       text = ["1st  8:00 to 9:02 Mathematics", "2nd  9:07 to 10:09 History", "3rd  10:14 to 11:16 Physics"]
       return print_notif(text)

   if date_int == '1':
       text = ['1st  8:00 to 9:15  English', '2nd  9:20 to 10:35  Art', '3rd  10:40 to 11:55  Mathematics']
       return print_notif(text)

   if date_int == '2':
       text = ['3rd  8:00 to 9:15  History', 'Homeroon  9:20 to 9:40 ', '4th  9:45 to 11:00  English']
       return print_notif(text)

   if date_int == '3':
       text = ['1st  8:00 to 9:15  History', '2nd  9:20 to 10:35  Sport', '4th  10:40 to 11:55  Geography']
       return print_notif(text)

   if date_int == '4':
       text = ['1st  8:00 to 9:15  Physics', '2nd  9:20 to 10:35  Mathematics', '3rd  10:40 to 11:55  English']
       return print_notif(text)


#-----------------------------------------
#pdefine the afternoon schedule according the day
#-----------------------------------------
def sched_afternoon (date_int):
   if date_int == '0':
       text = ["4th  11:56 to 12:58 Mathematics", "5th  1:03 to 2:05 History", "6th  2:10 to 3:12 Physics"]
       return print_notif(text)

   if date_int == '1':
       text = ['4th  12:35 to 1:50  English', '5th  1:55 to 3:10  Art']
       return print_notif(text)

   if date_int == '2':
       text = ['6th  11:40 to 12:55  History', 'Office Hours  1:00 to 1:25']
       return print_notif(text)

   if date_int == '3':
       text = ['5th  12:35 to 1:50  History', '6th  1:55 to 3:10  Sport']
       return print_notif(text)

   if date_int == '4':
       text = ['5th  12:35 to 1:50  Physics', '6th  1:55 to 3:10  English']
       return print_notif(text)



#-----------------------------------------
#print the content of the message in the morning (and positive quotes?)
#-----------------------------------------
print "Today : " + weekday[date_int] + " the " + date_day
print "Here are your courses"
print "--------------"
#print "positive quotes"

print sched_morning ('0')
print "--------------"
print sched_morning ('1')
print "--------------"
print sched_morning ('2')
print "--------------"
print sched_morning ('3')
print "--------------"
print sched_morning ('4')

#-----------------------------------------
#print the content of the message in the afternoon (and positive quotes?)
#-----------------------------------------
print "Today : " + weekday[date_int] + " the " + date_day
print "Here are your courses"
print "--------------"
#print "positive quotes"

print sched_afternoon ('0')
print "--------------"
print sched_afternoon ('1')
print "--------------"
print sched_afternoon ('2')
print "--------------"
print sched_afternoon ('3')
print "--------------"
print sched_afternoon ('4')