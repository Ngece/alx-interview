'''Prime game for Maria and Ben'''

def isWinner(x, nums):
    '''Returns the name of the player that won the most rounds'''
    def is_prime(num):
        '''Returns True if num is prime, else False'''
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def can_win(n):
        '''Returns True if Maria can win, else False'''
        if n % 2 == 0:
            return True
        else:
            return not is_prime(n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
    