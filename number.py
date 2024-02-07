number1 = int(input("Number 1 is: "))
number2 = int(input("Number 2 is: "))
number3 = int(input("Number 3 is: "))
number4 = int(input("Number 4 is: "))

def func(number1, number2, number3, number4):
    return (number1 + number2 + number3 + number4) / 4

def largest_and_smallest(number1, number2, number3, number4):
    numbers = [number1, number2, number3, number4]
    large = max(numbers)
    small = min(numbers)
    return large, small

large, small = largest_and_smallest(number1, number2, number3, number4)

print(func(number1, number2, number3, number4))
print("Largest:", large)
print("Smallest:", small)  