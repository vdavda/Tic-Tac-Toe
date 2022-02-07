import random

game_field = [['-' for i in range(10)] for j in range(10)]
count_of_point = {'player': 0,
                  'computer': 0}
chars = ['x', '0']

def print_field():
    '''вывод игрового поля'''
    row = 0
    print(' ',0,1,2,3,4,5,6,7,8,9)
    for i in game_field:
        print(row, end=' ')
        for j in i:
            print(j, end=' ')
        print()
        row += 1


def choise_player_char(chars):
    '''игрок выбирает для себя символ'''
    char = input('Выберите x или 0(x ходит первым): ')
    print()
    while char not in ('x', '0'):
        char = input('Неправильный ввод. Выберите x или 0(x ходит первым): ')
        print()
    index_player = chars.index(char) 
    index_computer = chars.index(char) - 1   

    return chars[index_player], chars[index_computer]


def computer_move(game_field):
    print()
    print('----- ХОД КОМПЬЮТЕРА -----')
    print()
    point = [random.randint(0, 9), random.randint(0, 9)]
    
    while True:
        if cage_is_free(point, game_field):
           game_field[point[0]][point[1]] = computer_char
           break
        else:
            point = [random.randint(0, 9), random.randint(0, 9)]
    return point

def cheсk_input_char(point):
    '''проверка ввода'''
    if len(point) != 2:
        return False
    if point[0] not in ('0123456789') or point[1] not in ('0123456789'):
        return False
    return True

def cage_is_free(point, game_field):
    '''проверяем свободна ли точка'''
    if game_field[point[0]][point[1]] == '-':
        
        return True
    else:
        return False


def player_move(game_field):
    '''ход игрока'''
    print()
    print('----- ХОД ИГРОКА -----')
    print()
    text = {0: 'Введите точку(две цифры от 0 до 9 через пробел):',
            1: 'Точка занята, выберите другую точку (две цифры от 0 до 9 через пробел):',
            2: 'Неправильный ввод. Введите две цифры от 0 до 9 через пробел:'}
    number_text = 0
    while True:
        point = input(text[number_text]).split()
        print()
        if cheсk_input_char(point):
            point = [int(i) for i in point]
            if cage_is_free(point, game_field):
                game_field[point[0]][point[1]] = player_char
                break
            else:
                number_text = 1
                continue
        else:
                number_text = 2
                continue
        
    return point


def check_victory(last_point, game_field):
    '''проверка количества символов по всем направлениям'''
    count_char = chek_horizon(last_point, game_field)

    if count_char >= 5:
         return count_char

    count_char = chek_vertical(last_point, game_field)

    if count_char >= 5:
         return count_char

    count_char = check_diagonal_right(last_point, game_field)

    if count_char >= 5:
         return count_char

    count_char = check_diagonal_left(last_point, game_field)

    return count_char
    

def chek_horizon(last_point, game_field):
    '''проверка горизонталной линии направо'''
    count = 0
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while column + 1 <= 9 and  game_field[row][column+1] == char:
        count += 1
        column += 1
    if count >= 5:
        return count
    '''проверка горизонталной линии налево'''
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while column - 1 >= 0 and  game_field[row][column-1] == char:
        count += 1
        column -= 1
    return count + 1

def chek_vertical(last_point, game_field):
    '''проверка вертикальной линии вниз'''
    count = 0
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row + 1 <= 9 and  game_field[row+1][column] == char:
        count += 1
        row += 1
    
    if count >= 5:
        return count
    '''проверка вертикальной линии вверх'''
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row - 1 >= 0 and  game_field[row-1][column] == char:
        count += 1
        row -= 1
        
    return count + 1

def check_diagonal_right(last_point, game_field):
    '''проверка диагонали вверх направо'''
    
    count = 0
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row - 1 >= 0 and column + 1 <=9 and game_field[row-1][column+1] == char:
        count += 1
        row -= 1
        column += 1
        
    
    if count >= 5:
        return count
    '''проверка диагонали вниз налево'''
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row + 1 <= 9 and column - 1 >= 0 and  game_field[row+1][column-1] == char:
        count += 1
        row += 1
        column -= 1
        
        
    return count + 1

def check_diagonal_left(last_point, game_field):
    '''проверка диагонали вверх налево'''
    
    count = 0
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row - 1 >= 0 and column - 1 >=0 and game_field[row-1][column-1] == char:
        count += 1
        row -= 1
        column -= 1
    
    if count >= 5:
        return count
    '''проверка диагонали вниз направо'''
    row = last_point[0]
    column = last_point[1]
    char = game_field[row][column]
    while row + 1 <= 9 and column + 1 <= 9 and  game_field[row+1][column+1] == char:
        count += 1
        row += 1
        column += 1
        
        
    return count + 1

def winner(last_point, game_field):
    count_point = check_victory(last_point, game_field)
    if count_point >= 5:
        return True
    else:
        return False


def quede():
    '''очередность в зависимости от символа'''
    if player_char == 'x':
        first = player_move
        second = computer_move
    else:
        first = computer_move
        second = player_move
    return first, second

        
           
player_char, computer_char = choise_player_char(chars)






def main():

    first, second = quede()
    print_field()
    

    while True:
    

        last_point = first(game_field)

        print_field()

        if winner(last_point, game_field):
            if game_field[last_point[0]][last_point[1]] == player_char:
                text = 'Вы проиграли'
            else:
                text = 'Компьютер проиграл. Вы победили'
            print(text)
            break

        last_point = second(game_field)
        print_field()
        if winner(last_point, game_field):
            if game_field[last_point[0]][last_point[1]] == player_char:
                text = 'Вы проиграли'
            else:
                text = 'Компьютер проиграл. Вы победили'
            print(text)
            break
        
        
main()
