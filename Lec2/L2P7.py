def sqrt_3():
    c = 10
    g = c / 3
    i = 0
    while(abs(g**3-c)>0.00000000001):
        g = (2*(g**3) + c)/(3*(g**2))
        i = i+1
        print ("%d:%.13f"%(i,g))

sqrt_3()