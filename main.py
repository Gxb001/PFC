from tkinter import *
from random import randint, choice
import string
import time

#créer la fenetre
window = Tk()
window.title("Pierre Feuille Ciseaux")
window.geometry("720x480")
window.maxsize(720, 480)
window.minsize(720, 480)
window.iconbitmap("ciseaux.ico")
window.config(background='#85E4E1')

#créer la frame
frame = Frame(window, bg='#80E5A0', bd=1, relief=SUNKEN)

#ajouter du texte
label_title = Label(frame, text="Bienvenue sur Pierre Feuille Ciseaux", font=("Helvetica", 25), bg='#80E5A0', fg='white')
label_title.pack()#side=LEFT cela décal le titre(bottom, etc

#ajouter un autre texte
label_subtitle = Label(frame, text="Bonne chance", font=("Helvetica", 15), bg='#80E5A0', fg='white')
label_subtitle.pack()

#fonctions
def create1():
    a = randint(1, 3) # a = 1 = pierre a = 2 = feuille a = 3 = ciseaux
    win = Toplevel(window)
    win.title("Resultat / PIERRE")
    win.maxsize(300, 300)
    win.minsize(300 ,300)
    win.config(background='#85E4E1')
    def destroy():
        win.destroy()
    win.after(1000, destroy)

    label_resultat = Label(win, text="Voici le resultat :", font=("Helvetica", 25), bg='#80E5A0', fg='white')
    label_resultat.pack(pady=25)
    if a == 1:
        label_reponse1 = Label(win, text="EGALITE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse1.pack(pady=25)
    elif a ==2:
        label_reponse2 = Label(win, text="PERDU", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse2.pack(pady=25)
    elif a == 3:
        label_reponse3 = Label(win, text="GAGNE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse3.pack(pady=25)






def create2():
    a = randint(1, 3)  # a = 1 = pierre a = 2 = feuille a = 3 = ciseaux
    win = Toplevel(window)
    win.title("Resultat / FEUILLE")
    win.maxsize(300, 300)
    win.minsize(300 ,300)
    win.config(background='#85E4E1')
    def destroy():
        win.destroy()
    win.after(1000, destroy)

    label_resultat = Label(win, text="Voici le resultat :", font=("Helvetica", 25), bg='#80E5A0', fg='white')
    label_resultat.pack(pady=25)
    if a == 1:
        label_reponse4 = Label(win, text="GAGNE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse4.pack(pady=25)
    elif a == 2:
        label_reponse5 = Label(win, text="EGALITE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse5.pack(pady=25)
    elif a == 3:
        label_reponse6 = Label(win, text="PERDU", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse6.pack(pady=25)

def create3():
    a = randint(1, 3)  # a = 1 = pierre a = 2 = feuille a = 3 = ciseaux
    win = Toplevel(window)
    win.title("Resultat / CISEAUX")
    win.maxsize(300, 300)
    win.minsize(300 ,300)
    win.config(background='#85E4E1')
    def destroy():
        win.destroy()
    win.after(1000, destroy)

    label_resultat = Label(win, text="Voici le resultat :", font=("Helvetica", 25), bg='#80E5A0', fg='white')
    label_resultat.pack(pady=25)
    if a == 1:
        label_reponse7 = Label(win, text="PERDU", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse7.pack(pady=25)
    elif a == 2:
        label_reponse8 = Label(win, text="GAGNE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse8.pack(pady=25)
    elif a == 3:
        label_reponse9 = Label(win, text="EGALITE", font=("Helvetica", 25), bg='#80E5A0', fg='white')
        label_reponse9.pack(pady=25)

#Bouton

pierre_button = Button(frame, text="Pierre", font=("Courrier", ), fg='#D04747', bg='white', command=create1)
pierre_button.pack(pady=25, fill=X)
feuille_button = Button(frame, text="Feuille", font=("Courrier", ), fg='#D04747', bg='white', command=create2)
feuille_button.pack(pady=25, fill=X)
ciseau_button = Button(frame, text="Ciseaux", font=("Courrier", ), fg='#D04747', bg='white', command=create3)
ciseau_button.pack(pady=25, fill=X)

#ajouter
frame.pack(expand=YES) # expand=YES pour le centrer

#afficher
window.mainloop()
