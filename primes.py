"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def calcNextPrime(primes):
    if primes == []:
        primes.append(2)
    else:
        #set a base value to one more than the greatest prime so foar
        baseVal = primes[len(primes) - 1] + 1
        #iterates the base value until a prime number is found
        while checkIfNotPrime(primes, baseVal):
            baseVal += 1
        primes.append(baseVal)

"""Since a number cannot be prime if divisible by another prime, we check if the value passed is divisible by any other primes already passed. If it isn't,
it's prime, and we pass False.
There are more efficient ways of checking this, but they're not entirely necessary for this project."""
def checkIfNotPrime(primes, val):
    for prime in primes:
        if val % prime == 0:
            return True
    return False

def primes(number_of_primes):
    if number_of_primes > 0:
        list = []
        while len(list) < number_of_primes:
            calcNextPrime(list)
        return list
    else:
        raise Exception("ValueError")
