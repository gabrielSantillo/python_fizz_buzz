def fizz_buzz(number):
    if(number % 3 == 0 and number % 5 == 0):
        print('FizzBuzz')
    elif(number % 5 == 0):
        print('Buzz')
    elif(number % 3 == 0):
        print('Fizz')

list_of_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for number in list_of_numbers:
    fizz_buzz(number)