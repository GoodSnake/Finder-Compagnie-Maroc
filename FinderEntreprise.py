import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import requests
from bs4 import BeautifulSoup
c_Nom = "Nom"
c_act = "Activiter"
c_ICE = "ICE"
c_IF = "IF"
c_CRC = "Centre RC"
c_RC = "RC"
c_Adresse = "Adresse"
def getCompagnyinfo(IFNUM):
    API_ENDPOINT = "https://simpl-recherche.tax.gov.ma/RechercheEntreprise/result"
    data = {"param['type']": "IF",
            "param['criteria']": IFNUM}


    r = requests.post(url=API_ENDPOINT, data=data)
    # extracting response text
    pastebin_url = r.text

    soup = BeautifulSoup(r.text,features="html.parser")
    x = 0
    for textarea in soup.find_all("textarea"):
        x = x + 1
        print(x)
        print(textarea.get_text())
        if(x == 1):
            c_Nom = textarea.get_text()
        if (x == 2):
            c_act = textarea.get_text()
        if (x == 3):
            c_Adresse = textarea.get_text()

    for input in soup.find_all("input"):
        x = x + 1
        print(x)
        print(input.get('value'))
        if (x == 7):
            c_IF =input.get('value')
        if (x == 9):
            c_ICE =input.get('value')
        if (x == 11):
            c_CRC = input.get('value')
        if (x == 12):
            c_RC = input.get('value')

    text_var.set(c_Nom)
    text_var2.set(c_act)
    text_var3.set(c_Adresse)
    text_var4.set(c_IF)
    text_var5.set(c_ICE)
    text_var6.set(c_CRC)
    text_var7.set(c_RC)






##
okno = tk.Tk()
label = Label(okno, text="Entrez l'IF de l'entreprise")
label.pack()
# bouton de recup info
def recupere():
    getCompagnyinfo(entree.get())
value = StringVar()
value.set("")
entree = Entry(okno, textvariable=value, width=30)
entree.pack()

bouton = Button(okno, text="Valider", command=recupere)
bouton.pack()
text_var = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
# setting now the text
text_var.set(c_Nom)
# a textvariable is used.
# remind, if you need the reference to Label,
# you need two line. The method pack returns none.
text_var2 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var2,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var2.set(c_act)
#
text_var3 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var3,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var3.set(c_Adresse)
#
text_var4 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var4,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var4.set(c_IF)
#
text_var5 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var5,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var5.set(c_ICE)
#
text_var6 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var6,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var6.set(c_CRC)
#
text_var7 = tk.StringVar(okno)
tk.Label(okno, textvariable=text_var7,  bg="White",width=100, height=2).pack(padx = 5, pady = 5)
text_var7.set(c_RC)
#
# bouton de sortie
bouton=Button(okno, text="Fermer", command=okno.quit)
bouton.pack()

okno.mainloop()
