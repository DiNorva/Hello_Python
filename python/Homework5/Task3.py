""" 3. Создайте программу для игры в 'Крестики-нолики'. """

board = list(range(1,10))

def draw_board(board):
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|",board[2+i*3], "|")

def put_move(step):
    valid = False
    while not valid:
        answer = input("Введите номер клетки куда поставить значение " + step+"? ")
        asw = int(answer)
        if asw >= 1 and asw <= 9:
            if (str(board[asw-1]) not in "XO"):
                board[asw-1] = step
                valid = True
        else:
            print ("Эта клетка занята")
def winner(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in victory:
        if board[x[0]] == board[x[1]] == board[x[2]]:
            return board[x[0]]
    return False

def game(board):
    count = 0
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
            put_move("X")
        else:
            put_move("O")
        count += 1
        if count > 4:
            m = winner(board)
            if m:
                print (m, "Победил!")
                win = True
                break
        if count == 9:
            print ("Победила дружба!")
            break
    draw_board(board)
game(board)