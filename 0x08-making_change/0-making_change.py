#!/usr/bin/python3
"""Determines a minimum number of coins to make change 
for an amount of money
"""

def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        if coin <= total:
            num_coins += total // coin
            total = total % coin
    if total != 0:
        return -1
    return num_coins