#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#http://py4e-data.dr-chuck.net/regex_sum_42.txt
import re
sum = 0
i = 0
y = list()
hand = open ('regex_sum_367631.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    y = x + y
for z in y :
    sum = sum + int (z)
print(sum)
