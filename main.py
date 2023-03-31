num = int(input('Digite um número: '))

if num%5==0 and num%3==0:
    print("FizzBuzz")
else:
    if num%3 == 0:
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    else:
        print(num)