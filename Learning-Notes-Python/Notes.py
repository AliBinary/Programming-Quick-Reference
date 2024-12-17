import numpy as np
import platform

# 1
numbers = [1, 2, 3, 4, 5]
doubles = map(lambda x: x * 2, numbers)
print(list(doubles))

names = ["mohammad", "sara", "iman", "ali"]
upperNames = map(lambda name: name.upper(), names)
print(list(upperNames))

# 2
numbers = [2, 4, 6, 7]
print(all([0, 2, 3, 4]))
print(all([num % 2 == 0 for num in numbers]))
print(any([num % 2 != 0 for num in numbers]))

# 3
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda num: num % 2 == 0, numbers)

# 4
chars = ['a', 't', 'z']
numbers = [3, 6, 8, 13, 4, 90]
print(max(numbers))
print(min(chars))

names = ['mohammad', 'milad', 'akbar', 'sara', 'iman', 'ali']
print(max(names, key=lambda n: len(n)))
print(min(names, key=lambda n: len(n)))

# 5
numbers = [1, 2, 3, 4, 5, 6]
print(list(reversed(numbers)))
print(list(reversed("hello")))

# 6
users = [
    {'name': 'mohammad', 'family': 'ordookhani', 'age': 23},
    {'name': 'taha', 'family': 'ordookhani', 'age': 40},
    {'name': 'ali', 'family': 'ordookhani', 'age': 30},
    {'name': 'sara', 'family': 'ordookhani', 'age': 80}
]
print(sorted(users, key=lambda user: user['age'], reverse=True))

numbers = [1, 5, 8, 4, 6, 2]
result = sorted(numbers, reverse=True)
print(result)

# 7
number = -5
print(abs(number))

# 8
data = (3, 4, 5, 6, 7, 8, 9)
print(len(data))

# 9
number = 4.56330480
print(round(number, 2))

# 10
numbers = [1, 2, 3]
print(sum(numbers, 10))

# 11
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [5, 6, 7, 8, 9, 10]
result = zip(numbers_1, numbers_2)
print(list(result))

myList = [(1, 5), (3, 7), (6, 4), (7, 9)]
print(list(zip(*myList)))

# 12
print(ord('a'))  # --> 97
print(chr(98))  # ---> b

# 13
price = 29825.344149584496
text = "right now, Bitcoin is %f dollars!" % price
print(text)

txt = "For only {:.2f} dollars!"
print(txt.format(price))

# 14
print(platform.system())
print(dir(platform))  # list all the function names in a modules

# 15
sorted(map(int, input().split()))
sorted([int(i) for i in input().split()])
[int(i) for i in input().split()].sort()

# 16
seq = "1 3 8 1"
"".join(seq.split())  # --> "1381"
seq.replace(" ", "")  # --> "1381"

# 17
num = int(input(), 2)  # save number in base 2
print(int("cafe", 16))
bin(7)  # convert decimal num to binary
int(0b111)  # convert binary to decimal
oct(22)  # convert decimal to octal number
hex(22)  # convert decimal to hexadecimal number

print((42).bit_length())  # check th bit-length of integer

num1, num2, a, n = 5, 7, 13, 2
print(num1 & num2)  # ---> Bitwise AND
print(num1 | num2)  # ---> Bitwise OR
print(num1 ^ num2)  # ---> Bitwise XOR (exlusive OR)
print(~a)  # ---> Bitwise NOT
print(a << n)  # ---> Bitwise left shift
print(a >> n)  # ---> Bitwise right shift

"""
also you can use them to form below:
   a &= b     ---> a = a & b
   a |= b     ---> a = a | b
   a ^= b     ---> a = a ^ b
   a <<= n     ---> a = a << n
   a >>= n     ---> a = a >> n
"""

print(f"{42:b}")  # 42 in binary
print(f"{42:032b}")  # 42 in binary on 32 zero-padded digits

s = {*input().split()}  # unpack the values from any iterable object
print(s)

# 18
txt = input()
match txt:
    case "one":
        print(1)
    case "two":
        print(2)
    case "three":
        print(3)
    case _:
        print("default")

# 19
x = 10
y = 7
z = 5
if z < y < x:  # means (z < y) and (y < x)
    pass

# 20
np.linspace(0, 1, 10)     # specify the number of steps
np.arange(0, 1, .1)       # specify the size of the steps
