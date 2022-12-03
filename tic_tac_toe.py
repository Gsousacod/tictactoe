import random
import os

class ticTicToe:
    def __init__(self):
        self.reset()

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + "  |  " + self.board[0][1] + "  |  " + self.board[0][2])
        print("---------------")
        print(" " + self.board[1][0] + "  |  " + self.board[1][1] + "  |  " + self.board[1][2])
        print("---------------") 
        print(" " + self.board[2][0] + "  |  " + self.board[2][1] + "  |  " + self.board[2][2])
       

    def reset(self):
        self.board=[[" "," "," "], [" "," "," "], [" "," "," "]]
        self.done = ""
        

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X","O"]:
            #horizontais
            dict_win[i] = (self.board[0][0]==self.board[0][1]==self.board[0][2]==i)
            dict_win[i] = (self.board[1][0]==self.board[1][1]==self.board[1][2]==i) or dict_win[i]
            dict_win[i] = (self.board[2][0]==self.board[2][1]==self.board[2][2]==i) or dict_win[i]
            #verticais
            dict_win[i] = (self.board[0][0]==self.board[1][0]==self.board[2][0]==i) or dict_win[i]
            dict_win[i] = (self.board[0][1]==self.board[1][1]==self.board[2][1]==i) or dict_win[i]
            dict_win[i] = (self.board[0][2]==self.board[1][2]==self.board[2][2]==i) or dict_win[i]

            #diagonais
            dict_win[i] = (self.board[0][0]==self.board[1][1]==self.board[2][2]==i) or dict_win[i]
            dict_win[i] = (self.board[2][0]==self.board[1][1]==self.board[0][2]==i) or dict_win[i]

        if dict_win["X"]:
            #self.done = "x"
            print("x venceu")
            return 

        elif dict_win["O"]:
            #self.done = "o"
            print("o perdeu!")
            return 
        
        c = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != "":
                    c+=1
                    break
        if c == 0:
            self.done = "d"
            print('Empate!')
            return

    def get_player_move(self):
        invalide_movie = True

        while invalide_movie:
            try:
                print("Digite a linha do seu próximo lance: ")
                x=int(input())

                print("Digite a coluna do seu próximo lance: ")
                y=int(input())

                if x>2 or x<0 or y>2 or y<0:
                    print("coordenadas inválidas")

                if self.board[x][y] != " ":
                    print("Posição já preenchida.")
                    continue

            except Exception as e:
                print(e)
                continue

            invalide_movie = False

        self.board[x][y] = "x"

    def make_move(self):
        list_move = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_move.append((i,j))
        if len(list_move)>0:
            x,y = random.choice(list_move)
            self.board[x][y] = "o"





tictictoe = ticTicToe()
tictictoe.print_board()

next = 0
while next == 0:
    os.system("cls")
    tictictoe.print_board()
    while tictictoe.done == "":
        tictictoe.get_player_move()
        tictictoe.make_move()
        os.system("cls")
        tictictoe.print_board()
        tictictoe.check_win_or_draw()


    print("Digite 1 para sair ou qualquer tecla parajogar novamente!")
    next = int(input())
    if next == 1:
        break
    else:
        tictictoe.reset()
        next = 0


