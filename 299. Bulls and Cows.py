# You are playing the following Bulls and Cows game with your friend:
# You write down a number and ask your friend to guess what the number is.
# Each time your friend makes a guess, you provide a hint that indicates
# how many digits in said guess match your secret number
# exactly in both digit and position (called "bulls") and
# how many digits match the secret number but locate in the wrong position (called "cows").
# Your friend will use successive guesses and hints to eventually derive the secret number.
# For example:
# Secret number:  "1807"
# Friend's guess: "7810"
# Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
# Write a function to return a hint according to the secret number and friend's guess,
# use A to indicate the bulls and B to indicate the cows.
# In the above example, your function should return "1A3B".
# Please note that both secret number and friend's guess may contain duplicate digits, for example:
# Secret number:  "1123"
# Friend's guess: "0111"
# In this case, the 1st 1 in friend's guess is a bull,
# the 2nd or 3rd 1 is a cow, and your function should return "1A1B".
# You may assume that the secret number and your friend's guess only contain digits,
# and their lengths are always equal.
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        cs, cg = [0]*10, [0]*10
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
            else:
                cs[int(secret[i])] += 1
                cg[int(guess[i])] += 1
        for i in range(10):
            B += min(cs[i], cg[i])
        return str(A)+'A'+str(B)+'B'
        # 使用1个数组
        A = B = 0
        c = [0]*10
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                A += 1
            else:
                c[int(secret[i])] += 1  # 如果secret对应的数没猜中，应该是正数
                if c[int(secret[i])] <= 0:
                    B += 1
                c[int(guess[i])] -= 1   # 如果guess没猜中，guess对应的数应该是负
                if c[int(guess[i])] >= 0:
                    B += 1
        return str(A)+'A'+str(B)+'B'