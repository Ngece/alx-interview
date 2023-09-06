#!/usr/bin/python3
'''Prime game for Maria and Ben'''

def isWinner(x, nums):
    '''Returns the name of the player that won the most rounds'''
    def is_prime(num):
        '''Checks if a number is prime'''
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def get_primes(n):
        '''Returns a list of prime numbers'''
        primes = []
        for i in range(1, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes
    
    def get_winner(primes, n):
        '''Returns the winner of the game'''
        if n % 2 == 0:
            return 'Maria'
        return 'Ben'
    
    if x < 1 or nums is None:
        return None
    primes = get_primes(max(nums))
    score = 0
    for n in nums:
        if n in primes:
            score += 1
    return get_winner(primes, score)
