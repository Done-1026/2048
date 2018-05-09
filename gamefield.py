import random
import curses

#field = [[0 for i in range(4)] for j in range(4)]

class GameField():
    def __init__(self,win=2048):
        self.field = [[0 for i in range(4)] for j in range(4)]
        #self.make_number()
        self.actions = dict(zip('WSADERwsader',['up','down','left','right','exit','restart']*2))
        self.score = 0
        self.win = win
        self.max = 0
             
    def make_number(self):
        '''在为0处生成2个随机数字'''
        _zero = []
        for i in range(4):
            for j in range(4):
                if self.field[i][j] == 0:
                    _zero.append((i,j))
        try:
            index = random.choice(_zero)
            self.field[index[0]][index[1]] = random.choices([2,4],weights=[9,1],k=1)[0]
        except:
            pass
        
        '''            
        _count = 0
        while True:
            if _count < count:
                i = random.randint(0,3)
                j = random.randint(0,3)
                if self.field[i][j] == 0:
                    _count += 1
                    self.field[i][j] = random.choices([2,4],weights=[9,1],k=1)[0]  #在随机空白处生成2，4数字
            else:
                break
        '''
    def align(self,row):
        '''左对齐每一行'''
        for i in range(3):
            for j in range(3):
                if row[j]==0:
                    row[j],row[j+1]=row[j+1],row[j]

    def plus_num(self,row):
        '''从左开始，相加相同数字'''
        for i in range(3):
            if row[i] == row[i+1] != 0:
                row[i] *= 2
                row[i+1]=0
                self.score += row[i]
                if self.max < row[i]:
                    self.max = row[i]
    
    def rotate_matrix(self,field):
        '''转置二维数组'''
        for i in range(4):
            for j in range(i+1,4):
                field[i][j],field[j][i] = field[j][i],field[i][j]

    def dec_rotate(up_down):
        def rotate(self,field):
            self.rotate_matrix(field)
            up_down(self,field)
            self.rotate_matrix(field)
        return rotate
                 
    def left_ac(self,field):
        '''向左'''
        for row in field:
            self.align(row)
            self.plus_num(row)
            self.align(row)
                
    def right_ac(self,field):
        '''向右'''
        for row in field:
            row.reverse()
            self.align(row)
            self.plus_num(row)
            self.align(row)
            row.reverse()
            
    @dec_rotate        
    def up_ac(self,field):
        '''向上'''
        self.left_ac(field)
        
    @dec_rotate            
    def down_ac(self,field):
        '''向下'''
        self.right_ac(field)

    def action_move(self,action):                    
        if self.actions[action] == 'left':
            self.left_ac(self.field)
        elif self.actions[action] == 'right':
            self.right_ac(self.field)
        elif self.actions[action] == 'up':
            self.up_ac(self.field)
        elif self.actions[action] == 'down':
            self.down_ac(self.field)
        elif self.actions[action] == 'restart':
            self.score = 0
            self.field = [[0 for i in range(4)] for j in range(4)]
        else:
            print('enter error!please try again.')

    def check_over(self,field):
        game_status = 'over'
        for i in range(4):
            if 0 in field[i]:
                game_status = 'go'
                break
            else:
                for j in range(3):
                #第i行的第j个==第i行的第j+1个    第i列的第j个=第i列的第j+1个
                    if field[i][j]==field[i][j+1] or field[j][i]==field[j+1][i]:
                        game_status = 'go'
                        break
        return game_status
    
    def check_status(self):
        if self.max == self.win:
            return 'win'
        else:
            return self.check_over(self.field)
                
    def field_display(self):
        for i in self.field:
            for j in i:
                print(str(j).ljust(4),end=' ')
            print('\n')
        print('score',self.score)

     
            
def main():
    while True:    
        try:
            win_score = int(input("Enter you target number(default 2048)!\nYour target:"))
            game = GameField(win_score)
            break
        except:
            print('input again')
            continue
        
    while True:
        game.make_number()
        game.field_display()
        status = game.check_status()
        if status == 'win':
            print('you win!!!')
            break
        elif status == 'over':
            print('game over!!!')
            break
        else:
            print(status)
            get_action = input()
            while get_action not in game.actions.keys():
                get_action = input('Enter error!Enter again.\n')
            if game.actions[get_action]=='exit':
                print('YOU QUIT!!!')
                break
            else:
                game.action_move(get_action)

if __name__ == '__main__':
    game = GameField()
    main()

        
    

            
    
    
