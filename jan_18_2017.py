# Description:

# Write a program that will calculate the number of trailing zeros in a factorial of a given number.

# N! = 1 * 2 * 3 * 4 ... N

# zeros(12) = 2 # 1 * 2 * 3 .. 12 = 479001600
# that has 2 trailing zeros 4790016(00)
# Be careful 1000! has length of 2568 digital numbers.

def zeros(n):
    sum = 0
    count = 1
    while int(pow(5, count)) < n:
        sum += n // pow(5, count)
        count += 1
    return sum

# Description:

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

def move_zeros(array):
    values = []
    zeroes = []
    for val in array:
        if not val and (type(val) == int or type(val) == float):
            zeroes.append(val)
        else:
            values.append(val)
    return values + zeroes


# Description:

# Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:

# solution(1000) # should return 'M'
# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
# Remember that there can't be more than 3 identical symbols in a row.

def solution(n):
    key = {
        0: ('I', 'V', 'X'),
        1: ('X', 'L', 'C'),
        2: ('C', 'D', 'M'),
        3: ('M', '0', '0')
    }
    reverse_num = str(n)[::-1]
    numeral = ''
    for idx, num in enumerate(reverse_num):
        if num == '0':
            continue
        else:
            syms = key[idx]
            numeral = crt_numeral(num, syms[0], syms[1], syms[2]) + numeral
    return numeral

def crt_numeral(val, lo, md, hi):
    key = {
        1: lo,
        2: 2*lo,
        3: 3*lo,
        4: lo + md,
        5: md,
        6: md + lo,
        7: md + 2*lo,
        8: md + 3*lo,
        9: lo + hi
    }
    return key[int(val)]


