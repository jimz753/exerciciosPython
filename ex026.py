frase = input('Digite uma frase qualquer: ').strip()
f = frase.upper()
a = f.count('A')
p = f.find('A')
u = f.rfind('A')
print ('A letra "a" aparece {} vezes, a primeira vez é a {}ª posição e a última é a {}ª posição nesta frase'.format(a,p+1,u+1))