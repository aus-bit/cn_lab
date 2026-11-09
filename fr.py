# =====================================
# TCP AND UDP APPLICATION LOGIC
# =====================================

# Receive message (TCP or UDP)
# message = data.decode()


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
    fact = fact * i

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


# 13. LARGEST DIGIT IN A NUMBER
n = int(message)
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit

    n //= 10

result = str(largest)


# 14. SMALLEST DIGIT IN A NUMBER
n = int(message)
smallest = 9

while n > 0:
    digit = n % 10

    if digit < smallest:
        smallest = digit

    n //= 10

result = str(smallest)


# 15. STRING LENGTH
result = str(len(message))


# 16. UPPERCASE
result = message.upper()


# 17. LOWERCASE
result = message.lower()


# 18. REVERSE STRING
result = message[::-1]


# 19. PALINDROME STRING
if message == message[::-1]:
    result = "Palindrome"
else:
    result = "Not Palindrome"


# 20. COUNT VOWELS
count = 0

for ch in message.lower():
    if ch in "aeiou":
        count += 1

result = str(count)


# 21. COUNT CONSONANTS
count = 0

for ch in message.lower():
    if ch.isalpha() and ch not in "aeiou":
        count += 1

result = str(count)


# 22. COUNT WORDS
words = message.split()
result = str(len(words))


# 23. REMOVE SPACES
result = message.replace(" ", "")


# 24. COUNT CHARACTER 'A'
result = str(message.lower().count('a'))


# 25. COMPARE TWO STRINGS
s1, s2 = message.split()

if s1 == s2:
    result = "Equal"
else:
    result = "Not Equal"


# 26. LARGEST ELEMENT IN LIST
a = list(map(int, message.split()))
result = str(max(a))


# 27. SMALLEST ELEMENT IN LIST
a = list(map(int, message.split()))
result = str(min(a))


# 28. SUM OF LIST ELEMENTS
a = list(map(int, message.split()))
result = str(sum(a))


# 29. SORT LIST
a = list(map(int, message.split()))
a.sort()
result = str(a)


# 30. SEARCH ELEMENT IN LIST
a = list(map(int, message.split()))
x = int(input("Enter search element: "))

if x in a:
    result = "Found"
else:
    result = "Not Found"


# 31. COUNT EVEN NUMBERS IN LIST
a = list(map(int, message.split()))
count = 0

for i in a:
    if i % 2 == 0:
        count += 1

result = str(count)


# 32. SIMPLE CALCULATOR
a, b = map(int, message.split())

# Choose operation
op = '+'

if op == '+':
    result = str(a + b)
elif op == '-':
    result = str(a - b)
elif op == '*':
    result = str(a * b)
elif op == '/' and b != 0:
    result = str(a / b)
else:
    result = "Invalid operation"


# 33. SIMPLE INTEREST
p, r, t = map(float, message.split())
result = str((p * r * t) / 100)


# 34. CELSIUS TO FAHRENHEIT
c = float(message)
result = str((c * 9 / 5) + 32)


# 35. AVERAGE OF LIST
a = list(map(int, message.split()))
result = str(sum(a) / len(a))


# =====================================
# SEND RESULT BACK TO CLIENT
# =====================================

# TCP SERVER:
# conn.send(result.encode())

# UDP SERVER:
# s.sendto(result.encode(), addr)

