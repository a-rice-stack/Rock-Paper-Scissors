from tkinter import *
from tkinter.font import *
import random

window = Tk()
window.title("가위바위보")
window.geometry("800x700+0+0")
window.resizable(True, True)


win = 0
draw = 0
lose = 0
p = 0



photo1 = PhotoImage(file = "")
photo2 = PhotoImage(file = "")
photo3 = PhotoImage(file = "")

font=Font(family="맑은 고딕", size=20, weight="bold")
font1=Font(family="맑은 고딕", size=30, weight="bold")

png1 = ""
png2 = ""

# 함수 설정
def game_start2():  # 바위

    y = random.randint(1, 4)
    global x, png, win, draw, lose, p

    if y == 2:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text = "Draw")

        x = 2

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 1:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Lose")

        x = 1

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 3:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Win")

        x = 3

        label_p.config(text=int(win) / int(win+draw+lose) + "%")


def game_start1():  # 가위

    y = random.randint(1, 4)
    global x, png, win, draw, lose, p

    if y == 2:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Draw")

        x = 2

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 1:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Lose")

        x = 1

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 3:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Win")

        x = 3

        label_p.config(text=int(win) / int(win+draw+lose) + "%")


def game_start3():  # 보

    y = random.randint(1, 4)
    global x, png, win, draw, lose, p

    if y == 2:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Draw")

        x = 2

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 1:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Lose")

        x = 1

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

    elif y == 3:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

        label_board.config(text="Win")

        x = 3

        label_p.config(text=int(win) / int(win+draw+lose) + "%")

def clear():
    global win, draw, lose, p
    if win > 0:
        win= 0
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

    if draw > 0:
        draw = 0
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))

    if lose > 0:
        lose = 0
        label_score.config(text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose))







#라벨 설정
label_score = Label(window, text = "Win : " + str(win) +" Draw : " + str(draw) +" Lose : " + str(lose), bd = 1, font=font)
label_score.pack()

label_photoA = Label(window, image = str(png1))
label_photoA.place(x=70, y=150)

label_photoB = Label(window, image = str(png2))
label_photoB.place(x=570, y=150)


label_player = Label(window, text = "USER", bd = 0, font=font)
label_player.place(x=100, y=50)

label_cpu = Label(window, text = "CPU", bd = 0, font=font)
label_cpu.place(x=600, y=50)

label_vs = Label(window, text = "VS", bd = 0, font=font)
label_vs.place(x=385, y=200)

label_board = Label(window, text = "", bd = 0, font=font1)
label_board.place(x=360, y=100)

label_p = Label(window, text = "0%", bd = 0, font=font)
label_p.pack()


#버튼 설정
b1 = Button(window, relief = "solid", image = photo1, command = game_start2, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b1.place(x=50, y=400)


b2 = Button(window, relief = "solid", image = photo2,command = game_start3, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b2.place(x=325, y=400)


b3 = Button(window, relief = "solid", image = photo3, command = game_start1, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b3.place(x=600, y=400)

b4 = Button(window, relief = "solid",text = "Clear", command = clear, width = 10, height = 2, repeatdelay=100, repeatinterval=100)
b4.place(x=365, y=600)






window.mainloop()