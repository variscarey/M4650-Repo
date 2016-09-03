from secfun import secret_func

def bisect(function,left=-100,right=100):
    from math import fabs
    new=.5*(left+right)
    value=function(new)
    print new,value
    if fabs(value) < 1E-1:
        return (new,value)
    else:
        if value > 0:
            return bisect(function,left,new)
        else:
            return bisect(function,new,right)

def newton(function,der,old,value):
    from math import fabs
    next=old-value/der(old)
    value=function(next)
    print next,value
    if fabs(value) < 1E-8:
        return next
    else:
        return newton(function,der,next,value)

    
f=secret_func()
print f.root
root=bisect(f.eval)
print 'Newton time?'
root2=newton(f.eval,f.deriv,root[0],root[1])
#root2=newton(f.eval,f.deriv,100,f.eval(100))



