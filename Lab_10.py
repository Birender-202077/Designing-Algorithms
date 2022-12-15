def expo(x,n):                                     #helper function
    if n==0:                                       #when power of base is zero
        return 1
    elif n%2==0:                                   #when power is even.
        r=n/2
        a=expo(x,r)
        a=a*a   
    else:
        r=(n-1)/2                                  #when power is odd
        a=expo(x,r)
        a=x*a*a 
    return a    

def is_Prime(n):                                    #main function 
    m=n-1                                           #storing (n-1) in new variable 'm'
    for x in range (2,n):
        e=expo(x,m)
        if e%n!=1:                                  #when remainder is not equals to 1 then return False
            return False
        return True                                 #when remainder equals to 1 then return True.

print(is_Prime(5))      
