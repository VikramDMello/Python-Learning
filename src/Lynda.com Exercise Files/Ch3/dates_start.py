#
# VIK Example file for working with date information
#

import os
import calendar
from datetime import date, time, datetime

def main():
  os.system('clear')
  ## DATE OBJECTS

  # Get today's date from the simple today() method from the date class
  # today = date.today()
  # print("Today's date is", date.today())

  # print out the date's individual components
  # print("Date component - Day:", date.today().day)
  # print("Date component - Month:", date.today().month)
  # print("Date component - Year:", date.today().year)
  
  # retrieve today's weekday and month (0=Monday, 6=Sunday; 1=January, 12=December)
  # print("Today's weekday number is", date.today().weekday())
  # print("Today's month number is", date.today().month)

  # Define array/list of weekday names
  DayOfWeek = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] 
  
  # Define array/list of month names
  MonthOfYear = ["January","February","March","April","May","June","July","August","September","October","November","December"]

  # print ("Which is a", DayOfWeek[date.today().weekday()], "in", MonthOfYear[date.today().month]) 
  # The above is called 'indexing into an array'

  # Ask user for name
  Name = input("\nHello there!  What's your name? ")

  # Ask user for birthday
  BirthdayInput = input("\nWhen were you born (m/d/yyyy)? ")

  # Convert birthday input to date
  Birthday = datetime.strptime(BirthdayInput,'%m/%d/%Y')
  # print(Birthday)
  
  # Date verb tense
  if Birthday.date() < date.today():
    DateTense = "fell on"
  elif Birthday.date() == date.today():
    DateTense = "is today - Happy Birthday!"
  else:
    DateTense = "will fall on"

  # Create and display a single-month calendar based on birthday input
  BirthdayCalendar = calendar.TextCalendar(calendar.MONDAY)
  BirthdayCalendarDisplay = BirthdayCalendar.formatmonth(Birthday.date().year,Birthday.date().month)
  print("\n\n",BirthdayCalendarDisplay,"\n\n")

  # Calculate difference in days between birth date and today
  BirthdayDiff = abs(Birthday.date() - date.today())
  # Calculate age in years
  AgeThisYear = date.today().year - Birthday.date().year
  # Determine birthday this year
  BirthdayThisYear = date(date.today().year,Birthday.date().month,Birthday.date().day)
  # Calculate difference in days between today and next birthday this year
  if abs(BirthdayThisYear - date.today()) < 14:
    BirthdayNext = abs(BirthdayThisYear - date.today())
    BirthdayNextUnit = "days"
  elif abs(BirthdayThisYear - date.today()) < 32:
    BirthdayNext = abs(BirthdayThisYear - date.today()) / 7
    BirthdayNextUnit = "weeks"
  elif abs(BirthdayThisYear - date.today()) >= 32:
      BirthdayNext = abs(BirthdayThisYear - date.today()) / 30.5
      BirthdayNextUnit = "months"


  # Symbols for future use
  Sunny = '\u263c'
  Cloudy = '\u2601'
  Rainy = '\u2614'
  

  print(
    Name,", your birth date,",
    MonthOfYear[Birthday.date().month-1], 
    Birthday.date().day,",",
    Birthday.date().year, 
    DateTense,"a",
    DayOfWeek[Birthday.date().weekday()],
    BirthdayDiff.days,"days ago."
    )
  
  
  if BirthdayThisYear < date.today():
    print("\nYour birthday has passed this year.\nYou turned",AgeThisYear,"years old.\n")
  elif BirthdayThisYear == date.today():
    print("\nIt's your birthday today - *** HAPPY BIRTHDAY! ***  \nYou turned",AgeThisYear,"years old.\n")
  else:
    print("\nYour birthday is coming up later this year in",BirthdayNext,BirthdayNextUnit,"\n")

  
  ## DATETIME OBJECTS

  # Get today's date from the datetime class
  

  # Get the current time


  
if __name__ == "__main__":
  main()
  