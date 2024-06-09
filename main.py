print("Hello")

def isEven(value):
    x = int(value/2)
    return x * 2 == value

while True:
    number = input("Enter the number: ")
    if number == '':
        break
    if isEven(int(number)):
        print("is even number")
    else:
        print("is odd number")