# Trabalho 3 - LLP

# Nome: João Marcos Silva Hess
# Prof: Diego Ascanio
# Disciplina: Laboratório de Linguagens de Programação

# Questão 1:

def potencia(base, expoente):
    if expoente == 0:
        return 1
    elif expoente == 1:
        return base
    else:
        return base * potencia(base, expoente - 1)

resultado = potencia(2, 3)
print(" ")
print("Questão 1: ")
print(resultado)  



# Questão 2:

def soma_impares(lista):
    if not lista:         
        return 0
    elif lista[0] % 2 != 0:  
        return lista[0] + soma_impares(lista[1:])  
    else:
        return soma_impares(lista[1:])  

resultado = soma_impares([1, 3, 2, 7, 4, 6, 5])
print(" ")
print("Questão 2: ")
print(resultado) 

# Questão 3:

def substituir(lista, antigo, novo):
    if not lista: 
        return []
    elif lista[0] == antigo: 
        return [novo] + substituir(lista[1:], antigo, novo)  
    else:
        return [lista[0]] + substituir(lista[1:], antigo, novo)  

resultado = substituir([1, 2, 1, 3, 1], 1, 0)
print(" ")
print("Questão 3: ")
print(resultado)  



# Questão 4:

def primo(n, div=2):
    if n <= 1:
        return False
    elif n == div:
        return True
    elif n % div == 0:
        return False
    else:
        return primo(n, div + 1)

# Exemplos:
print(" ")
print("Questão 4: ")
print(primo(17))  # True
print(primo(9))  # False

# Questão 5:

def binario(n):
    if n <= 0:
        return []
    else:
        return binario(n // 2) + [n % 2]

# Exemplo
print(" ")
print("Questão 5: ")
print(binario(20))  

# Questão 6:

def soma_divisores(n, div=1):
    if n == div:
        return 0
    elif n % div == 0:
        return div + soma_divisores(n, div + 1)
    else:
        return soma_divisores(n, div + 1)

def perfeito(n):
    return n == soma_divisores(n)

# Exemplo 
print(" ")
print("Questão 6: ")
print(perfeito(28))  

# Questão 7:

def distintos(lista):
    if not lista:
        return True  
    else:
        if lista[0] in lista[1:]:
            return False 
        else:
            return distintos(lista[1:])  

# Exemplos
print(" ")
print("Questão 7: ")
print(distintos([1, 2, 4, 2, 5]))  # False
print(distintos([3, 2, 1]))       # True

# Questão 8:

def distintas(lista1, lista2):
    if not lista1:
        return True     
    elif lista1[0] in lista2:
        return False  
    else:
        return distintas(lista1[1:], lista2)  

# Exemplos
print(" ")
print("Questão 8: ")
print(distintas([1, 2, 3], [4, 5, 6, 0]))  # True
print(distintas([1, 2, 3], [3, 4, 5]))    # False

# Questão 9:

def palindromo(lista):
    if len(lista) <= 1:
        return True  
    else:
        if lista[0] == lista[-1]:
            return palindromo(lista[1:-1])  
        else:
            return False  

# Exemplos
print(" ")
print("Questão 9: ")
print(palindromo([1, 2, 3, 4, 3, 2, 1]))  # True
print(palindromo([1, 2, 3, 4, 5, 6]))    # False



# Questão 10:
 
def somaParciais(lista):
    if not lista:
        return []  
    elif len(lista) == 1:
        return [lista[0]]  
    else:        
        return [lista[0]] + [lista[0] + x for x in somaParciais(lista[1:])]

# Exemplos
print(" ")
print("Questão 10: ")
resultado = somaParciais([1, 2, 3, 4])
print(resultado)  


# Questão 11:

def linearizar(lista):
    if not lista:
        return []  # Lista vazia
    else:
        return lista[0] + linearizar(lista[1:])  

# Exemplo
print(" ")
print("Questão 11: ")
print(linearizar([[1, 2], [5], [0, 4, 2]])) 



# Questão 12:

def shift(k, lista):
    if k <= 0:
        return lista
    else:
        return shift(k - 1, lista[1:] + [lista[0]])

# Exemplo
resultado = shift(3, [1, 5, 6, 7, 3, 4, 1])
print(" ")
print("Questão 12: ")
print(resultado)  

# Questão 13:

def removerFim(n, lista):
    if n <= 0:
        return lista
    else:
        return removerFim(n - 1, lista[:-1])

# Exemplo
resultado = removerFim(2, [1, 2, 3, 4, 5, 6])
print(" ")
print("Questão 13: ")
print(resultado)  

# Questão 14:

def intercalar(lista1, lista2):
    if not lista1:
        return lista2
    elif not lista2:
        return lista1
    elif lista1[0] < lista2[0]:
        return [lista1[0]] + intercalar(lista1[1:], lista2)
    else:
        return [lista2[0]] + intercalar(lista1, lista2[1:])

# Exemplo
resultado = intercalar([1, 5, 10], [2, 7, 9, 20, 25])
print(" ")
print("Questão 14: ")
print(resultado) 

# Questão 15:

def trocar(valor):
    if valor == 0:
        return []
    elif valor >= 100:
        return trocar(valor - 100) + [100]
    elif valor >= 50:
        return trocar(valor - 50) + [50]
    elif valor >= 10:
        return trocar(valor - 10) + [10]
    elif valor >= 5:
        return trocar(valor - 5) + [5]
    else:
        return trocar(valor - 1) + [1]

# Exemplo 
resultado = trocar(162)
print(" ")
print("Questão 15: ")
print(resultado)  





