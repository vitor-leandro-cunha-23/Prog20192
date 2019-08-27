
def menu():    
    print('\n1 = Habituação\n2 = Distância\n3 = Toque\n4 = Discriminação som\n5 = Sair')
    return int(input('\nEntre com a opção desejada:'))

'''Criação do menu para escolha por parte do usuário'''

while True:
    opcao = menu()

    if opcao == 1:
        Habituação = int(input('Como está o seu sagui?\n[ 0 ] Habituado\n[ 1 ] Não Habituado\n'))
        0
        print('O animal está apto para ir a próxima fase!\nSeguir para fase 2.')

    elif opcao == 2:    
        Distância = int(input('Distância do animal até a barra:'))  
        if Distância <= 30:
            print('Liberada recompensa.')
            print('Seguir para próxima fase.')
            print('Prossiga para etapa 3!')
        else: 
            print('Não prossiga,repita até conseguir a distância desejada.')

    elif opcao == 3:
        Toque = int(input('Quantas vezes seu sagui tocou na barra?'))
        if Toque >= 20:
            print('Liberada recompensa')
            print('Seguir para próxima fase.')
            print('Prossiga para etapa 4!')
        else:
            print('Não prossiga,repita até conseguir a quantidade de toques necessários.')
    
    elif opcao == 4:    
            print('Suas opções de som e barra: ')
            print('1-Som 1: Phi')
            print('2-Som 2: Trill')
            print('3-Barra direita')
            print('4-Barra esquerda')
            som = int(input('Digite o som reproduzido: '))
            Barra = int(input('Qual barra foi tocada: '))
            if som == 1 and Barra == 4:
                print('Recompensa liberada!')
            elif som == 2 and Barra == 3:
                print('Recompensa liberada!')
            else:
                print('Repetir o teste até que seja descriminado o som/barra.')

    elif opcao == 5:    
        print('Fim do programa, até a próxima!')
        break;