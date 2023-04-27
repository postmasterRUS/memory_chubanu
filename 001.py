def f(x,y,a):
    return (x+2*y>=240) or (a>2*x) and (y<=a)
for a in range(0,1000):
    if all (f(x,y,a)==1 for x in range(0,500) for y in range(0,500)):
        print(a)
        break
