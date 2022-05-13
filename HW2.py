# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:17:05 2022

@author: Shayla Sexton
"""

def sum_threshold(theta, *nums):
    """
    return the sum of numbers untill it reaches the threshold 

    Args:
        theta : args int that will serves of the threshold
        *nums : args list of numbers

    Returns:
        sum (int): sum of values

    """
    sum = 0;
    if theta and not nums:
        return 0
    else:
        for num in nums:
            sum += num
            if sum > theta:
                sum -= num
                break;
        return sum

    
def my_slice(lst, start=0, length=None, step=2):
    """
    return a editied list of numbers based on the arguments
    
    Args:
        lst : list of numbers
        start : starting position of slice
        length : length value for the slice
        step : value to space between elements included in new slice

    Returns:
        (list): list from sliced lst

    """
    return lst[start:length:step]
    
def with_factors(lst, factors):
    """
    return a new list with all the numbers from lst that have atleast one factor

    Args:
        lst :  list of nums
        factors : list of factors

    Returns:
        (list): list of numbers that have a factor in the facotrs list

    """ 
    
    def has_factor(x, fact):
        """
        Checks if a number has a factor

        Args:
            x :  a number
            fact : a factor

        Returns:
            (boolean): True or False if the number has that factor

        """ 
        if x%fact == 0:
            return True
        else:
            return False
            
    new_list = []
    for num in lst:
        for factor in factors:
            if has_factor(num, factor):
                new_list.append(num)
                break      
    return new_list

####################
#return listfilter(lambda z: has_factor(z, fcts), ls)()
                
                 
def pairs_factors(lst):
    """
    will make a list of tuples contained with the num and its factors in the same list

    Args:
        lst :  a list of number

    Returns:
        pf_list (list): list of tuples

    """ 
    pf_list = []
    s = ()
    for num in lst:
        factor_list = []
        for fact in lst:
            if num != fact and fact != 0 and fact != 1:
                if num%fact == 0:
                    factor_list.append(fact)
            s = (num, factor_list)
        pf_list.append(s)
    return pf_list
    
            
    

lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('The sum of the elements, left to right, without exceeding the')
print('threshold 40 is ', sum_threshold(40, *lst))
print('The same but with a threshold of 70: ', sum_threshold(70, *lst))
print('With an empty list of numbers: ', sum_threshold(50))
print('my_slice(lst): ', my_slice(lst))
print('my_slice(lst, start=2, step=1): ', my_slice(lst, start=2, step=1))
print('my_slice(lst, start=2, length=5): ', my_slice(lst, start=2, length=5))
print('my_slice(lst, length=5): ', my_slice(lst, length=5))
print('with_factors(lst, [2, 5]): ', with_factors(lst, [2, 5]))
print('pairs_factors(lst): ', pairs_factors(lst))

