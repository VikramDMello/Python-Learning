#
# Example file for working with loops
#

def main():
  print("\n")
  x = 0

  # define a while loop
  # while (x<5) or (x<6):
  #   print (x)
  #   x = x+1


  # define a for loop
  # for x in range(5,10,2):
  #     print (x)



  # use a for loop over a collection
  # days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  # for d in days:
  #   if len(d) == 2:
  #     print (d)

   
 
  # use the break and continue statements
  # for x in range(1,25):
  #   if (x % 2 != 0): # If "modulo of x and 2 not zero"; OR "remainder of x divided by 2 not zero"
  #     continue
  #   print (x)


  #using the enumerate() function to get index 
  days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for counter,day in enumerate(days, 0):
    print (counter, day)

  print("\n")



if __name__ == "__main__":
  main()
