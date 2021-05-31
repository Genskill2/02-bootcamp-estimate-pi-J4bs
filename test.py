def wallis(n):
     x = 1
     pi = 1 
     while (x<n):
      pi = pi * ((4*x*x)/((4*x*x)-1))
      x+=1
     return (2 * pi)