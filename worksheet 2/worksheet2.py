"""
Instructions

1) First run test.py: They should automatically fail
2) Here you are given a couple of functions that need to be filled in
3) Then you will run the test.py file from your terminal (linux) or command line (windows). If you filled in everything correctly,
then all the testcases should pass

Do not alter the file structure!!!
"""



def n_sum(n: int) -> int:
    """
    Use for loops to get the sum of first n numbers

    example:
    if n = 4, return 1 + 2 + 3 + 4, or return 10
    if n = 10, return 1+2+3+4+5+6+7+8+9+10, or return 55
    """
    # Add code here
    nsum = 0
    for i in range(n+1): #answer should be 3
        nsum = i + nsum
    return nsum

def n_cubes(n: int) -> int:
    """
    Use for loops to calculate and return the first n cubes

    example:
    if n = 3, return a list [1, 8, 27]
    if n = 5, return a list [1, 8, 27, 64, 125]
    """
    # Add code here
    cube_a = []
    for i in range (1, n+1): 
        cube_a.append(i**3)
    return cube_a

def string_concatenation(a: str, b: str) -> str:
    """
    Concatenation is a synonym for joining. write a function to concatenate two strings
    example:

    string_concatenation('ab', 'cd') should return 'abcd'
    string_concatenation('poke', 'mon') should return 'pokemon'
    """
    # Add code here
    return a+b

def is_even(a: int) -> bool:
    """
    Write a function that check if a number is even or not

    Example:
    is_even(4) should return True
    is_even(308237049) should return False
    """
    # Add code here
    if a%2 == 1:
        return False
    else:
        return True

def first_n_divisible_numbers(n: int, m: int) -> None:
    """
    given 2 integers n and m, return the first n integers that are also divisible by m

    example:
    if n= 3, m= 5, then you have to return [5, 10, 15]
    if n=7, m= 9, then you have to return [9,18,27,36,45,54,63]
    """
    # Add code here
    ans = []
    for i in range (1, n+1):
        ans.append(i*m)
    return ans

