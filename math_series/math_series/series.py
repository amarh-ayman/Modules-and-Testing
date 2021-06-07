'''
fibonacci equation
'''
def fibonacci(num):
        if num<=1:
           return num
        else :
           return fibonacci(num-1)+fibonacci(num-2)
    
     
'''
lucas equation
'''
def lucas(num):
    if num==0 :
            return 2
    if num==1:
           return num
    else :
           return lucas(num-1)+lucas(num-2)

'''
sum series for any series 
'''

def sum_series(num ,a=0,b=1):
        if num==0 :
            return a
        if num==1:
           return b
        else :
           return sum_series(num-1,a,b)+sum_series(num-2,a,b)
    