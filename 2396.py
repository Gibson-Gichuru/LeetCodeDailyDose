"""An Integer n is strictly palindromic if, for every base b between 2 and n-2 (inclusive), the string representation of the 
integer n in base b is palindromic.
Given an integer n, return true if n is strictly palindromic and false otherwise


A string is palindromic if it reads the same forward and backward   


Example 1:

input n = 9

Output: False

Explanation we only consider base 2: 4 - 100 (base 2), which is not palindromic Therefore, we return false


constraints:

4 <= n <= 10^5"""

import math


def isStrictlyPalindromic(n:int) -> bool:

    # we want to return true if for all base representation of n is palindromic

    # to represent our number n in base 2 to n-2 we need to get the highest power of a base 
    # that is less than or equal to n 
    # thus k = log(b) thus string

    results : list[bool] = []

    for i in range(2, n-2):

        if representation(n, i) != representation(n, i)[::-1]:
            results.append(False)
            continue
        
        results.append(True)
        
    return all(results)


def representation(n: int, base: int) -> str:

    highest_power =math.floor(math.log(n,base))

    return f"{n - math.pow(base, highest_power)}{highest_power}"


a : bool = isStrictlyPalindromic(9)

b: bool = isStrictlyPalindromic(4)

print(f"a: {a}")
print(f"b: {b}")