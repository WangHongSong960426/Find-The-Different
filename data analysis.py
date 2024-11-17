#data analysis
x = []
y = []
isx = float(0)
isy = float(0)
sxx = float(0)
syy = float(0)
sxy = float(0)

n = int(input("How Many Data are you going to input? "))
if n >=2:
    for i in range (0,n,1):
        print("Input the x", i+1, ": ")
        ix = int(input())
        print("Input the y", i+1, ": ")
        iy = int(input())
        isx = ix + isx
        isy = iy + isy
        x.append(ix)
        y.append(iy)


    iux = isx/n
    iuy = isy/n


    for j in range (0,n,1):
        xn = x[j]
        yn = y[j]
        sxx = (xn-iux)**2+sxx
        syy = (yn-iuy)**2+syy
        sxy = (xn-iux)*(yn-iuy)+sxy

    iux = round(iux,3)
    iuy = round(iuy,3)
    sxy = round(sxy,3)
    sxx = round(sxx,3)
    sxy = round(sxy,3)

    vx = (sxx/n)
    vy = (sxy/n)
    vx = round(vx,3)
    vy = round(vy,3)

    r = sxy/((sxx**0.5)*(syy**0.5))
    r = round(r,3)


    print("There are ", n, "data(s) you input")
    print("The x you input is: ", x)
    print("The y you input is: ", y)
    print("The mean of x is: ", iux)
    print("The mean of y is: ", iuy)
    print("The sum of Squares of Deviations of xy is: ", sxy)
    print("The sum of Squares of Deviations of x is: ",sxx)
    print("The sum of Squares of Deviations of y is: ", syy)
    print("the variance of x is: ", vx)
    print("the variance of y is: ", vy)
    print("The correlation coefficient is: ", r)
    print("I have round some variable to three decimal places!")
else:
    print("Error")