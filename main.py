import numpy as np

# Abstraindo para numeros o objetivo do jogo eh a ordenacao ao fim
# Porem apenas o 5 pode se mover, sendo que numeros menores que 5 nao podem
# ir para a direita e numeros maiores que 5 nao pode ir para a esquerda
primary = [6, 7, 8, 9, 5, 1, 2, 3, 4]
answer = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Checa se o numero deve estar a esquerda do 5
def is_left(number):
    if number < 5:
        return True
    return False


# Movendo o 5
def move(position):
    index_main = primary.index(5)

    index_secondary = index_main + position
    primary[index_main], primary[index_secondary] = primary[index_secondary], primary[index_main]


# Checa qual movimento eh possivel
def possible_move(side):

    index_main = primary.index(5)
    position = 0

    # Movendo o 5 para a esquerda
    if side:
        if index_main == 1:
            position = -1
        elif index_main > 1:
            if not is_left(primary[index_main - 2]) and is_left(primary[index_main - 1]):
                position = -2
            elif not is_left(primary[index_main - 1]):
                position = -1

    # Movendo o 5 para a direita
    else:
        if index_main == 7:
            position = 1
        elif index_main < 7:
            if is_left(primary[index_main + 2]) and not is_left(primary[index_main + 1]):
                position = 2
            elif is_left(primary[index_main + 1]):
                position = 1

    return position


# Checando se ainda eh possivel jogar
def is_valid():
    index_main = primary.index(5)
    right = False
    left = False

    if index_main == 0:
        left = True
    elif index_main == 1 and not is_left(primary[0]):
        left = True
    elif index_main > 1:
        if not is_left(primary[index_main - 2]) and is_left(primary[index_main - 1]):
            left = True
        elif not is_left(primary[index_main - 1]):
            left = True
    if all(is_left(number) for number in primary[0:index_main]):
        left = True

    if index_main == 8:
        right = True
    elif index_main == 7 and is_left(primary[8]):
        right = True
    elif index_main < 7:
        if is_left(primary[index_main + 2]) and not is_left(primary[index_main + 1]):
            right = True
        elif is_left(primary[index_main + 1]):
            right = True
    if all(not is_left(number) for number in primary[index_main:9]):
        right = True

    return right and left


def print_state():
    result = []
    for number in primary:
        if number > 5:
            result.append("R")
        elif number < 5:
            result.append("L")
        else:
            result.append("M")
    print result


def print_final_result(result_states):
    for result in result_states:
        move(result)
        print_state()


def main():
    global primary
    side = True
    result_states = []
    control = 0
    print_state()
    while not np.array_equal(primary, answer):
        # Se eh valido entao a jogada e feita e armazenada
        if is_valid():
            position = possible_move(side)
            if position != 0:
                move(position)
                result_states.append(position)
            else:
                side = not side
        else:
            # Se o jogo chegou ao fim entao a ultima jogada e desfeita
            # E o outro lado eh tentado
            side = not side
            move(-result_states[-1])
            result_states = result_states[:-1]

    # Voltando ao estado inicial para mostrar os resultados
    primary = [6, 7, 8, 9, 5, 1, 2, 3, 4]
    print_final_result(result_states)

if __name__ == "__main__":
    main()
