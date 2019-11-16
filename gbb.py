from tkinter import *
from tkinter.font import *
import random

window = Tk()
window.title("가위바위보")
window.geometry("800x700+0+0")
window.resizable(False, False)


win = 0
draw = 0
lose = 0


photo1 = PhotoImage(file =r"C:\Users\User\PycharmProjects\oh\rock.png")
photo2 = PhotoImage(file =r"C:\Users\User\PycharmProjects\oh\paper.png")
photo3 = PhotoImage(file =r"C:\Users\User\PycharmProjects\oh\scissors.png")

font=Font(family="맑은 고딕", size=20, weight="bold")

png1 = ""
png2 = ""

# 함수 설정
def game_start2():  # 바위

    y = random.randint(1, 4)
    global x, png, win, draw, lose

    if y == 2:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 2

    elif y == 1:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text="승 : " + str(win) + " 무 : " + str(draw) + " 패 : " + str(lose))

        x = 1

    elif y == 3:

        png = photo1
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text="승 : " + str(win) + " 무 : " + str(draw) + " 패 : " + str(lose))

        x = 3


def game_start1():  # 가위

    y = random.randint(1, 4)
    global x, png, win, draw, lose

    if y == 2:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 2

    elif y == 1:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 1

    elif y == 3:

        png = photo3
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 3


def game_start3():  # 보

    y = random.randint(1, 4)
    global x, png, win, draw, lose

    if y == 2:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo2
        label_photoB.config(image=str(png))

        draw += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 2

    elif y == 1:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo3
        label_photoB.config(image=str(png))

        lose += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 1

    elif y == 3:

        png = photo2
        label_photoA.config(image=str(png))

        png = photo1
        label_photoB.config(image=str(png))

        win += 1
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

        x = 3

def clear():
    global win, draw, lose
    if win > 0:
        win= 0
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

    if draw > 0:
        draw = 0
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))

    if lose > 0:
        lose = 0
        label_score.config(text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose))


#라벨 설정
label_score = Label(window, text = "승 : " + str(win) +" 무 : " + str(draw) +" 패 : " + str(lose), bd = 1, font=font)
label_score.pack()

label_photoA = Label(window, image = str(png1))
label_photoA.place(x=70, y=150)

label_photoB = Label(window, image = str(png2))
label_photoB.place(x=570, y=150)


label_player = Label(window, text = "사용자", bd = 0, font=font)
label_player.place(x=100, y=50)

label_cpu = Label(window, text = "컴퓨터", bd = 0, font=font)
label_cpu.place(x=600, y=50)

label_vs = Label(window, text = "VS", bd = 0, font=font)
label_vs.place(x=385, y=200)


#버튼 설정
b1 = Button(window, relief = "solid", image = photo1, command = game_start2, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b1.place(x=50, y=400)


b2 = Button(window, relief = "solid", image = photo2,command = game_start3, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b2.place(x=325, y=400)


b3 = Button(window, relief = "solid", image = photo3, command = game_start1, width = 150, height = 160, repeatdelay=100, repeatinterval=100)
b3.place(x=600, y=400)

b4 = Button(window, relief = "solid",text = "초기화", command = clear, width = 10, height = 2, repeatdelay=100, repeatinterval=100)
b4.place(x=365, y=600)






window.mainloop()