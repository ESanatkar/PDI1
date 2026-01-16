import time

'''
# Exercise 1


   Countdown, Liftoff


def countdown(n: int) -> None:
    """Print countdown from n to 1, then Liftoff!"""
    while n >= 1:
        if n <= 0: 
            break
        print(n)
        n -= 1
        time.sleep(1)
    print("Liftoff!")
    
if __name__ == "__main__":
    countdown(10)
'''

'''
# Exercise 2


   Positive Sums


def sum_positives(numbers: list[int]) -> int:
    """Return the sum of positive numbers in the list."""
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

print(sum_positives([1, 5, 3]))
    
def find_max(numbers: list[int]) -> int:
    """Returns the largest positive number given in the list."""
    currentLargest:int = 0

    for num in numbers:
        if num >currentLargest:
            currentLargest = num
    
    return currentLargest
        
def test_find_max():
    assert find_max([1, 2, 3]) == 3
    assert find_max([3, 2, 1]) == 3
    assert find_max([2, 3, 1]) == 3
    assert find_max([5, 5, 5]) == 5
    
    
if __name__ == "__main__":
    print(find_max([10, 5, 3]))  # Should print 10
'''

'''
# Exercise 3


   Password Requirements


def is_valid_password(password: str) -> bool:
    """Check if password is at least 8 characters with a digit."""
    has_digit = False
    has_upper = False

    if len(password) < 8:
        return False
    
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    
    if has_digit and has_upper:
        return True
    
    return False
    
    
def test_is_valid_password():
    assert is_valid_password("hello123") == True
    assert is_valid_password("short1") == False
    assert is_valid_password("longpassword") == False
    assert is_valid_password("12345678") == True
    

if __name__ == "__main__":
    print(is_valid_password("helLo123"))  # Should print True
    print(is_valid_password("hello123"))  # Should print False now
'''

'''
# Exercise 4


   Password Strength Handler
'''

def count_digits(password: str) -> int:
    """Count the number of digits in a password."""
    count = 0
    for char in password:
        if char.isdigit():
            count += 1
    return count


def count_special(password: str) -> int:
    """Count special characters in a password."""
    special_chars = "!@#$%^&*"
    count = 0
    for char in password:
        if char in special_chars:
            count += 1
    return count


def check_strength(password: str) -> str:
    """Return password strength: Weak, Medium, or Strong."""
    length = len(password)
    digits = count_digits(password)
    specials = count_special(password)
    
    if length >= 12 and digits >= 2 and specials >= 1:
        return "Strong"
    elif length >= 8 and digits >= 1:
        return "Medium"
    else:
        return "Weak"


def test_count_digits():
    assert count_digits("abc123") == 3
    assert count_digits("hello") == 0


def test_count_special():
    assert count_special("hello!@#") == 3
    assert count_special("password") == 0


def test_check_strength():
    assert check_strength("ab") == "Weak"
    assert check_strength("password1") == "Medium"
    assert check_strength("MySecure99!x") == "Strong"


if __name__ == "__main__":
    passwords = ["cat", "hello123", "SuperSecure42!"]
    
    for pw in passwords:
        strength = check_strength(pw)
        print(f"{pw}: {strength}")

# hello123, has 3 digits. [1, 2, 3]
# SuperSecure42! is rated as strong as it has 2 digits, and a special character with makes it more variable.