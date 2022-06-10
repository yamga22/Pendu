from tkinter import *
from random import randrange


def maj_mot_en_progres(mot_en_progres, lettre, secret):
    n = len(secret)
    for i in range(n):
        if secret[i] == lettre:
            mot_en_progres[2 * i] = lettre


def score(lettre):
    global nro, end, img
    if lettre not in secret:
        cnv.delete(images[nro])
        nro -= 1
        cnv.create_image((width_img / 2, height_img / 2),
                         image=images[nro])
        if nro == 0:
            cnv.create_image((width_img / 2, height_img / 2),
                             image=fail)
            lbl["text"] = " ".join(secret)
            
            end = True
    elif mot_en_progres == list(" ".join(secret)):
        cnv.create_image((width_img / 2, height_img / 2), image=win)
        end = True


def choisir_lettre(event):
    if end:
        return
    mon_btn = event.widget
    lettre = mon_btn["text"]
    mon_btn["state"] = DISABLED
    maj_mot_en_progres(mot_en_progres, lettre, secret)
    lbl["text"] = "".join(mot_en_progres)
    score(lettre)


def init():
    global end, mot_en_progres, secret, nro, img
    secret = arbres[randrange(len(arbres))]
    mot_en_progres = list(' '.join("●" * len(secret)))
    lbl["text"] = ''.join(mot_en_progres)
    cnv.delete(ALL)
    cnv.create_image((width_img / 2, height_img / 2), image=images[-1])

    for btn in btns:
        btn["state"] = NORMAL

    nro = limite
    end = False


root = Tk()

limite = 7

# Les images 
images = [PhotoImage(file="%s.png" % j) for j in range(limite + 1)]

fail = PhotoImage(file="fail.png")
win = PhotoImage(file="win.png")

width_img = win.width()
height_img = win.height()

cnv = Canvas(
    root, width=width_img, height=height_img, highlightthickness=0)
cnv.grid(row=0, column=0, padx=20, pady=20)

# La zone de texte

lbl = Label(
    root, font=('Deja Vu Sans Mono', 45, 'bold'), width=23, fg="blue")
lbl.grid(row=0, column=1)

# Rejouer

reset = Button(root, text="Nouveau", font="Times 15 bold", command=init)
reset.grid(row=1, column=0)

# Les boutons pour les lettres

lettres = Frame(root)
lettres.grid(row=1, column=1)

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
btns = []

for i in range(2):
    for j in range(10):
        btn = Button(
            lettres,
            text=ALPHA[10 * i + j],
            relief=FLAT,
            font='times 30')
        btn.grid(row=i, column=j)
        btn.bind("<Button-1>", choisir_lettre)
        btns.append(btn)

for j in range(6):
    btn = Button(
        lettres, text=ALPHA[20 + j], relief=FLAT, font='times 30')
    btn.grid(row=2, column=j + 2)
    btn.bind("<Button-1>", choisir_lettre)
    btns.append(btn)

with open("arbres.txt") as f:
    arbres=f.read().split("\n")

init()

root.mainloop()
