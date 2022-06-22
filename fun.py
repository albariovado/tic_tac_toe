import turtle as tr
import var

turn = 0
game_mat = [['','',''],
            ['','',''],
            ['','','']]
win_conditions = [
    game_mat[0][0] == game_mat[0][1] == game_mat[0][2],
    game_mat[1][0] == game_mat[1][1] == game_mat[1][2],
    game_mat[2][0] == game_mat[2][1] == game_mat[2][2],
    game_mat[0][0] == game_mat[1][0] == game_mat[2][0],
    game_mat[0][1] == game_mat[1][1] == game_mat[2][1],
    game_mat[0][2] == game_mat[1][2] == game_mat[2][2],
    game_mat[0][0] == game_mat[1][1] == game_mat[2][2],
    game_mat[0][2] == game_mat[1][1] == game_mat[2][0]
]


def create_screen():
    '''Crea uno schermo a sfondo nero, 600x600 px con titolo: "SNAKE GAME!".'''
    screen = tr.Screen()
    screen.setup(width = var.SCREEN_WIDTH, height = var.SCREEN_HEIGHT)
    screen.colormode(255)
    screen.bgcolor(var.SCREEN_BGCOLOR)
    screen.title("TIC-TAC-TOE!")
    return screen

def create_board():
    tr.hideturtle()
    tr.pencolor(var.PEN_COLOR)
    tr.pensize(var.PEN_SIZE)
    tr.penup()
    tr.goto(-300,150)
    tr.pendown()
    tr.goto(300,150)
    tr.penup()
    tr.goto(-300,-50)
    tr.pendown()
    tr.goto(300,-50)
    tr.penup()
    tr.goto(-100,350)
    tr.pendown()
    tr.goto(-100,-250)
    tr.penup()
    tr.goto(100,350)
    tr.pendown()
    tr.goto(100,-250)
    return

def print_char(x, y):
    a = 0
    b = 0
    global turn
    global game_mat

    if (y>150) and (y<350):
        a = 0
    elif (y>-50) and (y<150):
        a = 1
    elif (y>-250) and (y<-50):
        a = 2
        
    
    if (x>-300) and (x<-100):
        b = 0
    elif (x>-100) and (x<100):
        b = 1
    elif (x>100) and (x<300):
        b = 2

    cell_center = var.GRID_CENTER[a][b]
    tr.hideturtle()
    tr.penup()
    tr.goto(cell_center[0],cell_center[1])

    if turn%2 == 0:
        draw_x()
        char = 'X'
    else:
        draw_o()
        char = 'O'
    
    game_mat[a][b] = char
    turn += 1
    for i in range(3):
        print(game_mat[i])
    print("----------")

    if turn>4:
        if True in win_conditions:
            print("{} WIN!".format(char))
        elif turn == 9:
            print("DRAW!")

    return

def draw_x():
    delta = 60
    center = tr.pos()
    tr.hideturtle()
    tr.pencolor(var.X_COLOR)
    tr.pensize(var.CHAR_SIZE)
    tr.penup()
    tr.goto(center[0]-delta,center[1]-delta)
    tr.pendown()
    tr.goto(center[0]+delta,center[1]+delta)
    tr.penup()
    tr.goto(center[0]-delta,center[1]+delta)
    tr.pendown()
    tr.goto(center[0]+delta,center[1]-delta)
    return

def draw_o():
    r = 60
    center = tr.pos()
    tr.hideturtle()
    tr.pencolor(var.O_COLOR)
    tr.pensize(var.CHAR_SIZE)
    tr.penup()
    tr.goto(center[0],center[1]-60)
    tr.pendown()
    tr.circle(r)
    return