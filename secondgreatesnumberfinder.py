def secondGreatest(list):
    counterOne = 0
    counterTwo = 0
    for x in list:
        if x > counterOne:
            counterTwo = counterOne
            counterOne = x
        elif x > counterTwo and x != counterOne:
            counterTwo = x
    return counterTwo

print (secondGreatest([5, 10, 1, 8])) 
