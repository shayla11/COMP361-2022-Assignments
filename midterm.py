#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 11:28:36 2022

@author: shayla
"""




def max_lists(l1, l2):
    l3 = [max(l1, l2) for l1, l2 in zip(l1, l2)]
    return l3
    
    









"""if __name__ == "__main__":
    ls1 = [3,9,2,7,5,6]
    ls2 = [4,8,3,6,6,5]
    print(max_lists(ls1, ls2))
    
#[4, 9, 3, 7, 6, 6]
"""








class Car:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = 0
        
    def __str__(self):
        return "A car of capacity " + str(self.capacity)
    
    def add_passengers(self,num_pas):
        self.num_pas = num_pas
        try:
            if self.num_pas+self.passengers >= self.capacity: #forgot to add the "plus passengers to it :("
                raise Exception("Capacity " + str(self.capacity) + " exceed")
            self.passengers += self.num_pas
        except Exception as e:
            print(e)
            







if __name__ == "__main__" :
    c1 = Car(4)
    print(c1)
    c1.add_passengers(2)
    print(c1.passengers)
    try:
        c1.add_passengers(3)
    except Exception as detail:
        print(detail)













def get_float(s):
    p = re.findall('\d+\.\d+',s)    
    if len(p) > 0:
        return float(p[0])
    else:
        return 0.0






"""if __name__ == "__main__":
    n1 = get_float('*** 12.6 ***')
    n2 = get_float('__32.5  6.2__')
    n3 = get_float('  12')
    n4 = get_float('6.25##')
    print(n1, n2, n3, n4)
    print(n1 + n2 + n4)
  
    
#Output    
#12.6 32.5 0.0 6.25
#51.35

"""