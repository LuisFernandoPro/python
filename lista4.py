#Exercício Fix40

def calculo_salario(salario):
    if salario <= 1500:
        return salario * 1.2
    elif 1500 < salario < 2500:
        return salario * 1.1
    else:
        return salario * 1.05

salario_atual = float(input("Digite o valor do seu salário: "))
novo_salario = calculo_salario(salario_atual)

print("")
print(f"Seu novo salário é: R${novo_salario:.2f}")
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

#Exercício Fix41

def calculo_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número inteiro positivo: "))
resultado_fatorial = calculo_fatorial(numero)

print("")
print(f"O fatorial de {numero} é: {resultado_fatorial}")
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

#Exercício Fix42

def calculo_nota():
    contador = 1
    maior_nota = float(input("Digite a nota do aluno 1: "))

    while contador < 5:
        nota = float(input(f"Digite a nota do aluno {contador + 1}: "))
        if nota > maior_nota:
            maior_nota = nota
        contador += 1

    return maior_nota

maior_nota_turma = calculo_nota()

print("")
print(f"A maior nota da turma é: {maior_nota_turma}")
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

#Exercício Fix43

def calculo_imc():
    peso = float(input("Digite o peso da pessoa: "))
    altura = float(input("Digite a altura da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ").upper()

    imc = peso / altura ** 2

    if sexo == 'F':
        if imc < 19:
            return "Abaixo do peso"
        elif 19 <= imc < 24:
            return "Peso ideal"
        else:
            return "Acima do peso"
    elif sexo == 'M':
        if imc < 20:
            return "Abaixo do peso"
        elif 20 <= imc < 25:
            return "Peso ideal"
        else:
            return "Acima do peso"
    else:
        return "Sexo não reconhecido"

resultado_imc = calculo_imc()

print("")
print(f"A pessoa está: {resultado_imc}")
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

#Exercício Fix44

def calculo_media():
    nome_aluno = input("Digite o nome do aluno: ")
    nota_p1 = float(input("Digite a nota da avaliação 1: "))
    nota_p2 = float(input("Digite a nota da avaliação 2: "))

    media_aproveitamento = (nota_p1 * 4 + nota_p2 * 6) / 10

    if 9 <= media_aproveitamento <= 10:
        conceito = 'A'
        situacao = 'APROVADO'
    elif 7 <= media_aproveitamento < 9:
        conceito = 'B'
        situacao = 'APROVADO'
    elif 3 <= media_aproveitamento < 7:
        conceito = 'C'
        situacao = 'EXAME'
    elif 0 <= media_aproveitamento < 3:
        conceito = 'D'
        situacao = 'DP'
    else:
        conceito = ''
        situacao = 'SITUAÇÃO INDEFINIDA'

    return f"Aluno: {nome_aluno}\nMédia de Aproveitamento: {media_aproveitamento:.2f}\nConceito: {conceito}\nSituação: {situacao}"

resultado = calculo_media()

print("")
print(resultado)
print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

#Exercício Fix45

def autenticacao():
    usuario = input("Digite o nome de usuário do professor: ")
    senha = input("Digite a senha do professor: ")

    if usuario == "sergio medina" and senha == "senha123":
        return True
    else:
        return False

def calculo_media():
    nome_aluno = input("Digite o nome do aluno: ")
    nota_p1 = float(input("Digite a nota da avaliação 1: "))
    nota_p2 = float(input("Digite a nota da avaliação 2: "))

    media_aproveitamento = (nota_p1 * 4 + nota_p2 * 6) / 10

    if 9 <= media_aproveitamento <= 10:
        conceito = 'A'
        situacao = 'APROVADO'
    elif 7 <= media_aproveitamento < 9:
        conceito = 'B'
        situacao = 'APROVADO'
    elif 3 <= media_aproveitamento < 7:
        conceito = 'C'
        situacao = 'EXAME'
    elif 0 <= media_aproveitamento < 3:
        conceito = 'D'
        situacao = 'DP'
    else:
        conceito = ''
        situacao = 'SITUAÇÃO INDEFINIDA'

    return f"Aluno: {nome_aluno}\nMédia de Aproveitamento: {media_aproveitamento:.2f}\nConceito: {conceito}\nSituação: {situacao}"

autenticado = autenticacao()

if autenticado:
    resultado = calculo_media()
    print(resultado)
else:
    print("Acesso não autorizado.")

print("")
print("Luís Fernando Pires da Cruz, 1050292321022, 1 Semestre de redes")

# questionario

# 1 c) O código não funciona!
# 2 b) AndreSteves
# 3 a) Verdadeiro
# 4 b) O trecho de código onde a variável tem um determinador valor.
# 5 a) Uma variável temporária que é usada apenas dentro de uma função.
# 6 b) Sim, mas é não considerado uma boa prática.


