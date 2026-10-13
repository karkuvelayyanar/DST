# PYTHON DAY - 5 TASK
# Python practice set with 10 questions

print("PYTHON DAY - 5 TASK")
print("=" * 30)

# Q1. Reverse and palindrome check
text = input("Q1. Enter a string: ")
reversed_text = text[::-1]
print("Reversed:", reversed_text)
print("Palindrome:", text == reversed_text)

# Q2. Vowel and consonant count
word = input("Q2. Enter a word: ")
vowels = sum(1 for ch in word if ch.lower() in "aeiou")
consonants = sum(1 for ch in word if ch.isalpha() and ch.lower() not in "aeiou")
print("Vowels:", vowels)
print("Consonants:", consonants)

# Q3. Common elements in two lists
print("Q3. Enter two lists of numbers: ")
list1 = list(map(int, input("List 1: ").split()))
list2 = list(map(int, input("List 2: ").split()))
common = sorted(set(list1) & set(list2))
print("Common elements:", common)

# Q4. Remove duplicates in order
numbers = list(map(int, input("Q4. Enter numbers separated by spaces: ").split()))
unique = []
seen = set()
for num in numbers:
    if num not in seen:
        seen.add(num)
        unique.append(num)
print("After removing duplicates:", unique)

# Q5. Multiplication table
n = int(input("Q5. Enter a number: "))
print(f"Multiplication table for {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Q6. Fibonacci series
limit = int(input("Q6. Enter the number of terms: "))
a, b = 0, 1
fib_series = []
for _ in range(limit):
    fib_series.append(a)
    a, b = b, a + b
print("Fibonacci series:", fib_series)

# Q7. Perfect number check
num = int(input("Q7. Enter a number: "))
sum_divisors = sum(i for i in range(1, num) if num % i == 0)
print("Perfect number:", num > 0 and sum_divisors == num)

# Q8. Frequency of characters
sentence = input("Q8. Enter a sentence: ")
frequency = {}
for ch in sentence:
    frequency[ch] = frequency.get(ch, 0) + 1
print("Character frequency:")
for key, value in frequency.items():
    print(f"{key}: {value}")

# Q9. Matrix transpose
rows, cols = map(int, input("Q9. Enter rows and columns: ").split())
print("Enter matrix values row by row:")
matrix = [list(map(int, input().split())) for _ in range(rows)]
transposed = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
print("Transposed matrix:")
for row in transposed:
    print(row)

# Q10. Student grade calculator
print("Q10. Student grade calculator")
name = input("Student name: ")
marks = list(map(float, input("Enter marks separated by spaces: ").split()))
avg = sum(marks) / len(marks)
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Student: {name}")
print(f"Average marks: {avg:.2f}")
print(f"Grade: {grade}")

print("\nTask completed successfully.")
