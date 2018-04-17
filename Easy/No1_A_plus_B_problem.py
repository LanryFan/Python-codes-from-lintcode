"""
Problem description:
A plus B, but you can't use '+'.
"""

class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here
        if a==0:
            return b
        elif b==0:
            return a
        sum=a&b
        b=a^b
        a=sum<<1
        while a:
            sum=a&b
            b=a^b
            a=sum<<1
        return b
