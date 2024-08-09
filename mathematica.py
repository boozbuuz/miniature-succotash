def mean(*x):
    acum = 0
    for i in x:
        acum += i
    return acum / len(x)