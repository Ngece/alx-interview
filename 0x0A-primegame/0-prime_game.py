#!/usr/bin/python3
'''Prime game for Maria and Ben'''

def isWinner(x, nums):
    '''Prime game for Maria and Ben'''
    def is_prime(num):
        '''Check if a number is prime'''
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    def get_primes(n):
        '''Get all primes up to n'''
        primes = []
        for i in range(1, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes
    
    def get_winner(primes, n):
        '''Get the winner of the game'''
        if n % 2 == 0:
            return 'Maria'
        return 'Ben'
    
    if x < 1 or nums is None:
        return None
    
    primes = get_primes(max(nums))
    maria_turn = True  
    winners = []

    for n in nums:
        if n in primes:
            if maria_turn:
                winners.append('Maria')
            else:
                winners.append('Ben')
        maria_turn = not maria_turn

    maria_wins = winners.count('Maria')
    ben_wins = winners.count('Ben')

    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
