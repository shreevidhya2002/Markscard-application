"""------------------------------------ Project Made By Shree Vidhya-----------------------------------------------"""

from tkinter import *

import random

import time

from tkinter import messagebox

root = Tk()

root.geometry("1200x700+0+0")       # Geometric measurement of the system created

root.title("Report Card")      # Title is set

root.configure(background='yellow')


Tops = Frame(root, width=1150, height=90, bd=12, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=650, height=750, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=200, height=950, bd=9, relief="raise")
f2.pack(side=RIGHT)

f1a = Frame(f1, width=800, height=130, bd=6, relief="raise")
f1a.pack(side=TOP)

f2a = Frame(f1, width=750, height=520, bd=6, relief="raise")
f2a.pack(fill=BOTH, side=BOTTOM)

ft2 = Frame(f2, width=440, height=450, bd=12, relief="raise")
ft2.pack(side=TOP)

fb2 = Frame(f2, width=440, height=750, bd=16, relief="raise")
fb2.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1aa.pack(side=LEFT)

f1ab = Frame(f1a, width=400, height=330, bd=16, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2aa.pack(side=LEFT)

f2ab = Frame(f2a, width=450, height=330, bd=14, relief="raise")
f2ab.pack(side=RIGHT)

# ============================ Configuration set background black ==================================================

Tops.configure(background='white')
f1.configure(background='white')
f2.configure(background='white')

# =========================================== Label Set on Top to Restaurant MS =================================

lblInfo = Label(Tops, font=('arial', 44, 'bold',), text="Report Card", bd=9,)
lblInfo.grid(row=0, column=0)

# ============================================== Methods Declaration ================================================


# ======================================================== Cost of Items ====================================

def CostofItems():

    Subject1 = float(E_DAA.get())
    Subject2 = float(E_DMS.get())
    Subject3 = float(E_DBMS.get())
    Subject4 = float(E_OOPS.get())
    Subject5 = float(E_DC.get())
    Subject6 = float(E_DS.get())
    Subject7 = float(E_FS.get())
    Subject8 = float(E_WTA.get())

    Subject9 = float(E_ENGLISH.get())
    Subject10 = float(E_KANNADA.get())
    Subject11 = float(E_HINDI.get())
    Subject12 = float(E_MATHS.get())
    Subject13 = float(E_SCIENCE.get())
    Subject14 = float(E_SOCIAL.get())
    Subject15 = float(E_GEOGRAPHY.get())
    Subject16 = float(E_HISTORY.get())

    TotalofA =(Subject1 * 1) + (Subject2 * 1) + (Subject3 * 1) + (Subject4 *1) + (Subject5 * 1) + (Subject6 * 1) +\
                   (Subject7 * 1) + (Subject8 * 1)
    print(TotalofA)

    TotalofB =(Subject9 * 1) + (Subject10 * 1) + (Subject11 * 1) + (Subject12 *1) + (Subject13 * 1) + \
                  (Subject14 * 1) + (Subject15 * 1) + (Subject16 * 1)
    print(TotalofB)

    TotalA = " "+ str('%.2d' % TotalofA)
    TotalB = " "+ str("%.2d" % TotalofB)
    PartA.set(TotalA)
    PartB.set(TotalB)
    SC = " "+ str("%.2d" % 0.15)
    print(SC)
    ServiceCharge.set(SC)

    SubTotalofSUBJECTS = " "+ str(round(TotalofA + TotalofB +0))
    SubTotal.set(SubTotalofSUBJECTS)

   
    TT = ((TotalofA + TotalofB)*0)
    TC = " "+ str(round((TotalofA + TotalofB ) + TT))
    print((TC))
    TotalCost.set(TC)
    
    Percentage = (((TotalofA + TotalofB)/ (625))*100)
    Percentage=" "+ str("%.2f" % Percentage)
    print(Percentage)

# ================================================ Exit the Main frame ===============================================


def qExit():

    qExit = messagebox.askyesno("Quit System", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

# ================================================== Reset the Entries Module =========================================


def Reset():


    SubTotal.set("")
    TotalCost.set("")
    PartA.set("")
    PartB.set("")
    Percentage.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0", END)

    E_DAA.set("0")
    E_DMS.set("0")
    E_DBMS.set("0")
    E_OOPS.set("0")
    E_DC.set("0")
    E_DS.set("0")
    E_FS.set("0")
    E_WTA.set("0")

    E_ENGLISH.set("0")
    E_KANNADA.set("0")
    E_HINDI.set("0")
    E_MATHS.set("0")
    E_SCIENCE.set("0")
    E_SOCIAL.set("0")
    E_GEOGRAPHY.set("0")
    E_HISTORY.set("0")

    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    txtSCIENCE.configure(state=DISABLED)
    txtDMS.configure(state=DISABLED)
    txtDBMS.configure(state=DISABLED)
    txtOOPS.configure(state=DISABLED)
    txtDC.configure(state=DISABLED)
    txtDS.configure(state=DISABLED)
    txtFS.configure(state=DISABLED)
    txtWTA.configure(state=DISABLED)
    txtENGLISH.configure(state=DISABLED)
    txtKANNADA.configure(state=DISABLED)
    txtHINDI.configure(state=DISABLED)
    txtMATHS.configure(state=DISABLED)
    txtSCIENCE.configure(state=DISABLED)
    txtSOCIAL.configure(state=DISABLED)
    txtGEOGRAPHY.configure(state=DISABLED)
    txtHISTORY.configure(state=DISABLED)

# ====================================================== Added Receipt Functionality Module ======================

def Receipt():
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref:\t\t\t'+ Receipt_Ref.get() + '\t\t' + DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Subjects\t\t\t\t' + "Marks scored\n\n")
    txtReceipt.insert(END, 'DAA:\t\t\t\t\t' + E_DAA.get() + "\n")
    txtReceipt.insert(END, 'DMS : \t\t\t\t\t' + E_DMS.get() + "\n")
    txtReceipt.insert(END, 'DBMS: \t\t\t\t\t' + E_DBMS.get() + "\n")
    txtReceipt.insert(END, 'OOPS: \t\t\t\t\t' + E_OOPS.get() + "\n")
    txtReceipt.insert(END, 'DC: \t\t\t\t\t' + E_DC.get() + "\n")
    txtReceipt.insert(END, 'DS: \t\t\t\t\t' + E_DS.get() + "\n")
    txtReceipt.insert(END, 'FS: \t\t\t\t\t' + E_FS.get() + "\n")
    txtReceipt.insert(END, 'WTA: \t\t\t\t\t' + E_WTA.get() + "\n")
    txtReceipt.insert(END, 'ENGLISH: \t\t\t\t\t' + E_ENGLISH.get() + "\n")
    txtReceipt.insert(END, 'KANNADA: \t\t\t\t\t' + E_KANNADA.get() + "\n")
    txtReceipt.insert(END, 'HINDI: \t\t\t\t\t' + E_HINDI.get() + "\n")
    txtReceipt.insert(END, 'MATHS: \t\t\t\t\t' + E_MATHS.get() + "\n")
    txtReceipt.insert(END, 'SCIENCE: \t\t\t\t\t' + E_SCIENCE.get() + "\n")
    txtReceipt.insert(END, 'SOCIAL: \t\t\t\t\t' + E_SOCIAL.get() + "\n")
    txtReceipt.insert(END, 'GEOGRAPHY: \t\t\t\t\t' + E_GEOGRAPHY.get() + "\n")
    txtReceipt.insert(END, 'HISTORY: \t\t\t\t\t' + E_HISTORY.get() + "\n")
  
    txtReceipt.insert(END, 'Part-B: \t\t\t\t\t' + Part-B.get() + "\t\t\tSub Total:\t\t\t\t\t" +
                      SubTotal.get() + "\n")
    


# ============================================ CheckButton check performed module ====================================


def chkbutton_value():
    if var1.get() == 1:
        txtDAA.configure(state=NORMAL)
    elif var1.get() == 0:
        txtDAA.configure(state=DISABLED)
        E_DAA.set("0")
    if var2.get() == 1:
        txtDMS.configure(state=NORMAL)
    elif var2.get() == 0:
        txtDMS.configure(state=DISABLED)
        E_DMS.set("0")
    if var3.get() == 1:
        txtDBMS.configure(state=NORMAL)
    elif var3.get() == 0:
        txtDBMS.configure(state=DISABLED)
        E_DBMS.set("0")
    if var4.get() == 1:
        txtOOPS.configure(state=NORMAL)
    elif var4.get() == 0:
        txtOOPS.configure(state=DISABLED)
        E_OOPS.set("0")
    if var5.get() == 1:
        txtDC.configure(state=NORMAL)
    elif var5.get() == 0:
        txtDC.configure(state=DISABLED)
        E_DC.set("0")
    if var6.get() == 1:
        txtDS.configure(state=NORMAL)
    elif var6.get() == 0:
        txtDS.configure(state=DISABLED)
        E_DS.set("0")
    if var7.get() == 1:
        txtFS.configure(state=NORMAL)
    elif var7.get() == 0:
        txtFS.configure(state=DISABLED)
        E_FS.set("0")
    if var8.get() == 1:
        txtWTA.configure(state=NORMAL)
    elif var8.get() == 0:
        txtWTA.configure(state=DISABLED)
        E_WTA.set("0")
    if var9.get() == 1:
        txtENGLISH.configure(state=NORMAL)
    elif var9.get() == 0:
        txtENGLISH.configure(state=DISABLED)
        E_ENGLISH.set("0")
    if var10.get() == 1:
        txtKANNADA.configure(state=NORMAL)
    elif var10.get() == 0:
        txtKANNADA.configure(state=DISABLED)
        E_KANNADA.set("0")
    if var11.get() == 1:
        txtHINDI.configure(state=NORMAL)
    elif var11.get() == 0:
        txtHINDI.configure(state=DISABLED)
        E_HINDI.set("0")
    if var12.get() == 1:
        txtMATHS.configure(state=NORMAL)
    elif var12.get() == 0:
        txtMATHS.configure(state=DISABLED)
        E_MATHS.set("0")
    if var13.get() == 1:
        txtSCIENCE.configure(state=NORMAL)
    elif var13.get() == 0:
        txtSCIENCE.configure(state=DISABLED)
        E_SCIENCE.set("0")
    if var14.get() == 1:
        txtSOCIAL.configure(state=NORMAL)
    elif var14.get() == 0:
        txtSOCIAL.configure(state=DISABLED)
        E_SOCIAL.set("0")
    if var15.get() == 1:
        txtGEOGRAPHY.configure(state=NORMAL)
    elif var15.get() == 0:
        txtGEOGRAPHY.configure(state=DISABLED)
        E_GEOGRAPHY.set("0")
    if var16.get() == 1:
        txtHISTORY.configure(state=NORMAL)
    elif var16.get() == 0:
        txtHISTORY.configure(state=DISABLED)
        E_HISTORY.set("0")

# =======================================================================================================


# ======================================================= Variables ===============================================


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
PartB = StringVar()
PartA = StringVar()
Percentage = StringVar()
ServiceCharge = StringVar()

E_DAA = StringVar()
E_DMS = StringVar()
E_DBMS = StringVar()
E_OOPS = StringVar()
E_DC = StringVar()
E_DS = StringVar()
E_FS = StringVar()
E_WTA = StringVar()

E_ENGLISH = StringVar()
E_KANNADA = StringVar()
E_HINDI = StringVar()
E_MATHS = StringVar()
E_SCIENCE = StringVar()
E_SOCIAL = StringVar()
E_GEOGRAPHY = StringVar()
E_HISTORY = StringVar()


E_DAA.set("0")
E_DMS.set("0")
E_DBMS.set("0")
E_OOPS.set("0")
E_DC.set("0")
E_DS.set("0")
E_FS.set("0")
E_WTA.set("0")


E_ENGLISH.set("0")
E_KANNADA.set("0")
E_HINDI.set("0")
E_MATHS.set("0")
E_SCIENCE.set("0")
E_SOCIAL.set("0")
E_GEOGRAPHY.set("0")
E_HISTORY.set("0")

# ===================================================== Date Declared =============================================

DateofOrder.set(time.strftime("%d/%m/%y"))

# ====================================== Food Check buttons =======================================================

DAA = Checkbutton(f1aa, font=('arial',18, 'bold'), text="DAA \t", variable=var1, onvalue=1,
                    offvalue=0, command=chkbutton_value).grid(row=0, sticky=W)

DMS = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="DMS \t", variable=var2, onvalue=1,
                       offvalue=0, command=chkbutton_value).grid(row=1, sticky=W)

DBMS = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="DBMS \t", variable=var3, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=2, sticky=W)

OOPS = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="OOPS \t", variable=var4, onvalue=1,
                          offvalue=0, command=chkbutton_value).grid(row=3, sticky=W)

DC = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="DC \t", variable=var5, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=4, sticky=W)

DS = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="DS \t", variable=var6, onvalue=1,
                             offvalue=0, command=chkbutton_value).grid(row=5, sticky=W)

FS = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="FS \t", variable=var7, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=6, sticky=W)

WTA = Checkbutton(f1aa, font=('arial', 18, 'bold'), text="WTA \t", variable=var8, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=7, sticky=W)

# ====================================== Drinks & Cake Check Buttons ================================================

ENGLISH = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="ENGLISH \t", variable=var9, onvalue=1,
                         offvalue=0, command=chkbutton_value).grid(row=0, sticky=W)

KANNADA = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="KANNADA \t", variable=var10, onvalue=1,
                              offvalue=0, command=chkbutton_value).grid(row=1, sticky=W)

HINDI_Cake = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="HINDI \t", variable=var11,
                                onvalue=1, offvalue=0, command=chkbutton_value).grid(row=2, sticky=W)

MATHS = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="MATHS \t", variable=var12, onvalue=1,
                                offvalue=0, command=chkbutton_value).grid(row=3, sticky=W)

SCIENCE = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="SCIENCE \t", variable=var13,
                                   onvalue=1, offvalue=0, command=chkbutton_value).grid(row=4, sticky=W)

SOCIAL = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="SOCIAL \t", variable=var14,
                                     onvalue=1, offvalue=0, command=chkbutton_value).grid(row=5, sticky=W)

GEOGRAPHY = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="GEOGRAPHY \t", variable=var15, onvalue=1,
                                offvalue=0, command=chkbutton_value).grid(row=6, sticky=W)

HISTORY = Checkbutton(f1ab, font=('arial', 18, 'bold'), text="HISTORY \t", variable=var16,
                              onvalue=1, offvalue=0, command=chkbutton_value).grid(row=7, sticky=W)

# ====================================== Entry Widget for  Part-A===============================================

txtDAA = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_DAA, state=DISABLED)
txtDAA.grid(row=0, column=1)
txtDMS = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_DMS,
                    state=DISABLED)
txtDMS.grid(row=1, column=1)
txtDBMS = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_DBMS,
                      state=DISABLED)
txtDBMS.grid(row=2, column=1)
txtOOPS = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_OOPS,
                       state=DISABLED)
txtOOPS.grid(row=3, column=1)
txtDC = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_DC,
                      state=DISABLED)
txtDC.grid(row=4, column=1)
txtDS = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left', textvariable=E_DS
                          , state=DISABLED)
txtDS.grid(row=5, column=1)
txtFS = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_FS, state=DISABLED)
txtFS.grid(row=6, column=1)
txtWTA = Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_WTA, state=DISABLED)
txtWTA.grid(row=7, column=1)

# ====================================== Entry Widget for Part-B ===================================================

txtENGLISH = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                       textvariable=E_ENGLISH, state=DISABLED)
txtENGLISH.grid(row=0, column=1)
txtKANNADA = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                          textvariable=E_KANNADA, state=DISABLED)
txtKANNADA.grid(row=1, column=1)
txtHINDI = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_HINDI, state=DISABLED)
txtHINDI.grid(row=2, column=1)
txtMATHS = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_MATHS, state=DISABLED)
txtMATHS.grid(row=3, column=1)
txtSCIENCE = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                textvariable=E_SCIENCE, state=DISABLED)
txtSCIENCE.grid(row=4, column=1)
txtSOCIAL = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                                 textvariable=E_SOCIAL, state=DISABLED)
txtSOCIAL.grid(row=5, column=1)
txtGEOGRAPHY = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                             textvariable=E_GEOGRAPHY, state=DISABLED)
txtGEOGRAPHY.grid(row=6, column=1)
txtHISTORY = Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6, justify='left',
                           textvariable=E_HISTORY, state=DISABLED)
txtHISTORY.grid(row=7, column=1)

# ========================================== Receipt Information ====================================================

lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt", bd=2, anchor='w')
lblReceipt.grid(row=0, column=0, sticky=W)
txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
txtReceipt.grid(row=1, column=0, sticky=W+E)

# =================================== Cost Items Information(f2aa) ==================================================

lblPartA = Label(f2aa, font=('arial', 16, 'bold'), text="Part-A Marks", bd=8)
lblPartA.grid(row=2, column=0, sticky=W)
txtPartA = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=PartA)
txtPartA.grid(row=2, column=1)

lblPartB = Label(f2aa, font=('arial', 16, 'bold'), text="Part-B Marks", bd=8)
lblPartB.grid(row=3, column=0, sticky=W)
txtPartB = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=PartB)
txtPartB.grid(row=3, column=1, sticky=W)



# ======================================Marks Information(f2ab)===================================================



lblTotalCost = Label(f2ab, font=('arial', 16, 'bold'), text="Total", bd=8)
lblTotalCost.grid(row=4, column=0, sticky=W)
print(TotalCost)
txtTotalCost = Entry(f2ab, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=TotalCost)
txtTotalCost.grid(row=4, column=1, sticky=W)


lblPercentage = Label(f2aa, font=('arial', 16, 'bold'), text="Percentage", bd=8)
lblPercentage.grid(row=5, column=0, sticky=W)
txtPercentage = Entry(f2aa, font=('arial', 16, 'bold'), bd=8, justify="left", textvariable=PartA)
txtPercentage.grid(row=5, column=1)


# ======================================Button===================================================

btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Total", command=CostofItems).grid(row=0, column=0, sticky=W+E+N+S)
btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                    text="Receipt", command=Receipt).grid(row=0, column=1, sticky=W+E+N+S)
btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                  text="Reset", command=Reset).grid(row=0, column=2, sticky=W+E+N+S)
btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16, 'bold'), width=5,
                 text="Exit", command=qExit).grid(row=0, column=3, sticky=W+E+N+S)




root.mainloop()



