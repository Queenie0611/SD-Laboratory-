def minmax(data,n):
    if n == 1:
        return data[0],data[0]
    else:
        x ,y= minmax(data, n - 1)
        return data[n - 1] if (data[n - 1] > x) else x, data[n - 1] if (data[n - 1] <y) else y
data=[5,10,15,20,25,30,35,40,45,50]
n,m=minmax(data,9)
print(n,m)