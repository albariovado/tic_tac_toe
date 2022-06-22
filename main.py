import fun
import turtle

screen = fun.create_screen()
fun.create_board()

screen.listen()

screen.onscreenclick(fun.print_char)

turtle.getscreen()._root.mainloop()