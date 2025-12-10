letter= input(largest number
Get three integers from three different number
number1=int("Input(The fisrt number: "))
number2=int("Input(The second number: "))
number3=int("Input(The third number: "))
largest = number1

if number2 >= largest:
  largest = number2
elif number3 >= largest:
    largest = number3
else:
    largest = largest

 print("The largest numberis: ", largest)
