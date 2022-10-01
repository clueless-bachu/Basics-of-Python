"""
Instructions

1) First run test.py: They should automatically fail
2) Here you are given a couple of functions that need to be filled in
3) Then you will run the test.py file from your terminal (linux) or command line (windows). If you filled in everything correctly,
then all the testcases should pass

Do not alter the file structure!!!
"""

## Basic Operators

def add(a: int, b: int) -> int:
    '''
    This function takes 2 integers a and b. It then returns the sum.
    '''

    # Add code here 
    return a+b

def subt(a: int, b: int) -> int:
    '''
    This function takes 2 integers a and b. It then returns the difference.
    '''

    # Add code here
    
    return a-b

def mult(a: int, b: int) -> int:
    '''
    This function takes 2 integers a and b. It then returns the product.
    '''

    # Add code here
    return a*b

def div(a: int, b: int) -> int:
    '''
    This function takes 2 integers a and b. It then returns the quotient.
    what would you do if the divisor b is zero?
    if divisor is zero, return 0
    '''

    # Add code here
    if b == 0:
        return 0
    else:
        return a/b


def and_gate(a: bool, b: bool) -> bool:
    '''
    Implement AND gate for inputs a and b.
    '''

    ## add code here
    and_res1 = a and b
    return and_res1
    

def or_gate(a: bool, b: bool) -> bool:
    '''
    Implement OR gate for inputs a and b.
    '''

    ## add code here
    return a or b

def xor_gate(a: bool, b: bool) -> bool:
    '''
    Implement XOR gate for inputs a and b.
    '''

    ## add code here
    return a ^ b
