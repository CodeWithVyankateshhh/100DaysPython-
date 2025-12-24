# Looping through a range of numbers
 
for number in range(1,6): # This will generate numbers from 1 to 5
  print(number)
  
for number2 in range(3,10,3): # This will generate numbers from 3 to 9 with a step of 3
  print(number2)
  
for number3 in range(10,2,-2): # This will generate numbers from 10 to 3 in reverse order
  print(number3)
  
total = 0
for number4 in range(1,101):
  total += number4
print(total)