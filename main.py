# 1- imports / biblioteca

# 2- Classe

# 3- Métodos e funções
#def = definition = definição
def print_hi(name):
    print(f'Oi,{name}')  # a partir do Python 3
    print('Oi,'+ name)  # antes do Python 3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_progressiva(fim):
    for numero in range(fim):  # repetir o bloco de zero até o fim
        print(numero) # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1 #contador recebe numero+1
        #print(f'{contador} - {nome}')

        if numero < 9: # acrescentar 0 na numeração de 1 a 9 p ficar alinhado
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(numero + 1, '-', nome) #pode retirar as linhas 26 e 27 e substitui por essa linha de codigo

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM')
        else:
            print('{:0>3}'.format(numero))

# estrutura de identificação / execução do script
if __name__ == '__main__':
    print_hi('José')

    # chamar a função de calculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A area do retângulo é de {resultado} m²')

    # chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A area do quadrado é de {resultado} m²')

    #chamar a função de calculo da area do triângulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A area do triângulo é de {resultado} m²')

    #executar uma contagem progressiva
    contagem_progressiva(11)

    # exibir o nome do candidato varias vezes
    apoiar_candidato('Faker', 100) #chama o nome da função apoiar candidato, passa o texto com aspa simples e 10 numero de vezes

    #brincar de plim
    brincar_de_plim(100)