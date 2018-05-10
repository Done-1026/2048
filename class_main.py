import tkinter as tk
import tkinter.messagebox as tkm
import gamefield


class Root(tk.Tk):

    _color = ['#FFFFFF','#FFFFF0','#FFFFE0','#FFF8DC','#FFEBCD','#FFF68F','#FFEC8B','#FFFF00','#FFD700','FFC125','FFA500','FF7F24']
    _num_color = dict(zip([0]+[2**i for i in range(1,12)],_color))
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.game.make_number()
        self.title('2048')
        self.geometry('185x300')
        self.labels = [[] for i in range(4)]
        
        #记分区
        self.scoreboard = tk.Frame(self,bg='grey')
        self.scoreboard.grid()
        self.score = tk.Label(self.scoreboard,text='score: '+str(self.game.score))
        self.score.grid(row=0) 

        #数字显示区         
        self.chessboard = tk.Frame(self)
        self.chessboard.grid()
        self.init_board()
        self.refresh_board()

        #按键区        
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
        self.restart = tk.Button(self.hand_shank,text='restart',width=6,height=1,
                                 command=self.restart_button).grid(column=4,row=3)
        self.quit = tk.Button(self.hand_shank,text='exit',width=6,height=1,
                              command=self.quit_button).grid(column=4,row=4)
        #绑定键盘
        self.bind('<Key>',self.key_button)

    def init_board(self):
        for i in range(4):
            for j in range(4):
                num = tk.Label(self.chessboard,bg=self._num_color[self.game.field[i][j]],
                               font=5,height=2,width=5,text=str(self.game.field[i][j]))
                num.grid(row=i,column=j)
                self.labels[i].append(num)
                              
    def refresh_board(self):
        '''刷新棋盘'''
        for i in range(4):
            for j in range(4):
                if self.game.field[i][j] == 0:
                    font_color = '#FFFFFF'
                else:
                    font_color = '#000000'
                self.labels[i][j]['text'] = str(self.game.field[i][j])
                self.labels[i][j]['fg'] = font_color
                self.labels[i][j]['bg'] = self._num_color[self.game.field[i][j]]
        self.score['text'] = 'score: '+str(self.game.score)
               
    def move(move_to):
        '''装饰器:棋盘动作,判断胜负，增加数字，刷新棋盘'''
        def move1(self,*argv):
            status = self.game.check_status()
            print(status)
            if status == 'go':
                if len(argv)==0 or argv[0].char in self.game.actions:
                    move_to(self,*argv)
                    self.game.make_number()
                    self.refresh_board()
            elif status == 'win':
                tk.messagebox.askokcancel('info','you win!!',parent=self.chessboard)
            else:
                tk.messagebox.askokcancel('info','faild!!',parent=self.chessboard)               
        return move1
    
    def restart_button(self):
        '''重玩，有提示'''
        if tk.messagebox.askquestion('info','restart?')=='yes':
            self.game.action_move('r')         
            self.game.make_number()
            self.refresh_board()

    def quit_button(self):
        '''关闭窗口，有提示'''
        if tk.messagebox.askokcancel('info','quit?'):
            self.destroy()
    
    @move
    def key_button(self,event):
        '''绑定键盘,wsadr'''
        if event.char in self.game.actions.keys():
            self.game.action_move(event.char)
            
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
        
