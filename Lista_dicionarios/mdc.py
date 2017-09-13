def mdc(m, n):
    while(m % n != 0):
        resto = m % n
        m = n
        n = resto 
        
    return n