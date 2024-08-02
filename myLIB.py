### Created a Cutsom Library to export Methods directly for Practice  
def Total(Lst):
    cout = 0
    for i in Lst:
        cout = cout + i
    return cout
    
def Min(m):
    minim = min(m)
    return minim

def Max(m):
    maxim = max(m)
    return maxim 

def f2c(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0