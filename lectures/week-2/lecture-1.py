from math import prod
import time

'''
# Exercise 1


   Grade Statistics
'''

grades: list[int] = [78, 85, 92, 68, 95, 88, 73, 90, 82, 87]

lowest_grade: int = min(grades)
highest_grade: int = max(grades)
average_grade: float = sum(grades) / len(grades)

print("Lowest Grade: " + str(object=lowest_grade))
print("Highest Grade: " + str(object=highest_grade))
print("Average Grade: " + str(object=average_grade))

total_above_80 = 0
list_above_85: list = []

for grade in grades:
    if grade >80:
        total_above_80 += 1
        if grade > 85:
            list_above_85.append(grade)


print(total_above_80)
print(list_above_85)

list_above_85.sort(reverse=True)
print(list_above_85)

'''
# Exercise 2


   List Comprehensions
'''

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x ** 2, numbers)))

words: list[str] = ["apple", "banana", "kiwi", "strawberry", "grape"]
print(list(filter(lambda x: len(x) >5, words)))

temperatures: list[int] = [23, 18, 32, 15, 28, 20]
print(list(map(lambda x: (x * 9/5) + 32, temperatures)))

'''
# Exercise 3


   Tuples
'''

users: list[tuple[int, str, str]] = [
    (101, "barold@email.com", "Barold"),
    (102, "cleo@email.com", "Cleo"),
    (103, "kabuki@email.com", "Kabuki")
]

for tuple in users:
    print("Name: " + tuple[2] + ", Email: " + tuple[1])

print(users[1][2])
users.append((104, "maddie@email.com", "Maddie"))
print(users)

email_list: list[str] = []

for tuple in users:
    userid, email, user = tuple
    email_list.append(email)

print(email_list)

'''
# Exercise 4


   Zip and Enumerate
'''

products: list[str] = ["laptop", "mouse", "keyboard", "monitor"]
prices: list[int] = [899, 25, 75, 350]

product_tuples: list = []

for item in zip(products, prices):
    product_tuples.append(item)

print(product_tuples)

for idx, x in enumerate(products):
    print(f"index {idx}")
    print(f"item {x}\n")

print(max(product_tuples, key=lambda x: x[1]))

discounted_products: list[float] = list(map(lambda x: x[1] * .9, product_tuples))
print(discounted_products)

discounted_product_tuples: list = []

for item in zip(products, discounted_products):
    discounted_product_tuples.append(item)

print(list(filter(lambda x: x[1] >50, discounted_product_tuples)))