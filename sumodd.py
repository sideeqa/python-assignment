
counter=1
sum_odd=0
sum_even=0

while(counter <= 20):
      
    print("Enter your number")
    number = int(input())
    if (number%2==0):
         sum_even+=number 
    else:
         sum_odd+=number
    counter = counter+1
print("The sum of even number and sum of odd numbers are",sum_even, "and",sum_odd,"respectively")
     
