'''
são blocos de códigos que são executados apenas quando chamados.
Então você define assim:
def nome (parâmetros)
	comando (este comando só é executado quando é chamado)
nome (argumentos) (chamada desta função):
'''

def soma(x,y):
  print(x+y)
soma(2, 3)
print(soma)


#Note que pode ser qualquer operação, +,-, * , /
#Outra opção é utilizar a função RETURN e armazenar a soma como uma variavel

def soma(x, y):
  return x+y
def multiplicacao(x,y):
  return x*y
s = soma(2,3)
m = multiplicacao(3,4)
print(soma(s,m))
#No exemplo acima, foi impresso a soma da varivel s, com a multiplicação da varivel m. Ou seja 5+12 = 17.