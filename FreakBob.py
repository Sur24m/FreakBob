import tkinter as tk
from tkinter import messagebox
okno=tk.Tk()
okno.geometry("277x160")
global balance1
balance1=500
global balance2
balance2=500
#hrac 1
def skibidi11():
    global hrac1
    hrac1="skibidi"
def nuzky11():
    global hrac1
    hrac1="nuzky"
def kamen11():
    global hrac1
    hrac1="kamen"
def papir11():
    global hrac1
    hrac1="papir"
global hrac1
global hrac2
hrac1="pepa"
hrac2="pepa"

#hrac 2
def skibidi22():
    global hrac2
    hrac2="skibidi"
def nuzky22():
    global hrac2
    hrac2="nuzky"
def kamen22():
    global hrac2
    hrac2="kamen"
def papir22():
    global hrac2
    hrac2="papir"

def hra():
    global hrac1
    global hrac2
    global balance1
    global balance2
    while True:
        sazka1=(bet1.get())
        sazka2=(bet2.get())
        jmeno1=str(entryjmeno1.get())
        jmeno2=str(entryjmeno2.get())

        if jmeno1=="" or jmeno2=="":
            messagebox.showinfo("Error","Nezapomeňte zadat jméno")
            break
        if hrac1=="kamen":
            hrac11="Kámen"
        elif hrac1=="papir":
            hrac11="Papír"
        elif hrac1=="nuzky":
            hrac11="Nůžky"
        if hrac2=="kamen":
            hrac22="Kámen"
        elif hrac2=="papir":
            hrac22="Papír"
        elif hrac2=="nuzky":
            hrac22="Nůžky"
        if hrac1=="pepa" or hrac2=="pepa":
            messagebox.showinfo("Error","Nezapomeňte si vybrat kámen, nůžky nebo papír :)")
            break
        if sazka1=="":
            sazka1=0
        if sazka2=="":
            sazka2=0
        if sazka1 != sazka2:
            messagebox.showinfo("Error",f"Hodnota sázky hráče {jmeno1} musí být stejná jako hodnota sázky hráče {jmeno2}")
            hrac2="pepa"
            hrac1="pepa"
            break
        elif (hrac1=="kamen" and hrac2=="nuzky") or (hrac1=="papir" and hrac2=="kamen") or (hrac1=="nuzky" and hrac2=="papir"):
            result="vyhrál"
            balance1=balance1+sazka2
            balance2=balance2-sazka1
            messagebox.showinfo("vysledek",f"{jmeno1} {result}\n {jmeno1} si vybral {hrac11}\n {jmeno2} si vybral {hrac22}\n balance hráče {jmeno1} je {balance1}\n balance hráče {jmeno2} je {balance2}")
            hrac2="pepa"
            hrac1="pepa"
            break
        elif (hrac2=="kamen" and hrac1=="nuzky") or (hrac2=="papir" and hrac1=="kamen") or (hrac2=="nuzky" and hrac1=="papir"):
            result="vyhrál"
            balance2=balance2+sazka1
            balance1=balance1-sazka2
            messagebox.showinfo("vysledek",f"{jmeno2} {result}\n {jmeno1} si vybral {hrac11}\n {jmeno2} si vybral {hrac22}\n balance hráče {jmeno1} je {balance1} \n balance hráče {jmeno2} je {balance2}") 
            hrac2="pepa"
            hrac1="pepa"
            break
        elif (hrac1=="skibidi") and (hrac2!="skibidi") :
            messagebox.showinfo("vysledek",f"Ultimate skibidi Boss was summoned and {jmeno1} won, {jmeno2} was brutaly molested by a down syndrome skibidi toilet.\n žádný hráč nestratil žádné peníze")
            hrac2="pepa"
            hrac1="pepa"
            break
        elif (hrac2=="skibidi") and (hrac1!="skibidi") :
            messagebox.showinfo("vysledek",f"Ultimate skibidi Boss was summoned and {jmeno2} won, {jmeno1} was brutaly molested by a down syndrome skibidi toilet.\n žádný hráč nestratil žádné peníze")
            hrac2="pepa"
            hrac1="pepa"
            break
        elif (hrac2=="skibidi") and (hrac1=="skibidi") :
            messagebox.showinfo("vysledek",f"Ultimate skibidi Boss was summoned and nobody won, {jmeno1} and {jmeno2} were brutaly molested by a down syndrome skibidi toilet.\n žádný hráč nestratil žádné peníze")
            hrac2="pepa"
            hrac1="pepa"
            break
        elif hrac1 == hrac2:
            result="remíza"
            messagebox.showinfo(f"vysledek",f"{result}\n žádný hráč nestratil žádné peníze\n {jmeno1} si vybral {hrac11}\n {jmeno2} si vybral {hrac22}")
            hrac2="pepa"
            hrac1="pepa"
            break
        else: 
            messagebox.showinfo("vysledek",f"Tak seš kokot, nemuzes hrat {hrac1} s {hrac2}.")
            hrac2="pepa"
            hrac1="pepa"
            break
        
        
    
    
    
jmenolabel1=tk.Label(okno,text="Jméno hráče 1")
jmenolabel1.grid(column=0,row=0,sticky=tk.W+tk.E)
jmenolabel2=tk.Label(okno,text="Jméno hráče 2")
jmenolabel2.grid(column=2,row=0,sticky=tk.W+tk.E)
entryjmeno1=tk.Entry(okno)
entryjmeno1.grid(column=0,row=1,sticky=tk.W+tk.E)
entryjmeno2=tk.Entry(okno)
entryjmeno2.grid(column=2,row=1,sticky=tk.W+tk.E)

kamen1=tk.Button(okno,command=kamen11,text="Kámen")
kamen1.grid(column=0,row=2,sticky=tk.W+tk.E)
nuzky1=tk.Button(okno,command=nuzky11,text="Nůžky")
nuzky1.grid(column=0,row=3,sticky=tk.W+tk.E)
papir1=tk.Button(okno,command=papir11,text="Papír")
papir1.grid(column=0,row=4,sticky=tk.W+tk.E)

kamen2=tk.Button(okno,command=kamen22,text="Kámen")
kamen2.grid(column=2,row=2,sticky=tk.W+tk.E)
nuzky2=tk.Button(okno,command=nuzky22,text="Nůžky")
nuzky2.grid(column=2,row=3,sticky=tk.W+tk.E)
papir2=tk.Button(okno,command=papir22,text="Papír")
papir2.grid(column=2,row=4,sticky=tk.W+tk.E)
button=tk.Button(okno,text="Hra",command=hra)
button.grid(column=1 ,row=3 ,sticky=tk.W+tk.E)

betlabel1=tk.Label(okno,text="Sázka:")
betlabel1.grid(column=0,row=5,sticky=tk.W+tk.E)
betlabel2=tk.Label(okno,text="Sázka:")
betlabel2.grid(column=2,row=5,sticky=tk.W+tk.E)
bet1=tk.Entry(okno)
bet1.grid(row=6,column=0,sticky=tk.W+tk.E)
bet2=tk.Entry(okno)
bet2.grid(row=6,column=2,sticky=tk.W+tk.E)
label=tk.Label(okno)
label.grid(row=7,column=0)

skibidi1=tk.Button(okno,text="skibidi",command=skibidi11)
skibidi1.grid(row=8,column=0,sticky=tk.W+tk.E)
skibidi2=tk.Button(okno,text="skibidi",command=skibidi22)
skibidi2.grid(row=8,column=2,sticky=tk.W+tk.E)
okno.mainloop()
