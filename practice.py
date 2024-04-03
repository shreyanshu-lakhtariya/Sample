
#num_sqrt = num ** 0.5
#print('the square root of %0.3f if %0.3f' %(num, num_sqrt)) 


num = int(input('Enter number: '))
#y = input('Enter value of y: ')

fact = 1
if num < 0:
  print("factorial does not exist for negative numbers")
elif num == 1:
   print("factorial is 1")
else:
  for i in range(1 , num + 1):
    fact = fact * i
  print("the factorial of" ,num, "is" ,fact)