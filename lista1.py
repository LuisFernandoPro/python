
# TP-01(IPE - Python)

# 1) Elaborar um programa que determine qual é 7 elevado na potencias 4?.

pot = 7

calc_pot = 7**4

print("")
print("o resultado da potencia é:",calc_pot)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")


# 2) Elaborar um programa que determine qual a divisão de 21424 dividido por 89.

valor1 = 21424
valor2 = 89

divisao = (valor1 / valor2)

print("")
print("o resultado da divisão é:",divisao)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 3) Elaborar um programa que imprime a string “ Boa noite, Python” de tras para frente, usando
# indexação.

frase = "Boa noite,  Python"

print("")
print("a frase escrita de trás para frente é:",frase[::-1])
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 4) Entrar via teclado com a base e a altura de um retângulo, calcular e exibir sua área.

base = int(input('Digite a base:'))
altura = int(input('Digite a altura:'))

area = (base * altura)

print("")
print("a area do retangulo é:",area)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 5) Calcular e exibir a área de um quadrado, a partir do valor de sua aresta que será digitado.

base = int(input('Digite a base:'))
altura = int(input('Digite a altura:'))

area = (base * altura)

print("")
print("a area do quadrado é:",area)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 6) A partir dos valores da base e altura de um triângulo, calcular e exibir sua área.

base = int(input('Digite a base:'))
altura = int(input('Digite a altura:'))

area = (base * altura / 2)

print("")
print("a area do triangulo é:",area)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 7) Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.

n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))
n3 = int(input('Digite o terceiro numero:'))
n4 = int(input('Digite o quarto numero:'))

ma = ((n1 + n2 + n3 + n4) / 4)

print("")
print("a média aritmética é:",ma)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 8) Entrar via teclado com o valor de uma temperatura em graus Celsius, calcular e exibir sua
# temperatura equivalente em Fahrenheit.

temp = int(input('Digite a temperatura:'))

conversor = (temp * 9/5 + 32)

print("")
print("a temperatura em Fahrenheit é:",conversor)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 9) Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular
# e exibir o valor correspondente em Reais (R$).

quantidade = float(input('Digite a quantidade:'))
valor = float(input('Digite a cotação do dolar:'))

reais = (quantidade * valor)

print("")
print("valor em reais: R$",reais)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 10) Entrar via teclado com o valor de cinco produtos. Após as entradas, digitar um valor referente ao
# pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

prod1 = float(input('Digite o valor do produto1:'))
prod2 = float(input('Digite o valor do produto2:'))
prod3 = float(input('Digite o valor do produto3:'))
prod4 = float(input('Digite o valor do produto4:'))
prod5 = float(input('Digite o valor do produto5:'))
pagamento = float(input('Qual o valor pago:'))

total = (prod1 + prod2 + prod3 + prod4 + prod5)
troco = (pagamento - total)

print("")
print("valor pago:",pagamento, "valor total:",total,"troco:",troco )
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 11) Dona Maria foi comprar uma bolsa. As formas de pagamento que eram oferecidas foram:
# a) A vista com 10% de desconto
# b) Parcelado em 1+2 vezes sem desconto
# c) Dividido em 10 vezes com juros de 5% sobre o valor total

# e 

# 12) Crie um programa que permita informar o valor total da compra e exiba os valores que Dona
# Maria irá pagar no total em cada uma das formas de pagamento e os valores de cada parcela,
# caso a mesma opte por dividir.

bolsa = float(input('Digite o valor da bolsa: '))

desc_vista = (10 * bolsa /100 )
valor_vista = (bolsa - desc_vista)

parce = (bolsa / 3)

juros_divid = (5 * bolsa /100)
acresc = (bolsa + juros_divid)
valor_divid = (acresc / 10)

print("")
print("total a vista:",valor_vista)
print("")
print("total com parcelas:",bolsa)
print("valor individual das 3 parcelas:",parce)
print("")
print("total com divisao:",acresc)
print("valor individual das parcelas:",valor_divid)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 13) Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento. Exiba quantos
# litros o mesmo conseguiu colocar no tanque.


preco = float(input('Quantos reais deseja pagar?: '))
litro = float(input('Qual o preco do litro?: '))

abastecido = (preco / litro)

print("")
print("Voce consegue abastecer: ", abastecido, " litros")
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 14) O restaurante cobra R$23,00 por cada quilo de refeição. Escreva um algoritmo que leia o peso
# do prato montado pelo cliente (em quilos) e imprima o valor a pagar. Assuma que a balança já
# desconte o peso do prato (200 g).

peso = float(input('insira o peso do prato em gramas: '))
balanca = (peso - 200)

preco = (balanca * 0.023)

print("")
print("O valor total é R$:", preco)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 15) Leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a apenas em dias.

anos = int(input('insira a sua idade em anos: '))
meses = int(input('insira sua idade em meses: '))
dias = int(input('insira sua idade em dias: '))

calc_ano = (anos * 365)
calc_meses = (meses * 30)
dias_finais = (calc_ano + calc_meses + dias)

print("")
print("sua idade em dias é: ", dias_finais)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# 16) Leia a idade de uma pessoa expressa em dias e mostre-a em anos, meses e dias.

dias = int(input('insira sua idade em dias: '))

calc_ano = (dias / 365)
calc_meses = (dias / 30)


print("")
print("sua idade em anos é: ", calc_ano)
print("")
print("sua idade em meses é: ", calc_meses)
print("")
print("sua idade em dias é: ", dias)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")
