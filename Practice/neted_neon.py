for i in range(0,1000):
    sqr=i**2
    sum = 0
    while sqr > 0:
        sum = sum + sqr%10
        sqr = sqr//10
    if sum==i:
        print(i,end=" ")
