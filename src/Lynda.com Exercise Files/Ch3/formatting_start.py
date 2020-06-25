#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  # print(now.strftime("The current year is: %Y"))
  # print(now.strftime("The current year is: %y"))
  # print(now.strftime("The current month is: %B"))
  # print(now.strftime("The current month is: %b"))
  # print(now.strftime("The current date is: %D"))
  # print(now.strftime("The current date is: %d"))
  # print(now.strftime("The current weekday is: %A"))
  # print(now.strftime("The current weekday is: %a"))
  
  print(now.strftime("Today is %A, %B %d, and it is currently %H:%M"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM



if __name__ == "__main__":
  main();
