class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
        number = 0
        for i in range(len(s) - 1): #IV is passed len() is 2;
            if roman[s[i]] < roman[s[(i + 1)]]: #IV, 1 < 5
                number = number - roman[s[(i)]]# num = 0 - 1
            else :
                number = (number + roman[s[i]])# VI, 5! < 1, num = 0 + 5-- > on i = 1(2 nd itr) wont happens as only two char
        return number + roman[s[-1]]# 5 + 1


#Dry Run, s=XVI , X is 10 ,V is 5 and I is 1
# so i will iterate 2 times only as (len-1)
# first itr ,   X < V is false so else condition will run , num=0+10
#2nd itr , V < I is false so if condition , num=10+5, 15
#returns 4+roman[s[-1]] which is 15+1 give 16
