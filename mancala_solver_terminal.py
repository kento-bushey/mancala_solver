import simpleguitk as simplegui

class board():
    left_side,right_side = [],[]
    def __init__(this,left_side,right_side):
        this.left_side = left_side
        this.right_side = right_side
    def getBest(this):
        return getMax(this.left_side,this.right_side)
            
    def __str__(this):
        return f"left_side:\n{this.left_side}\nright_side:\n{this.right_side}"

"""
Here you will input your board values
Left side is top down, right side is bottom up

Example board
[    ]
[2][5]
[2][4]
[1][4]
[4][1]
[4][2]
[5][2]
[    ]

left_side_board = [2,2,1,4,4,5]
right_side_board = [2,2,1,4,4,5]

"""

left_side_board = [2,2,1,4,4,5]
right_side_board = [2,2,1,4,4,5]

game_board = board(left_side_board,right_side_board)

def turn(index,board):
        i = index
        steps_left = board[i]
        board[i]=0
        while (steps_left > 0):
            if (i == 12):
                i = -1
            i+=1
            board[i]+=1
            steps_left-=1
        if (i==6):
            return [[board[0:6],board[7:],board[6]],"go_again"]
        if (board[i]>1 and i!=6):
            return turn(i,board)
        return [[board[0:6],board[7:],board[6]],"end"]
def getMax(left_side,right_side):
        movelist = []
        turn_max = 0
        score = 0
        for i in range(6):
            go = turn(i,left_side+[0]+right_side)
            score = go[0][2]
            mlist = [i]
            if go[1] == "go_again":
                re = getMax(go[0][0],go[0][1])
                mlist+=re[0]
                score += re[1]
            if score>turn_max:
                movelist = mlist
                turn_max = score
        return [movelist,turn_max]

def calculate_board():
    best = game_board.getBest()
    moves = best[0]
    score = best[1]
    for i in range(len(moves)):
        moves[i] +=1
    print(f"List of moves: {moves}\nPoints Scored: {score}")

"""
How to read the output:

List of moves is the list of moves to perform on the left side of the board(1-6), 1 being top, and 6 being bottom

"""

calculate_board()
