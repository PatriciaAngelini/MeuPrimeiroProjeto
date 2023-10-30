# Aula7
#Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se são iguais;
print('Comparação entre números')
n1 = float(input('Entre com o primeiro numero '))
n2 = float(input('Entre com o segundo numero '))

# n1 == n2
# n1 > n2
# n1 < n2

if (n1==n2):
  print('Números iguais')
elif (n1>n2):
  print(f'{n1} é maior que {n2}')
  print(n1, 'é maior que', n2)
  print(str(n1) + ' é maior que ' + str(n2))
else:
  print(f'{n2} é maior que {n1}')


#Utilize o FOR e elabore um algoritmo que imprima todos os números de 250 a 500.
print('Numeros de 250 a 500')
#for
for num in range(250,501,1): #range (comeco, final sem o ultimo numero, pulos)
  print(num)
for num in range(250,501,15): #range (comeco, final sem o ultimo numero, pulos)
  print(num)
for num in range(250,500+1,50): #range (comeco, final sem o ultimo numero, pulos)
  print(num)
for num in range(500,250-1,-50): #range (comeco, final sem o ultimo numero, pulos)
  print(num)
#while
num = 250
while num <= 500:
  print(num)
  num = num + 1
num = 250
while num <= 500:
  print(num)
  num = num + 15
num = 500
while num >= 250:
  print(num)
  num = num - 50

# Faça um algoritmo que leia um valor inteiro e imprima o dobro do seu valor até que esse valor seja maior ou igual a 1000 
# exemplo, com o numero 5, seria 5, 10, 20, 40, 80 até 1000
# exemplo, como numero 100 seria, 100, 200, 400, 800 


# ler um numero inteiro - input e nao posso esquecer a conversao para int
# o numero é o começo da minha repeticao
# o final da minha repeticao é o 1000

# quando eu não sei ao certo o numero de vezes que eu eu vou executar a repeticao o mais indicado é o comando while
print('Os dobros até 1000')
num = int(input('Entre com um numero '))

if (num<0) or (num>100):
  print('Erro, o numero deve ser positivo e menor igual a 1000')
while num <= 1000:
  num = num * 2
  if num <= 1000: 
    print(num)

while num*2 <= 1000:
  num = num * 2
  print(num)

if (num>=0) and (num<=100):
  while num <= 1000:
    print(num)
    num = num * 2
else: 
  print('Erro, o numero deve ser positivo e menor igual a 1000')

#Luis Henrique
n = int(input('Digite um numero: '))
print(n)
while n < 1000:
    n = n * 2
    print(n)

# Elabore um algoritmo que leia um número e imprima a soma dos números múltiplos de 5 no intervalo entre 1 e o número informado. Verifique se o número lido é maior que zero

# pedir um numero inteiro
# verificar se ele e maior que 1
# multiplo de 5? resto da divisao por 5 é 0
# quando isso acontecer eu preciso somar
# pulos podem ser de 1 em 1 ou de 5 em 5 se o primeiro numero for um multiplo de 5
print('Soma dos multiplos de 5')
num = int(input('Entre com um numero '))
i = 1
soma = 0
if num > 1:
  #while
  while i <= num:
    if (i%5 == 0): # not(i%5)
      soma = soma + i
    i = i + 1 # i += 1 
  print(soma)
else:
  print('O numero deve ser maior que 1')

#for
#Luis Henrique
num = int(input('Digite um numero: '))
soma=0
if num > 0 :
    for n in range(1, num+1):
        if n % 5 == 0:
                soma = soma + n
    print(soma)
else:
    print('Numero invalido.')