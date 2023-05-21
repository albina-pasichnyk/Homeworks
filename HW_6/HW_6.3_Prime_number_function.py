"""
3. Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime
number, and False otherwise.
"""
def is_prime(number: int) -> bool:
    if 2 < number < 1000:
        for i in range(2, int(number/2)):
            if number % i == 0:
                return False
        return True
    else:
        return False

#print(is_prime(9))
