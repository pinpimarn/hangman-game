import turtle
import time


class Play:
    def __init__(self, word, input):
        self.word = word
        self.input = input

    def update(self, status, word, char):
        w = " "
        if status:
            for i in word:
                if i == char:
                    w = w + i + " " + " "
                else:
                    w = w + " " + " " + " "
        else:
            pass
        pen2 = turtle.Turtle()
        pen2.hideturtle()
        pen2.penup()
        pen2.pensize(3)
        pen2.goto(5, 0)
        pen2.write(w, move=False, align='center', font=('Comic Sans MS', 50, 'normal'))
        pen2.pu()
        return w

    def show_update(self, clue):  # อันเก่า show_clue
        pen2 = turtle.Turtle()
        pen2.penup()
        pen2.hideturtle()
        pen2.pensize(3)
        pen2.goto(0, 0)
        pen2.write(clue, move=False, align='center', font=('Comic Sans MS', 50, 'normal'))
        pen2.pu()

    def stage(self):
        pen1 = turtle.Turtle()
        pen1.hideturtle()
        pen1.screen.screensize(1440, 900)
        pen1.screen.bgcolor("#fdf5e6")
        pen1.penup()

    def pop_up_screen(self, w, x):
        screen = turtle.Screen()
        screen.bgcolor("#fdf5e6")
        choose = screen.textinput("HANGMAN GAME", "Choose one alphabet")
        pen1 = turtle.Turtle()
        pen1.hideturtle()
        pen1.penup()
        if (('a' <= choose <= 'z') or ('A' <= choose <= 'Z')) and len(choose) == 1:
            choose = choose.lower()
            if (choose not in w) and (choose not in self.input):
                self.input.append(choose)
                pen1.hideturtle()
                pen1.penup()
                pen1.goto(0, -200)
                pen1.color("red")
                pen1.write("Try again!!!", move=False, align='center', font=('Comic Sans MS', 40, 'normal'))
                time.sleep(2)
                pen1.clear()
                pen1.goto(x, 150)
                pen1.pensize(3)
                pen1.write(choose, move=False, align='center', font=('Comic Sans MS', 30, 'normal'))
                return False, None
            elif choose in self.input:
                pen1.hideturtle()
                pen1.penup()
                pen1.goto(0, -200)
                pen1.color("red")
                pen1.write("Don't repeat yourself!", move=False, align='center', font=('Comic Sans MS', 40, 'normal'))
                time.sleep(2)
                pen1.clear()
                return "None", None
            else:
                self.input.append(choose)
                pen1.penup()
                pen1.hideturtle()
                pen1.goto(0, -200)
                pen1.color("green")
                pen1.write("Correct!!!", move=False, align='center', font=('Comic Sans MS', 40, 'normal'))
                time.sleep(2)
                pen1.clear()
                return True, choose
        else:
            pen1.penup()
            pen1.hideturtle()
            pen1.goto(0, -200)
            pen1.color("red")
            pen1.write("Please input an alphabet!!!", move=False, align='center', font=('Comic Sans MS', 40, 'normal'))
            time.sleep(2)
            pen1.clear()
            return "None", None

    def header(self):
        penmain = turtle.Turtle()
        penmain.hideturtle()
        penmain.color("brown")
        penmain.pensize(5)
        penmain.penup()
        penmain.goto(0, 250)
        penmain.write("HANGMAN GAME", move=False, align='center', font=('Comic Sans MS', 50, 'bold'))
        penmain.pu()

    def sub_header(self):
        penmain = turtle.Turtle()
        penmain.hideturtle()
        penmain.color("brown")
        penmain.pensize(5)
        penmain.penup()
        penmain.goto(0, 200)
        penmain.write("HANGMAN GAME", move=False, align='center', font=('Comic Sans MS', 50, 'bold'))
        penmain.pu()

    def draw_heart(self, c):
        win = turtle.Screen()
        win.register_shape("heart.gif")
        heart_list = []
        for i in range(9 - c):
            heart_list.append(turtle.Turtle())
        x = -680
        for h in heart_list:
            h.speed(0)
            h.hideturtle()
            h.penup()
            h.goto(x, 400)
            h.showturtle()
            h.shape("heart.gif")
            x += 50

    def hangman(self, ccount):
        pen2 = turtle.Turtle()
        pen2.hideturtle()
        pen2.color("#cd853f")
        pen2.pensize(8)
        if ccount == 1:
            pen2.pu()
            pen2.goto(-600, -400)
            pen2.pd()
            pen2.goto(-300, -400)
            pen2.pu()
        if ccount == 2:
            pen2.pu()
            pen2.goto(-450, -400)
            pen2.pd()
            pen2.goto(-450, -50)
            pen2.goto(-300, -50)
            pen2.goto(-300, -90)
            pen2.pu()
        if ccount == 3:
            pen2.pu()
            pen2.goto(-300, -150)
            pen2.pd()
            pen2.circle(30)
            pen2.pu()
        if ccount == 4:
            pen2.pu()
            pen2.goto(-300, -150)
            pen2.pd()
            pen2.goto(-300, -300)
            pen2.pu()
        if ccount == 5:
            pen2.pu()
            pen2.goto(-300, -165)
            pen2.pd()
            pen2.goto(-340, -230)
            pen2.pu()
        if ccount == 6:
            pen2.pu()
            pen2.goto(-300, -165)
            pen2.pd()
            pen2.goto(-260, -230)
            pen2.pu()
        if ccount == 7:
            pen2.pu()
            pen2.goto(-300, -300)
            pen2.pd()
            pen2.goto(-340, -330)
            pen2.pu()
        if ccount == 8:
            pen2.pu()
            pen2.goto(-300, -300)
            pen2.pd()
            pen2.goto(-260, -330)
            pen2.pu()
