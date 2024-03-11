#Lê uma frase e mostra quantas vezes aparece a letra "A". Em que posição ela aparece pela primeira vez. Em que posição ela aparece pela última vez

frase = input('Digite uma frase: ').strip()
print(frase.lower().count('a'))
print(frase.lower().find('a')) # .find mostra quando a letra 'a' aparece pela primeira vez 
print(frase.lower().find('a', -1))