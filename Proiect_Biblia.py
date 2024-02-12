
import random
import customtkinter
from tkinter import *
from tkinter import Text
from PIL import ImageTk, Image
from customtkinter import CTk
from datetime import datetime
import requests
from io import BytesIO

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# creearea ferestei grafice pentru pagina principala
root: CTk = customtkinter.CTk()
root.title("Bible App")
root.geometry("1200x650")
root.resizable(0, 0)

# conficurarea coloanelor si randurilor
root.columnconfigure(0, weight=1)
root.columnconfigure((1, 2, 3), weight=0)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=1)
root.rowconfigure((0, 1, 2, 3), weight=0)


# put the image for main page
url = "https://images.pexels.com/photos/1421903/pexels-photo-1421903.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
response = requests.get(url)
image_data = response.content
img = (Image.open(BytesIO(image_data)))
resized_image = img.resize((1500, 850))
bgimagine = ImageTk.PhotoImage(resized_image)
label1 = Label(root, image=bgimagine)
label1.place(x=-2, y=-2)

#get the image for the books background
url_book= "https://images.pexels.com/photos/1428277/pexels-photo-1428277.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
response_book = requests.get(url_book)
image_data_book = response_book.content
img_book = (Image.open(BytesIO(image_data_book)))
resized_image_book = img_book.resize((1000, 720))
bgimagine_book = ImageTk.PhotoImage(resized_image_book)

# creearea unei liste cu toate versetele din Bilie
ListaVerseteCarti = []
CuvantCautat = StringVar()

with open('Galateni.txt', 'r') as f:
    for line in f:
        ListaVerseteCarti.append(line)
with open('Efeseni.txt', 'r') as f:
    for line in f:
        ListaVerseteCarti.append(line)
with open('Filipeni.txt', 'r') as f:
    for line in f:
        ListaVerseteCarti.append(line)
with open('Coloseni.txt', 'r') as f:
    for line in f:
        ListaVerseteCarti.append(line)


def VersZilei():
    # adaugarea zilei
    ZiuaDinAn = datetime.now().timetuple().tm_yday
    AnulCurent = datetime.now().timetuple().tm_year
    NrVerset = int((AnulCurent + ZiuaDinAn) % (len(ListaVerseteCarti) - 1))
    random.seed(NrVerset)
    Alegerea_Vzilei = random.choice(ListaVerseteCarti)
    index_Vzilei = ListaVerseteCarti.index(Alegerea_Vzilei)

    if 0 <= index_Vzilei <= 148:
        return "Galateni " + Alegerea_Vzilei
    if 149 <= index_Vzilei <= 303:
        return "Efeseni " + Alegerea_Vzilei
    if 304 <= index_Vzilei <= 407:
        return "Filipeni " + Alegerea_Vzilei
    if 408 <= index_Vzilei <= (len(ListaVerseteCarti) - 1):
        return "Coloseni " + Alegerea_Vzilei


import tkinter
from tkinter import END

def CautareAvansata():
    index_lista = 0
    flag = 0
    VerseteCauate_Text.delete(0.0, END)
    cuvant = CuvantCautat.get()

    for linie in ListaVerseteCarti:
        if cuvant.lower() in linie.lower():
            flag = 1

            # Afisează linia originală
            if 0 <= index_lista <= 148:
                VerseteCauate_Text.insert(tkinter.INSERT, chars="Gal. " + linie + "\n")
            if 149 <= index_lista <= 303:
                VerseteCauate_Text.insert(tkinter.INSERT, chars="Efes. " + linie + "\n")
            if 304 <= index_lista <= 407:
                VerseteCauate_Text.insert(tkinter.INSERT, chars="Fil. " + linie + "\n")
            if 408 <= index_lista <= (len(ListaVerseteCarti) - 1):
                VerseteCauate_Text.insert(tkinter.INSERT, chars="Col. " + linie + "\n")

            # Evidențiază cuvântul căutat în linia originală
            start_index = "1.0"
            while True:
                start_index = VerseteCauate_Text.search(cuvant.lower(), start_index, stopindex="end", nocase=True)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(cuvant)}c"
                VerseteCauate_Text.tag_add("highlight", start_index, end_index)
                VerseteCauate_Text.tag_config("highlight", background="lightblue", foreground="black")
                start_index = end_index

        index_lista += 1

    if flag == 0:
        VerseteCauate_Text.insert(tkinter.INSERT, chars="Nu s-a găsit niciun verset care să corespundă criteriului de căutare")


def OpenGalateni():
    def Cap1_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "1":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap2_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "2":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap3_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "3":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap4_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "4":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap5_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "5":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap6_Galateni():
        Versete_Galateni_Text.delete(0.0, END)
        with open('Galateni.txt', 'r') as f:
            for line in f:
                if line[0] == "6":
                    Versete_Galateni_Text.insert(tkinter.INSERT, chars=line[2:])

    # crearea ferestrei pentru cartea Galateni
    Galateni_Window = customtkinter.CTkToplevel()
    Galateni_Window.title("Galateni")
    Galateni_Window.geometry("800x570")
    Galateni_Window.resizable(0, 0)
    Galateni_Window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    Galateni_Window.rowconfigure((0, 1, 2, 3), weight=0)

    # setarea imaginii pentru fereastra Galateni
    Label_Galateni = Label(Galateni_Window, image=bgimagine_book)
    Label_Galateni.place(x=-2, y=-2)

    # crearea titlului pentru cartea Galateni
    titlu_Galateni = customtkinter.CTkLabel(Galateni_Window, font=("Times New Roman", 34), text="Galateni")
    titlu_Galateni.grid(column=2, row=0, columnspan=4)

    # crearea unui subtitlu cu numele Capitole
    subtitlu_Galateni = customtkinter.CTkLabel(Galateni_Window, font=("Times New Roman", 18), text="Capitole")
    subtitlu_Galateni.grid(column=2, row=1, columnspan=4)

    # crearea unui frame pentru capitolele din Galateni
    Capitole_Frame_Galateni = customtkinter.CTkFrame(Galateni_Window, corner_radius=10)
    Capitole_Frame_Galateni.grid(column=1, row=2, columnspan=6)

    # crearea butoanelor
    ButtonCap1_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="1",
                                                  command=Cap1_Galateni)
    ButtonCap1_Galateni.grid(column=1, row=2, padx=10, pady=10)

    ButtonCap2_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="2",
                                                  command=Cap2_Galateni)
    ButtonCap2_Galateni.grid(column=2, row=2, padx=10, pady=10)

    ButtonCap3_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="3",
                                                  command=Cap3_Galateni)
    ButtonCap3_Galateni.grid(column=3, row=2, padx=10, pady=10)

    ButtonCap4_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="4",
                                                  command=Cap4_Galateni)
    ButtonCap4_Galateni.grid(column=4, row=2, padx=10, pady=10)

    ButtonCap5_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="5",
                                                  command=Cap5_Galateni)
    ButtonCap5_Galateni.grid(column=5, row=2, padx=10, pady=10)

    ButtonCap6_Galateni = customtkinter.CTkButton(Capitole_Frame_Galateni, width=30, height=20, text="6",
                                                  command=Cap6_Galateni)
    ButtonCap6_Galateni.grid(column=6, row=2, padx=10, pady=10)

    # crearea unui frame pentru afișarea versetelor din fiecare capitol
    Versete_Frame_Galateni = customtkinter.CTkFrame(Galateni_Window, corner_radius=10)
    Versete_Frame_Galateni.grid(column=1, row=3, columnspan=6)

    # textbox-ul pentru versetele Bibliei
    Versete_Galateni_Text = Text(Versete_Frame_Galateni, height=20, width=80, wrap=WORD, bd=0, bg="#292929",
                                 fg="silver", font=("Calibri", 15))
    Versete_Galateni_Text.grid(column=1, row=3, columnspan=6, pady=5, padx=5)

    # punerea unui scroll down pentru versetele Bibliei
    Versete_Galateni_Scrollbar = customtkinter.CTkScrollbar(Versete_Frame_Galateni, command=Versete_Galateni_Text.yview)
    Versete_Galateni_Scrollbar.grid(column=7, row=3, sticky="ns")

    # conectarea scroll down-ului la textbox
    Versete_Galateni_Text.configure(yscrollcommand=Versete_Galateni_Scrollbar.set)

    # crearea unui buton de ieșire
    Button_Iesire_Galateni = customtkinter.CTkButton(Galateni_Window, width=100, height=40, text="Close page",
                                                     command=Galateni_Window.destroy)
    Button_Iesire_Galateni.grid(column=2, row=4, columnspan=4, padx=10, pady=10)


def OpenEfeseni():
    def Cap1_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "1":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap2_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "2":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap3_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "3":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap4_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "4":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap5_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "5":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap6_Efeseni():
        Versete_Efeseni_Text.delete(0.0, END)
        with open('Efeseni.txt', 'r') as f:
            for line in f:
                if line[0] == "6":
                    Versete_Efeseni_Text.insert(tkinter.INSERT, chars=line[2:])

    # crearea ferestrei pentru cartea Efeseni
    Efeseni_Window = customtkinter.CTkToplevel()
    Efeseni_Window.title("Galateni")
    Efeseni_Window.geometry("800x570")
    Efeseni_Window.resizable(0, 0)
    Efeseni_Window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    Efeseni_Window.rowconfigure((0, 1, 2, 3), weight=0)

    # setarea imaginii pentru fereastra Efeseni
    Label_Efeseni = Label(Efeseni_Window, image=bgimagine_book)
    Label_Efeseni.place(x=-2, y=-2)

    # crearea titlului pentru cartea Galateni
    titlu_Efeseni = customtkinter.CTkLabel(Efeseni_Window, font=("Times New Roman", 34), text="Efeseni")
    titlu_Efeseni.grid(column=2, row=0, columnspan=4)

    # crearea unui subtitlu cu numele Capitole

    subtitlu_Efeseni = customtkinter.CTkLabel(Efeseni_Window, font=("Times New Roman", 18), text="Capitole")
    subtitlu_Efeseni.grid(column=2, row=1, columnspan=4)

    # crearea unui frame pentru capitolele din Galateni
    Capitole_Frame_Efeseni = customtkinter.CTkFrame(Efeseni_Window, corner_radius=10)
    Capitole_Frame_Efeseni.grid(column=1, row=2, columnspan=6)

    # crearea butoanelor
    ButtonCap1_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="1",
                                                 command=Cap1_Efeseni)
    ButtonCap1_Efeseni.grid(column=1, row=2, padx=10, pady=10)

    ButtonCap2_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="2",
                                                 command=Cap2_Efeseni)
    ButtonCap2_Efeseni.grid(column=2, row=2, padx=10, pady=10)

    ButtonCap3_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="3",
                                                 command=Cap3_Efeseni)
    ButtonCap3_Efeseni.grid(column=3, row=2, padx=10, pady=10)

    ButtonCap4_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="4",
                                                 command=Cap4_Efeseni)
    ButtonCap4_Efeseni.grid(column=4, row=2, padx=10, pady=10)

    ButtonCap5_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="5",
                                                 command=Cap5_Efeseni)
    ButtonCap5_Efeseni.grid(column=5, row=2, padx=10, pady=10)

    ButtonCap6_Efeseni = customtkinter.CTkButton(Capitole_Frame_Efeseni, width=30, height=20, text="6",
                                                 command=Cap6_Efeseni)
    ButtonCap6_Efeseni.grid(column=6, row=2, padx=10, pady=10)

    # crearea unui frame pentru afisarea versetelor din fiecare capitol
    Versete_Frame_Efeseni = customtkinter.CTkFrame(Efeseni_Window, corner_radius=10)
    Versete_Frame_Efeseni.grid(column=1, row=3, columnspan=6)

    # textbox-ul pentru versetele Bibliei
    Versete_Efeseni_Text = Text(Versete_Frame_Efeseni, height=20, width=80, wrap=WORD, bd=0, bg="#292929", fg="silver",
                                font=("Calibri", 15))
    Versete_Efeseni_Text.grid(column=1, row=3, columnspan=6, pady=5, padx=5)

    # punerea unui scroll down pentru versetele Bibliei
    Versete_Efeseni_Scrollbar = customtkinter.CTkScrollbar(Versete_Frame_Efeseni, command=Versete_Efeseni_Text.yview)
    Versete_Efeseni_Scrollbar.grid(column=7, row=3, sticky="ns")

    # conectarea scroll down-ului la textbox
    Versete_Efeseni_Text.configure(yscrollcommand=Versete_Efeseni_Scrollbar.set)

    # crearea unui buton de iesire
    Button_Iesire_Efeseni = customtkinter.CTkButton(Efeseni_Window, width=100, height=40, text="Close page",
                                                    command=Efeseni_Window.destroy)
    Button_Iesire_Efeseni.grid(column=2, row=4, columnspan=4, padx=10, pady=10)


def OpenFilipeni():
    def Cap1_Filipeni():
        Versete_Filipeni_Text.delete(0.0, END)
        with open('Filipeni.txt', 'r') as f:
            for line in f:
                if line[0] == "1":
                    Versete_Filipeni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap2_Filipeni():
        Versete_Filipeni_Text.delete(0.0, END)
        with open('Filipeni.txt', 'r') as f:
            for line in f:
                if line[0] == "2":
                    Versete_Filipeni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap3_Filipeni():
        Versete_Filipeni_Text.delete(0.0, END)
        with open('Filipeni.txt', 'r') as f:
            for line in f:
                if line[0] == "3":
                    Versete_Filipeni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap4_Filipeni():
        Versete_Filipeni_Text.delete(0.0, END)
        with open('Filipeni.txt', 'r') as f:
            for line in f:
                if line[0] == "4":
                    Versete_Filipeni_Text.insert(tkinter.INSERT, chars=line[2:])

    # crearea ferestrei pentru cartea Filipeni
    Filipeni_Window = customtkinter.CTkToplevel()
    Filipeni_Window.title("Filipeni")
    Filipeni_Window.geometry("800x570")
    Filipeni_Window.resizable(0, 0)
    Filipeni_Window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    Filipeni_Window.rowconfigure((0, 1, 2, 3), weight=0)

    # setarea imaginii pentru fereastra Filipeni
    Label_Filipeni = Label(Filipeni_Window, image=bgimagine_book)
    Label_Filipeni.place(x=-2, y=-2)

    # crearea titlului pentru cartea Filipeni
    titlu_Filipeni = customtkinter.CTkLabel(Filipeni_Window, font=("Times New Roman", 34), text="Filipeni")
    titlu_Filipeni.grid(column=2, row=0, columnspan=4)

    # crearea unui subtitlu cu numele Capitole
    subtitlu_Filipeni = customtkinter.CTkLabel(Filipeni_Window, font=("Times New Roman", 18), text="Capitole")
    subtitlu_Filipeni.grid(column=2, row=1, columnspan=4)

    # crearea unui frame pentru capitolele din Filipeni
    Capitole_Frame_Filipeni = customtkinter.CTkFrame(Filipeni_Window, corner_radius=10)
    Capitole_Frame_Filipeni.grid(column=1, row=2, columnspan=6)

    # crearea butoanelor
    ButtonCap1_Filipeni = customtkinter.CTkButton(Capitole_Frame_Filipeni, width=30, height=20, text="1",
                                                  command=Cap1_Filipeni)
    ButtonCap1_Filipeni.grid(column=1, row=2, padx=10, pady=10)

    ButtonCap2_Filipeni = customtkinter.CTkButton(Capitole_Frame_Filipeni, width=30, height=20, text="2",
                                                  command=Cap2_Filipeni)
    ButtonCap2_Filipeni.grid(column=2, row=2, padx=10, pady=10)

    ButtonCap3_Filipeni = customtkinter.CTkButton(Capitole_Frame_Filipeni, width=30, height=20, text="3",
                                                  command=Cap3_Filipeni)
    ButtonCap3_Filipeni.grid(column=3, row=2, padx=10, pady=10)

    ButtonCap4_Filipeni = customtkinter.CTkButton(Capitole_Frame_Filipeni, width=30, height=20, text="4",
                                                  command=Cap4_Filipeni)
    ButtonCap4_Filipeni.grid(column=4, row=2, padx=10, pady=10)

    # crearea unui frame pentru afișarea versetelor din fiecare capitol
    Versete_Frame_Filipeni = customtkinter.CTkFrame(Filipeni_Window, corner_radius=10)
    Versete_Frame_Filipeni.grid(column=1, row=3, columnspan=6)

    # textbox-ul pentru versetele Bibliei
    Versete_Filipeni_Text = Text(Versete_Frame_Filipeni, height=20, width=80, wrap=WORD, bd=0, bg="#292929",
                                 fg="silver",
                                 font=("Calibri", 15))
    Versete_Filipeni_Text.grid(column=1, row=3, columnspan=6, pady=5, padx=5)

    # punerea unui scroll down pentru versetele Bibliei
    Versete_Filipeni_Scrollbar = customtkinter.CTkScrollbar(Versete_Frame_Filipeni, command=Versete_Filipeni_Text.yview)
    Versete_Filipeni_Scrollbar.grid(column=7, row=3, sticky="ns")

    # conectarea scroll down-ului la textbox
    Versete_Filipeni_Text.configure(yscrollcommand=Versete_Filipeni_Scrollbar.set)

    # crearea unui buton de iesire
    Button_Iesire_Filipeni = customtkinter.CTkButton(Filipeni_Window, width=100, height=40, text="Close page",
                                                     command=Filipeni_Window.destroy)
    Button_Iesire_Filipeni.grid(column=2, row=4, columnspan=4, padx=10, pady=10)


def OpenColoseni():
    def Cap1_Coloseni():
        Versete_Coloseni_Text.delete(0.0, END)
        with open('Coloseni.txt', 'r') as f:
            for line in f:
                if line[0] == "1":
                    Versete_Coloseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap2_Coloseni():
        Versete_Coloseni_Text.delete(0.0, END)
        with open('Coloseni.txt', 'r') as f:
            for line in f:
                if line[0] == "2":
                    Versete_Coloseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap3_Coloseni():
        Versete_Coloseni_Text.delete(0.0, END)
        with open('Coloseni.txt', 'r') as f:
            for line in f:
                if line[0] == "3":
                    Versete_Coloseni_Text.insert(tkinter.INSERT, chars=line[2:])

    def Cap4_Coloseni():
        Versete_Coloseni_Text.delete(0.0, END)
        with open('Coloseni.txt', 'r') as f:
            for line in f:
                if line[0] == "4":
                    Versete_Coloseni_Text.insert(tkinter.INSERT, chars=line[2:])

    # crearea ferestrei pentru cartea Coloseni
    Coloseni_Window = customtkinter.CTkToplevel()
    Coloseni_Window.title("Coloseni")
    Coloseni_Window.geometry("800x570")
    Coloseni_Window.resizable(0, 0)
    Coloseni_Window.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
    Coloseni_Window.rowconfigure((0, 1, 2, 3), weight=0)

    # setarea imaginii pentru fereastra Filipeni
    Label_Coloseni = Label(Coloseni_Window, image=bgimagine_book)
    Label_Coloseni.place(x=-2, y=-2)

    # crearea titlului pentru cartea Coloseni
    titlu_Coloseni = customtkinter.CTkLabel(Coloseni_Window, font=("Times New Roman", 34), text="Coloseni")
    titlu_Coloseni.grid(column=2, row=0, columnspan=4)

    # crearea unui subtitlu cu numele Capitole
    subtitlu_Coloseni = customtkinter.CTkLabel(Coloseni_Window, font=("Times New Roman", 18), text="Capitole")
    subtitlu_Coloseni.grid(column=2, row=1, columnspan=4)

    # crearea unui frame pentru capitolele din Coloseni
    Capitole_Frame_Coloseni = customtkinter.CTkFrame(Coloseni_Window, corner_radius=10)
    Capitole_Frame_Coloseni.grid(column=1, row=2, columnspan=6)

    # crearea butoanelor
    ButtonCap1_Coloseni = customtkinter.CTkButton(Capitole_Frame_Coloseni, width=30, height=20, text="1",
                                                  command=Cap1_Coloseni)
    ButtonCap1_Coloseni.grid(column=1, row=2, padx=10, pady=10)

    ButtonCap2_Coloseni = customtkinter.CTkButton(Capitole_Frame_Coloseni, width=30, height=20, text="2",
                                                  command=Cap2_Coloseni)
    ButtonCap2_Coloseni.grid(column=2, row=2, padx=10, pady=10)

    ButtonCap3_Coloseni = customtkinter.CTkButton(Capitole_Frame_Coloseni, width=30, height=20, text="3",
                                                  command=Cap3_Coloseni)
    ButtonCap3_Coloseni.grid(column=3, row=2, padx=10, pady=10)

    ButtonCap4_Coloseni = customtkinter.CTkButton(Capitole_Frame_Coloseni, width=30, height=20, text="4",
                                                  command=Cap4_Coloseni)
    ButtonCap4_Coloseni.grid(column=4, row=2, padx=10, pady=10)

    # crearea unui frame pentru afisarea versetelor din fiecare capitol
    Versete_Frame_Coloseni = customtkinter.CTkFrame(Coloseni_Window, corner_radius=10)
    Versete_Frame_Coloseni.grid(column=1, row=3, columnspan=6)

    # textbox-ul pentru versetele Bibliei
    Versete_Coloseni_Text = Text(Versete_Frame_Coloseni, height=20, width=80, wrap=WORD, bd=0, bg="#292929",
                                 fg="silver",
                                 font=("Calibri", 15))
    Versete_Coloseni_Text.grid(column=1, row=3, columnspan=6, pady=5, padx=5)

    # punerea unui scroll down pentru versetele Bibliei
    Versete_Coloseni_Scrollbar = customtkinter.CTkScrollbar(Versete_Frame_Coloseni, command=Versete_Coloseni_Text.yview)
    Versete_Coloseni_Scrollbar.grid(column=7, row=3, sticky="ns")

    # conectarea scroll down-ului la textbox
    Versete_Coloseni_Text.configure(yscrollcommand=Versete_Coloseni_Scrollbar.set)

    # crearea unui buton de iesire
    Button_Iesire_Coloseni = customtkinter.CTkButton(Coloseni_Window, width=100, height=40, text="Close page",
                                                     command=Coloseni_Window.destroy)
    Button_Iesire_Coloseni.grid(column=2, row=4, columnspan=4, padx=10, pady=10)


# setarea titlului paginii principale
titlu = customtkinter.CTkLabel(root, font=("Times New Roman", 30), text="Biblia sau Sfânta Scriptură",
                               bg_color="transparent")
titlu.grid(column=4, row=0)

# crearea subtitlurilor
Text_Cartile_Bibliei = customtkinter.CTkLabel(root, text="Cartile Bibliei")
Text_Cartile_Bibliei.grid(column=0, row=1, columnspan=2)

Text_Cautare_Avansata = customtkinter.CTkLabel(root, text="Căutare avansată")
Text_Cautare_Avansata.grid(column=4, row=1)

Text_Versetul_Zilei = customtkinter.CTkLabel(root, text="Versetul zilei")
Text_Versetul_Zilei.grid(column=5, row=1)

# crearea unui frame pentru butonul de cautare si casuta de cautare
SearchFrame = customtkinter.CTkFrame(root, corner_radius=10, width=200, height=200)
SearchFrame.grid(column=4, row=2)

# crearea casutei de cautare
SearchEntry = customtkinter.CTkEntry(SearchFrame, width=315, height=40, border_width=1, text_color="silver",
                                     placeholder_text="căutați un cuvânt")
SearchEntry.configure(textvariable=CuvantCautat)
SearchEntry.grid(column=4, row=2, padx=10, pady=10)

# crearea butonului de cautare
SearchButton = customtkinter.CTkButton(SearchFrame, text="cautati", command=CautareAvansata)
SearchButton.grid(column=4, row=3, padx=10, pady=10)

# crearea unui frame pentru afisarea versetelor cautate
Versete_Cautate_Frame = customtkinter.CTkFrame(root, corner_radius=10)
Versete_Cautate_Frame.grid(column=4, row=3)

# textbox-ul pentru versetele cautate
VerseteCauate_Text = Text(Versete_Cautate_Frame, height=20, width=63, wrap=WORD, bd=0, bg="#292929", fg="silver",
                          font=("Calibri", 14))
VerseteCauate_Text.grid(column=4, row=3, pady=5, padx=5)
# VerseteCauate_Text['state'] = 'disabled'

# punerea unui scroll down
VerseteCauate_Scrollbar = customtkinter.CTkScrollbar(Versete_Cautate_Frame, command=VerseteCauate_Text.yview)
VerseteCauate_Scrollbar.grid(column=5, row=3, sticky="ns")

# conectarea scroll down-ului la textbox
VerseteCauate_Text.configure(yscrollcommand=VerseteCauate_Scrollbar.set)

# VerseteCauate_Text.tag_config("highlight", background="lightblue", foreground="black")
# VerseteCauate_Text.tag_lower("highlight")  # pentru a asigura că textul evidențiat este sub textul normal
# VerseteCauate_Text.tag_raise("sel")  # pentru a asigura că selecția utilizatorului este întotdeauna vizibilă
# VerseteCauate_Text.tag_raise("highlight")  # pentru a asigura că textul evidențiat este întotdeauna vizibil


# crearea unui frame pentru versetul zilei
Versetul_Zilei_Frame = customtkinter.CTkFrame(root, corner_radius=10, fg_color="#295699")
Versetul_Zilei_Frame.grid(column=5, row=2)

# crearea unui textbox pentru versetul zilei
Versetul_Zilei_Text = Text(Versetul_Zilei_Frame, height=7, width=35, wrap=WORD, bd=0, bg="#292938",
                           fg="silver", font=("Calibri", 16))
Versetul_Zilei_Text.grid(column=5, row=2, pady=4, padx=4)
Versetul_Zilei_Text.insert(tkinter.INSERT, chars=VersZilei())
Versetul_Zilei_Text['state'] = 'disabled'

# crearea unui frame pentru butoanele cartilor din Biblie
Capitole_Frame = customtkinter.CTkFrame(root, corner_radius=10)
Capitole_Frame.grid(column=0, row=2, columnspan=4)

# crearea butoanelor pentru cartile Bibliei
Button1 = customtkinter.CTkButton(Capitole_Frame, width=50, height=25, text="Gal.", command=OpenGalateni)
Button1.grid(column=0, row=2, padx=10, pady=10)

Button2 = customtkinter.CTkButton(Capitole_Frame, width=50, height=25, text="Efes.", command=OpenEfeseni)
Button2.grid(column=1, row=2, padx=10, pady=10)

Button3 = customtkinter.CTkButton(Capitole_Frame, width=50, height=25, text="Filip.", command=OpenFilipeni)
Button3.grid(column=2, row=2, padx=10, pady=10)

Button4 = customtkinter.CTkButton(Capitole_Frame, width=50, height=25, text="Col.", command=OpenColoseni)
Button4.grid(column=3, row=2, padx=10, pady=10)

# crearea unui buton de iesire
Button_Exit = customtkinter.CTkButton(root, width=100, height=40, text="Close page", command=root.destroy)
Button_Exit.grid(column=4, row=5, padx=10, pady=10)

Mesaj = customtkinter.CTkLabel(Capitole_Frame, font=("Calibri", 15), text="Alegeți o carte să citiți",
                               text_color="silver")
Mesaj.grid(column=1, row=3, columnspan=2)

root.mainloop()
