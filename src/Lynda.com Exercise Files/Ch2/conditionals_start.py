#
# Example file for working with conditional statements
#

def main(x, y):
  
  # conditional flow uses if, elif, else  
  if (x < y):
    st = "x is less than y"
    return st
  elif (x == y):
    st = "x is the same as y"
    return st
  else:
    st = "x is greater than y"
    return st
print (main(10,100))

# conditional statements let you use "a if C else b"
x, y = 100, 10
st = "x is less than y" if (x<y) else "x is more than y"
print (st)
  

# if __name__ == "__main__":
#   main(10,10)
