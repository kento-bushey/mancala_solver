import simpleguitk as simplegui

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
            #print(board)
        if (i==6):
            return [[board[0:6],board[7:],board[6]],"go_again"]
        if (board[i]>1 and i!=6):
            #print("we go again")
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

class board():
    left_side,right_side = [],[]
    def __init__(this,left_side,right_side):
        this.left_side = left_side
        this.right_side = right_side
    def getBest(this):
        return getMax(this.left_side,this.right_side)
            
    def __str__(this):
        return f"left_side:\n{this.left_side}\nright_side:\n{this.right_side}"

#CODECODE

l = [2,2,1,4,4,5]#bottom
r = [2,2,1,4,4,5]#top

b = board(l,r)
#CODECODE

def string_to_int_list(input_string):
    # Split the input string by commas and convert each part to an integer
    int_list = [int(x) for x in input_string.split(',')]
    return int_list

def Left_Side_handler(text_input):
    b.left_side = string_to_int_list(text_input)
def Right_Side_handler(text_input):
    b.right_side = string_to_int_list(text_input)

def button_handler():
    best = getMax(b.left_side,b.right_side)
    moves = best[0]
    for i in range(len(moves)):
        moves[i] +=1
    # for i in best[0]:
    #     i+=1
    return([moves,best[1]])

def draw_circles(canvas):
    x1 = 100
    x2 = 160
    y_offset = 80
    for i in range(6):
        canvas.draw_circle([x1,(i)*50+y_offset],20,1,"white","white")
        if (len(b.left_side)==6):
            canvas.draw_text(b.left_side[i],[x1-5,(i)*50+y_offset+10],12,"black")
    for i in range(6):
        canvas.draw_circle([x2,(i)*50+y_offset],20,1,"white","white")
        if (len(b.right_side)==6):
            canvas.draw_text(b.right_side[5-i],[x2-5,(i)*50+y_offset+10],12,"black")
    canvas.draw_text(f"Left Side: {b.left_side}",[200,100],12,"white")
    canvas.draw_text(f"Right Side: {b.right_side}",[194,120],12,"white")
    rect_hei_rad = 20
    rect_wid_rad = 40
    y_offset = 30
    canvas.draw_polygon([[(x1+x2)/2-rect_wid_rad,(y_offset-rect_hei_rad)],[(x1+x2)/2+rect_wid_rad,(y_offset-rect_hei_rad)],[(x1+x2)/2+rect_wid_rad,(y_offset+rect_hei_rad)],[(x1+x2)/2-rect_wid_rad,(y_offset+rect_hei_rad)]],1,"white","white")
    y_offset = 410-y_offset
    canvas.draw_polygon([[(x1+x2)/2-rect_wid_rad,(y_offset-rect_hei_rad)],[(x1+x2)/2+rect_wid_rad,(y_offset-rect_hei_rad)],[(x1+x2)/2+rect_wid_rad,(y_offset+rect_hei_rad)],[(x1+x2)/2-rect_wid_rad,(y_offset+rect_hei_rad)]],1,"white","white")
    canvas.draw_text("Enter the comma separated\n values into the text box,\nthen press enter in each box.",[200,200],12,"white")
    canvas.draw_text("Left side best move list \n(index is top down, 1-6)",[200,250],12,"white")
    best = button_handler()
    print(best[0])
    canvas.draw_text(best[0],[200,275],8,"white")
    canvas.draw_text(f"Points scored: {best[1]}",[200,305],12,"white")

def draw_handler(canvas):
    draw_circles(canvas)

frame = simplegui.create_frame('Testing', 400, 400)

left = frame.add_input('Left_Side', Left_Side_handler, 100)
right = frame.add_input('Right_Side', Right_Side_handler, 100)
frame.set_draw_handler(draw_handler)
frame.start()