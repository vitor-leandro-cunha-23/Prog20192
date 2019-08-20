'''Verificar idade, já que o IMC é uma medida destinada
 a adultos com idade de 20 a 59 anos'''

idade = float(input("Digite sua idade:"))
if idade < 20:
    print('Você ainda não é adulto (a), o cáuculo de IMC não se aplica a sua faixa etária.')
    
else:
    print('Vixiiiii, tá ficando velhinha (o).')
    print ('\U0001F605')
    print ('Caso queira verificar seu Índice de Massa Corporal (IMC), fique à vontade')

def menu():    
    print('0 = Sair\n1 = Calcular IMC\n2 = Classificação IMC')
    return int(input('Entre com a opção desejada:'))

'''Criação do menu para escolha por parte do usuário
Adicionei 3 opções: Sair, caucular IMC 
e Classificação do IMC'''

while True:
    opcao = menu()

    if opcao == 0:
        print ('Tchau!')
        break;

    elif opcao == 1:    
         altura = float(input('Entre com sua altura:'))  
         peso = float(input('Entre com seu peso:'))  
         imc = peso/(altura * altura)  
         print('Seu índice de massa corporal é {:.2f}'.format(imc)) 

    elif opcao == 2:
        if imc < 18.5:
            print("Você se encontra com baixo peso.")
        elif imc > 18.5 and imc < 25:
            print("Parabèns, seu peso está adequado.")
        elif imc > 25 and imc < 30:
            print("Xiiii você está com sobrepeso.")
        elif imc > 30:
            print("Melhor pensar em atividades físicas, você está obeso (a) :(")

