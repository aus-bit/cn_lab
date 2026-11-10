# 1. EVEN OR ODD
n = int(message)
if n % 2 == 0:
    result = "Even"
else:
    result = "Odd"


# 2. DIVISIBLE BY 3 AND 5
n = int(message)
if n % 3 == 0 and n % 5 == 0:
    result = "Divisible by 3 and 5"
else:
    result = "Not Divisible"


# 3. PRIME NUMBER
n = int(message)
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
        break

if n > 1 and flag == 0:
    result = "Prime"
else:
    result = "Not Prime"


# 4. FACTORIAL
n = int(message)
fact = 1
for i in range(1, n + 1):
    fact *= i
result = str(fact)


# 5. LARGEST OF THREE NUMBERS
a, b, c = map(int, message.split())
result = str(max(a, b, c))


# 6. SMALLEST OF THREE NUMBERS
a, b, c = map(int, message.split())
result = str(min(a, b, c))


# 7. LEAP YEAR
n = int(message)
if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    result = "Leap Year"
else:
    result = "Not Leap Year"


# 8. SUM OF DIGITS
n = int(message)
total = 0
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
result = str(total)


# 9. REVERSE A NUMBER
n = int(message)
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
result = str(rev)


# 10. PALINDROME NUMBER
n = int(message)
original = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if original == rev:
    result = "Palindrome"
else:
    result = "Not Palindrome"


# 11. ARMSTRONG NUMBER
n = int(message)
temp = n
total = 0
power = len(str(n))

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == n:
    result = "Armstrong Number"
else:
    result = "Not Armstrong Number"


# 12. FIBONACCI SERIES
n = int(message)
a, b = 0, 1
res = []
for i in range(n):
    res.append(str(a))
    a, b = b, a + b
result = " ".join(res)


# 13. LARGEST DIGIT
n = int(message)
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10
result = str(largest)


# 14. SMALLEST DIGIT
n = int(message)
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10
result = str(smallest)


# 15. PERFECT NUMBER
n = int(message)
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if n > 0 and total == n:
    result = "Perfect Number"
else:
    result = "Not Perfect Number"


# 16. STRONG NUMBER
n = int(message)
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    total += fact
    temp //= 10

if total == n:
    result = "Strong Number"
else:
    result = "Not Strong Number"


# 17. PRODUCT OF DIGITS
n = int(message)
product = 1
while n > 0:
    digit = n % 10
    product *= digit
    n //= 10
result = str(product)


# 18. COUNT DIGITS
n = int(message)
result = str(len(str(abs(n))))


# 19. SECOND LARGEST DIGIT
n = int(message)
digits = sorted(set(str(abs(n))))
if len(digits) >= 2:
    result = digits[-2]
else:
    result = "No second largest digit"


# 20. MULTIPLE OF 10
n = int(message)
if n % 10 == 0:
    result = "Multiple of 10"
else:
    result = "Not Multiple of 10"


# 21. MULTIPLICATION TABLE
n = int(message)
res = []
for i in range(1, 11):
    res.append(f"{n} x {i} = {n*i}")
result = "\n".join(res)


# 22. GCD
import math
a, b = map(int, message.split())
result = str(math.gcd(a, b))


# 23. LCM
import math
a, b = map(int, message.split())
if a == 0 or b == 0:
    result = "0"
else:
    result = str(abs(a*b) // math.gcd(a, b))


# 24. POWER OF 2
n = int(message)
if n > 0 and (n & (n-1)) == 0:
    result = "Power of 2"
else:
    result = "Not Power of 2"


# ---------------- STRING PROGRAMS ----------------

# 25. STRING LENGTH
result = str(len(message))


# 26. UPPERCASE
result = message.upper()


# 27. LOWERCASE
result = message.lower()


# 28. REVERSE STRING
result = message[::-1]


# 29. PALINDROME STRING
if message == message[::-1]:
    result = "Palindrome"
else:
    result = "Not Palindrome"


# 30. COUNT VOWELS
count = 0
for ch in message.lower():
    if ch in "aeiou":
        count += 1
result = str(count)


# 31. COUNT CONSONANTS
count = 0
for ch in message.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1
result = str(count)


# 32. COUNT WORDS
words = message.split()
result = str(len(words))


# 33. REMOVE SPACES
result = message.replace(" ", "")


# 34. COUNT CHARACTER A
result = str(message.lower().count('a'))


# 35. COMPARE TWO STRINGS
s1, s2 = message.split()
if s1 == s2:
    result = "Equal"
else:
    result = "Not Equal"


# 36. COUNT UPPERCASE
count = 0
for ch in message:
    if ch.isupper():
        count += 1
result = str(count)


# 37. COUNT LOWERCASE
count = 0
for ch in message:
    if ch.islower():
        count += 1
result = str(count)


# 38. COUNT DIGITS IN STRING
count = 0
for ch in message:
    if ch.isdigit():
        count += 1
result = str(count)


# 39. COUNT SPACES
result = str(message.count(" "))


# 40. REMOVE VOWELS
result = ""
for ch in message:
    if ch.lower() not in "aeiou":
        result += ch


# 41. ANAGRAM
s1, s2 = message.split()
if sorted(s1.lower()) == sorted(s2.lower()):
    result = "Anagram"
else:
    result = "Not Anagram"


# 42. FIRST CHARACTER
result = message[0] if message else "Empty"


# 43. LAST CHARACTER
result = message[-1] if message else "Empty"


# 44. REPLACE CHARACTER
result = message.replace("a", "b")


# 45. COUNT SPECIAL CHARACTERS
count = 0
for ch in message:
    if not ch.isalnum() and not ch.isspace():
        count += 1
result = str(count)


# 46. CAPITALIZE EACH WORD
result = message.title()


# 47. CHECK ALPHABETS ONLY
if message.isalpha():
    result = "Only Alphabets"
else:
    result = "Other Characters Present"


# ---------------- LIST PROGRAMS ----------------

# 48. LARGEST ELEMENT
a = list(map(int, message.split()))
result = str(max(a))


# 49. SMALLEST ELEMENT
a = list(map(int, message.split()))
result = str(min(a))


# 50. SUM OF ELEMENTS
a = list(map(int, message.split()))
result = str(sum(a))


# 51. SORT LIST
a = list(map(int, message.split()))
a.sort()
result = str(a)


# 52. SEARCH ELEMENT
a = list(map(int, message.split()))
x = a[0]
if x in a:
    result = "Found"
else:
    result = "Not Found"


# 53. COUNT EVEN NUMBERS
a = list(map(int, message.split()))
count = 0
for i in a:
    if i % 2 == 0:
        count += 1
result = str(count)


# 54. SECOND LARGEST ELEMENT
a = list(map(int, message.split()))
b = sorted(set(a))
if len(b) >= 2:
    result = str(b[-2])
else:
    result = "No second largest element"


# 55. SECOND SMALLEST ELEMENT
a = list(map(int, message.split()))
b = sorted(set(a))
if len(b) >= 2:
    result = str(b[1])
else:
    result = "No second smallest element"


# 56. COUNT POSITIVE AND NEGATIVE
a = list(map(int, message.split()))
positive = 0
negative = 0
for i in a:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
result = "Positive: " + str(positive) + ", Negative: " + str(negative)


# 57. SEPARATE EVEN AND ODD
a = list(map(int, message.split()))
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
result = "Even: " + str(even) + ", Odd: " + str(odd)


# 58. REMOVE DUPLICATES
a = list(map(int, message.split()))
result = str(list(dict.fromkeys(a)))


# 59. REVERSE LIST
a = list(map(int, message.split()))
result = str(a[::-1])


# 60. COUNT OCCURRENCES OF FIRST ELEMENT
a = list(map(int, message.split()))
x = a[0]
result = str(a.count(x))


# 61. MERGE TWO LISTS
a, b = message.split(",")
a = list(map(int, a.split()))
b = list(map(int, b.split()))
result = str(a + b)


# ---------------- MATHEMATICAL APPLICATIONS ----------------

# 62. SIMPLE CALCULATOR
a, b = map(int, message.split())
op = '+'

if op == '+':
    result = str(a+b)
elif op == '-':
    result = str(a-b)
elif op == '*':
    result = str(a*b)
elif op == '/' and b != 0:
    result = str(a/b)
else:
    result = "Invalid operation"


# 63. SIMPLE INTEREST
p, r, t = map(float, message.split())
result = str((p*r*t)/100)


# 64. COMPOUND INTEREST
p, r, t = map(float, message.split())
amount = p * (1+r/100)**t
result = str(amount-p)


# 65. AREA OF CIRCLE
import math
r = float(message)
result = str(math.pi*r*r)


# 66. AREA OF RECTANGLE
l, b = map(float, message.split())
result = str(l*b)


# 67. SWAP TWO NUMBERS
a, b = map(int, message.split())
a, b = b, a
result = str(a) + " " + str(b)


# 68. KM TO METRES
km = float(message)
result = str(km*1000)


# 69. PERCENTAGE
obtained, total = map(float, message.split())
if total != 0:
    result = str((obtained/total)*100)
else:
    result = "Invalid total"


# 70. AVERAGE
a = list(map(int, message.split()))
result = str(sum(a)/len(a))


# ---------------- PRACTICAL APPLICATIONS ----------------

# 71. ECHO SERVER
result = message


# 72. GREETING
result = "Hello " + message


# 73. CHECK FILE EXISTS
import os
filename = message
if os.path.exists(filename):
    result = "File Exists"
else:
    result = "File Not Found"


# 74. CURRENT DATE AND TIME
from datetime import datetime
result = str(datetime.now())


# 75. FILE CONTENTS
filename = message
try:
    with open(filename, "r") as f:
        result = f.read()
except FileNotFoundError:
    result = "File Not Found"


# 76. COUNT WORDS AND CHARACTERS
words = len(message.split())
characters = len(message)
result = "Words: " + str(words) + ", Characters: " + str(characters)


# 77. SEND A LIST OF SERVICES
services = ["HTTP", "FTP", "DNS", "SMTP"]
result = ", ".join(services)
# Sum of Digits

n = int(message)
total = 0

while n > 0:
    digit = n % 10       # Get last digit
    total = total + digit
    n = n // 10          # Remove last digit

result = str(total)
exchange 2 
a, b = map(int, message.split())

a, b = b, a

result = str(a) + " " + str(b)


# =====================================================
# SEND RESULT TO CLIENT
# =====================================================

# TCP SERVER:
# conn.send(result.encode())

# UDP SERVER:
# s.sendto(result.encode(), addr)