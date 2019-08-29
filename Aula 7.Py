'''def mensagemDeErro():
    """Função chamada sempre que houver um erro"""
    print("Erro!!!")
    print("Infelizmente você terá que fazer tudo novamente")
    print("Nada do que você fez está certo!!! :(")

mensagemDeErro()
mensagemDeErro()
mensagemDeErro()
mensagemDeErro()'''

'''def arbitrary(x,y,*more):
    """Função com dois ou mais parametros"""
    print("x = ", x, ", y = ", y)
    print("Parametros arbitrarios: ", more)

arbitrary(2,3)
arbitrary(2,3,"oi","xau")'''

'''def nomesPaises(paises = "Noruega"):
    print("Eu vim da: ", paises)

    nomesPaises("Venezuela")
    nomesPaises()'''

'''def listaDeComidas(comidas):
    """Programa para imprimir a lista de comidas passadas"""
    for comida in comidas:
        print(comida)

listaDeComidas(["Banana", "Maçã", "Pera", "Abacaxi"])'''

def recursao(k):
    if(k > 0):
        resultado = k + recursao(k-1)
        print(resultado)
    else:
        resultado = 0
    return resultado

recursao(6)