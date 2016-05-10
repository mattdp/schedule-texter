#!/usr/bin/python

import time
import datetime
import holidays
from datetime import date

# omitted a ton of test code - definitely revisit when expand project

date_int = datetime.datetime.today().weekday()
date_day = time.strftime("%x")

now = datetime.datetime.now()
year = int(now.year)
month = int(now.month)
day = int(now.day)

text = []
day_start = {0: '8:00', 1: '9:20', 2: '8:00', 3: '9:20', 4: '8:00'} #1st hour of the day
lunch_start = {0: '11:16', 1: '11:55', 2: '11:00', 3: '11:55', 4: '11:55'}

date_int = datetime.datetime.today().weekday()
date_day = time.strftime("%x")

#---------------------------
#find the first hour
#---------------------------
first_hour= day_start[date_int]
first_hour_form = datetime.datetime.strptime(first_hour,'%H:%M')

first_notif = first_hour_form - datetime.timedelta(hours=1, minutes=00, seconds=00)
morning_trigger = datetime.datetime.time(first_notif)

#---------------------------
#after lunch (Notification 1 hour before lunch or 1 hour before the 1st lesson of the afternoon
#---------------------------
sec_hour= lunch_start[date_int]
sec_hour_form = datetime.datetime.strptime(sec_hour,'%H:%M')

sec_notif = sec_hour_form - datetime.timedelta(hours=1, minutes=00, seconds=00)
afternoon_trigger = datetime.datetime.time(sec_notif)

def weekday_map():
  weekday = {0:'Monday',1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday'}
  return weekday

#-----------------------------------------
#define the morning schedule according the day
#-----------------------------------------
def sched_morning (date_int):
  if date_int == 0:
    text = ["1st  8:00 to 9:02 Mathematics", "2nd  9:07 to 10:09 History", "3rd  10:14 to 11:16 Physics"]

  if date_int == 1:
    text = ['1st  8:00 to 9:15  English', '2nd  9:20 to 10:35  Art', '3rd  10:40 to 11:55  Mathematics']

  if date_int == 2:
    text = ['3rd  8:00 to 9:15  History', 'Homeroon  9:20 to 9:40 ', '4th  9:45 to 11:00  English']

  if date_int == 3:
    text = ['1st  8:00 to 9:15  History', '2nd  9:20 to 10:35  Sport', '4th  10:40 to 11:55  Geography']

  if date_int == 4:
    text = ['1st  8:00 to 9:15  Physics', '2nd  9:20 to 10:35  Mathematics', '3rd  10:40 to 11:55  English']

  return '\n'.join(text)

#-----------------------------------------
#define the afternoon schedule according the day
#NEEDS REFACTOR IF USING WITH REDESIGN FOR DEMO
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
def morning_text(date_int):
  output_string = ""
  output_string += "Today : " + weekday_map()[date_int] + " the " + date_day + "\n"
  output_string += "Here are your courses:\n"
  output_string += "--------------\n"
  output_string += sched_morning(date_int)
  return output_string