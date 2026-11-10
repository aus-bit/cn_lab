. Even or Odd

n = int(data.decode())

if n % 2 == 0:

    result = "Even"

else:

    result = "Odd"

2. Divisible by 3 and 5

if n % 3 == 0 and n % 5 == 0:

    result = "Divisible"

else:

    result = "Not Divisible"

3. Sum of digits

n = int(data.decode())

sum = 0



while n > 0:

    sum += n % 10

    n //= 10



result = str(sum)

4. Reverse a number

n = int(data.decode())

rev = 0



while n > 0:

    rev = rev * 10 + n % 10

    n //= 10



result = str(rev)

5. Palindrome

n = int(data.decode())

if str(n) == str(n)[::-1]:

    result = "Palindrome"

else:

    result = "Not Palindrome"

6. Armstrong number

n = int(data.decode())

temp = n

total = 0



while n > 0:

    r = n % 10

    total += r ** 3

    n //= 10



if temp == total:

    result = "Armstrong"

else:

    result = "Not Armstrong"

7. Prime number

n = int(data.decode())

count = 0



for i in range(1, n + 1):

    if n % i == 0:

        count += 1



if count == 2:

    result = "Prime"

else:

    result = "Not Prime"

8. Factorial

n = int(data.decode())

fact = 1



for i in range(1, n + 1):

    fact *= i



result = str(fact)

9. Fibonacci series

n = int(data.decode())

a, b = 0, 1

result = ""



for i in range(n):

    result += str(a) + " "

    a, b = b, a + b

10. Largest of three

a, b, c = map(int, data.decode().split())



result = str(max(a, b, c))

11. Swap two numbers

a, b = map(int, data.decode().split())

a, b = b, a



result = str(a) + " " + str(b)

12. Multiplication table

n = int(data.decode())

result = ""



for i in range(1, 11):

    result += f"{n} x {i} = {n*i}\n"

13. String length

s = data.decode()

result = str(len(s))

14. Count vowels

s = data.decode()

count = 0



for ch in s.lower():

    if ch in "aeiou":

        count += 1



result = str(count)

15. Celsius to Fahrenheit

c = float(data.decode())

f = (c * 9/5) + 32



result = str(f)

3. Python functions y