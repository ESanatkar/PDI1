from collections.abc import Iterable

'''
# Exercise 1

    Low To High
'''

def start_to_end(start: int, end: int) -> None:
    if start > end:
        return

    print(start)
    start_to_end(start + 1, end)

start_to_end(4, 9)

'''
# Exercise 2

    List Flattening
'''

def flatten(lst: Iterable) -> list:
    result: list = []
    for item in lst:
        if isinstance(item, Iterable) and not isinstance(item, str):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([[1, 2], [3, [4, 5]], 6]))

'''
# Exercise 3

    Coin Combinations
'''

def ways(amount: int, coins: list[int]) -> int:
    if amount == 0:
        return 1
    if amount < 0 or not coins:
        return 0
    
    return ways(amount - coins[0], coins) + ways(amount, coins[1:])

print(ways(5, [1, 2, 3]))  # 5
print(ways(50, [1, 5, 10, 25]))  # 49