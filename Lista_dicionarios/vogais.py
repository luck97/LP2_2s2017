def aeiou(texto):
    qtdvogais = 0
    #variáveis
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    vog = {
        a : 0, 
        e : 0,
        i : 0,
        o : 0, 
        u : 0 
    }
    
    for letra in texto:
        if vog.__contains__(letra):
            qtdvogais = qtdvogais + 1
            if letra == 'a':
                a += 1
            if letra == 'e':
                e += 1
            if letra == 'i':
                i += 1
            if letra == 'o':
                o += 1
            if letra == 'u':
                u += 1
    vog = [a] = a
    vog = [e] = e
    vog = [i] = i
    vog = [o] = o
    vog = [u] = u         
    return qtdvogais 

txt = str(input("Digite um texto: "))
print("A quantidade de vogais no texto: ", aeiou(txt))