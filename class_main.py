import tkinter as tk
import gamefield


class Root(tk.Tk):

    _color = ['#FFFFFF','#FFFFE0','#FFFACD','#EEE8AA','#F0E68C','#FFFF00','#FFD700']
    _num_color = dict(zip([0]+[2**i for i in range(1,7)],_color))
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.game.make_number()
        self.title('2048')
        self.geometry('200x300')

        self.chessboard = tk.Frame(self,bg='grey')
        self.chessboard.grid()
        self.refresh_board()
        
        self.hand_shank = tk.Frame(self)
        self.hand_shank.grid()
        self.up = tk.Button(self.hand_shank,text='↑',width=4,height=1,
                            command=self.move_up).grid(column=1,row=0)
        self.down = tk.Button(self.hand_shank,text='↓',width=4,height=1,
                              command=self.move_down).grid(column=1,row=1)
        self.left = tk.Button(self.hand_shank,text='←',width=4,height=1,
                              command=self.move_left).grid(column=0,row=1)
        self.right = tk.Button(self.hand_shank,text='→',width=4,height=1,
                               command=self.move_right).grid(column=2,row=1)
        

    def refresh_board(self):
        '''刷新棋盘'''
        for i in range(4):
            for j in range(4):
                if self.game.field[i][j] == 0:
                    font_color = '#FFFFFF'
                else:
                    font_color = '#000000'
                num = tk.Label(self.chessboard,bg=self._num_color[self.game.field[i][j]],
                               fg=font_color,font=5,height=2,width=5,text=str(self.game.field[i][j]))
                num.grid(row=i,column=j)

    def move(move_to):
        '''棋盘动作'''
        def move1(self):
            status = self.game.check_status()
            print(status)
            if status == 'go':
                move_to(self)
                self.game.make_number()
                self.refresh_board()
        return move1

    @move
    def move_up(self):
        self.game.up_ac(self.game.field)
    @move
    def move_down(self):
        self.game.down_ac(self.game.field)
    @move
    def move_left(self):
        self.game.left_ac(self.game.field)
    @move
    def move_right(self):
        self.game.right_ac(self.game.field)

if __name__ == '__main__':
    game = gamefield.GameField()
    root = Root(game)
    root.mainloop()
        
