
#Question 1

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("divide numbers")
ch = input("Enter any of these char for specific operation / ")

result = 0

if ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch , num2, ":", result)



#Question 2

num1 = input("Enter first number: ");
if num1 == 'x':
    exit();
else:
    num2 = input("Enter second number: ");
    print("\nStarted swapping the given two numbers...");
    number1 = int(num1);
    number2 = int(num2);
    swap = number1;
    number1 = number2;
    number2 = swap;
    print("Given two numbers are successfully swapped!\n");
    print("Value of First and Second number after swapping:");
    print("First Number =",number1,"\nSecond Number=",number2);



#Question 3


	__author__ = 'Owner'
# This program multiplies three numbers provided by the user

# Store input numbers
number1 = input('Enter first number: ')         #I called my first variable number1
number2 = input('Enter second number: ')        #I called my second variable number2
number3 = input('Enter third number: ')        #I called my third variable number3

# multiply three numbers
my_answer = int(number1) * int(number2)  * int(number3)    #I changed my variable to my_answer. int() tell
                                              # python to
                                            # change the input variable to an integer

# Display the sum
print('The product of {0}, {1} and {2} is {3}'.format(number1, number2, number3, my_answer))



#Question 4


n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)



#Question 5


   print("Input some integers to calculate their sum and average. Input 0 to exit.")

count = 0
sum = 0.0
number = 1

while number != 0:
	number = int(input(""))
	sum = sum + number
	count += 1

if count == 0:
	print("Input some numbers")
else:
	print("Average and Sum of the above numbers are: ", sum / (count-1), sum)




#Question 6


age = input("Enter your age: ")

print("You look older than " + age ) 



#Question 7


def sum_thrice(x, y):

     sum = x + y 
  
     if x == y:
      sum = sum * 3
     return sum

print(sum_thrice(2, 2))
print(sum_thrice(3, 3))



#Question 4


while True:
   n = int(input("enter a number between 20 and 100: "))
   if 20 <= n <= 100:
      break
   print('try again')



   #Question 9

   names_array=['jordan','debbie','john','jenelle','tony','suzan','tim','alicia','jordan','jeff']
print("length of names_array is " + str(len(names_array)))
searchForWho=input("who are you searching for ?")
for i in range(0,len(names_array)):
    thisName=names_array[i]
    if(thisName.find(searchForWho) > -1):
        print("found it..",searchForWho, "in position ",i)

        else :
        print("Not Found")