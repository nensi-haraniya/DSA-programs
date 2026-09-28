# 1. Function to print "Hello, World!"
def hello_world():
    print("Hello, World!")

hello_world()

# 2. Function that takes a name and prints a greeting
def greet(name):
    print("Hello,", name)

greet("Rahul")


# 3. Function to add two numbers
def add(a, b):
    return a + b

print(add(10, 20))


# 4. Function to find the square of a number
def square(n):
    return n * n

print(square(5))


# 5. Function to check whether a number is even or odd
def even_or_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))


# 6. Function to find the maximum of two numbers
def maximum_two(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum_two(10, 20))


# 7. Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

print(celsius_to_fahrenheit(25))


# 8. Function to calculate the area of a circle
def circle_area(radius):
    return 3.14159 * radius * radius

print(circle_area(5))


# 9. Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))


# 10. Function to check whether a number is positive, negative, or zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-10))


# 11. Function to find the maximum of three numbers
def maximum_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(maximum_three(10, 25, 15))


# 12. Function to count vowels in a string
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World"))


# 13. Function to reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))


# 14. Function to check whether a string is a palindrome
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(is_palindrome("madam"))


# 15. Function to find the sum of all elements in a list
def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(list_sum([10, 20, 30, 40]))


# 16. Function to find the largest element in a list
def largest_element(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest

print(largest_element([10, 50, 20, 40]))


# 17. Function to remove duplicate elements from a list
def remove_duplicate(numbers):
    result = []

    for num in numbers:
        if num not in result:
            result.append(num)

    return result

print(remove_duplicate([1, 2, 2, 3, 3, 4]))


# 18. Function to count how many times an element appears in a list
def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count += 1

    return count

print(count_element([1, 2, 2, 3, 2, 4], 2))


# 19. Function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(is_prime(7))


# 20. Function to return all prime numbers between two numbers
def primes_between(start, end):
    primes = []

    for num in range(start, end + 1):
        if num >= 2:
            prime = True

            for i in range(2, num):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                primes.append(num)

    return primes

print(primes_between(10, 30))


# 21. Function to calculate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result

print(fibonacci(10))


# 22. Function to find the second-largest number in a list
def second_largest(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    if len(unique_numbers) < 2:
        return None

    largest = unique_numbers[0]
    second = unique_numbers[0]

    for num in unique_numbers:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

print(second_largest([10, 50, 20, 40, 50, 30]))


# 23. Function to sort a list without using sort()
def sort_list(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result

print(sort_list([5, 2, 8, 1, 3]))


# 24. Function to merge two lists and remove duplicates
def merge_remove_duplicates(list1, list2):
    result = []
    for num in list1:
        if num not in result:
            result.append(num)

    for num in list2:
        if num not in result:
            result.append(num)
            
            return result
print(merge_remove_duplicates([1, 2, 3, 4], [3, 4, 5, 6]))
