# !/usr/bin/env python3
# #fibonacci sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
# #prints out fibonacci sequence 
# #formula 
# #Xn = Xn-1 + Xn-2
def print_fibonacci(length):
    if length <= 0:
            print([]) 
    elif length ==1: 
        print ([0])
    elif length == 2: 
        print ([0,1]) 
    else:
        fibo_list= [0, 1]
        for _ in range(2,length):
            fibo_list.append(fibo_list[-1]+ fibo_list[-2])
        print(fibo_list)
      
print_fibonacci(9)






