'''num = input('Digite um número:')
print(num)

login = input("Login:")
senha = input("Senha:")

print("O usuário informado foi: %s, e a senha digitada foi: %s" %(login, senha))'''

'''varLogica = input("Você é uma pessoa inteligente?")

if varLogica:
    print("Não deixe o trabalho para depois!!")

print("FIm de programa")'''

'''botao1Apertado = int(input("O rato apertou o botão 1?/n"))
botao2Apertado = int(input("O rato apertou o botão 2?/n"))

if (botao1Apertado and not botao2Apertado):
    print("Foram adicionados 10 mg de comida")
if (not botao1Apertado and botao2Apertado):
    print("Foram adicionados 20 mg de comida")
if (not botao1Apertado and not botao2Apertado):
    print("Nenhuma comida foi adicionada")
if (botao1Apertado and botao2Apertado):
    print("Foram adicionados 40 mg de comida")

print("Fim de programa!!!")'''

strLazy        = input("Você é uma pessoa preguiçosa? ")
strIntelligent = input("Você é uma pessoa inteligente? ")

if(strLazy == "n" and strIntelligent == "n"):
    print("Você não é preguiçoso nem inteligente\n")
if(strLazy == "n" and strIntelligent == "s"):
    print("Você não é preguiçoso, mas é inteligente\n")
if(strLazy == "s" and strIntelligent == "n"):
    print("Você é preguiçoso, mas não inteligente\n")

print("Fim do programa")
