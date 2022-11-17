from tkinter import *
import random 
from PIL import ImageTk,Image
from tkinter import messagebox    
from tkinter import font as tkFont


run = True
while run:

    #------------   GUI WINDOW  -------------------
    root = Tk()
    root.title(" Hangman Game")
    root.geometry("900x600")
    
    root['bg']='#8D72E1'
    

    #*******************************************************  ICON     *******************************************************

    # ------------- ICON IMAGE -----------
    root.iconbitmap('icon.ico')

    # ------------- DATA FOR THE GAME -------------

    myli = ['cat.png','dog.png','lion.png','zebra.png']
    words = ['CAT','DOG','LION','ZEBRA']
    hangman = ['img1.png','img2.png','img3.png','img4.png']

    #global variables

    #sr=''
    global mi
    mi=[' ', ' ', ' ', ' ', ' ', ' ']
    t = 0




    #------------- RANDOM NUMBER GENERATE  ------------------------
    p= random.randint(0,3)
    guess = words[p]

    #****************************************************** BUTTONS   *****************************************************
    def onclick1(): alp1['state'],alp1['relief'],alp1['bg'] = DISABLED,'sunken','red'
    def onclick2(): alp2['state'],alp2['relief'],alp2['bg'] = DISABLED,'sunken','red'
    def onclick3(): alp3['state'],alp3['relief'],alp3['bg'] = DISABLED,'sunken','red'
    def onclick4(): alp4['state'],alp4['relief'],alp4['bg'] = DISABLED,'sunken','red'
    def onclick5(): alp5['state'],alp5['relief'],alp5['bg'] = DISABLED,'sunken','red'
    def onclick6(): alp6['state'],alp6['relief'],alp6['bg'] = DISABLED,'sunken','red'
    def onclick7(): alp7['state'],alp7['relief'],alp7['bg'] = DISABLED,'sunken','red'
    def onclick8(): alp8['state'],alp8['relief'],alp8['bg'] = DISABLED,'sunken','red'
    def onclick9(): alp9['state'],alp9['relief'],alp9['bg'] = DISABLED,'sunken','red'
    def onclick10(): alp10['state'],alp10['relief'],alp10['bg'] = DISABLED,'sunken','red'
    def onclick11(): alp11['state'],alp11['relief'],alp11['bg'] = DISABLED,'sunken','red'
    def onclick12(): alp12['state'],alp12['relief'],alp12['bg'] = DISABLED,'sunken','red'
    def onclick13(): alp13['state'],alp13['relief'],alp13['bg'] = DISABLED,'sunken','red'
    def onclick14(): alp14['state'],alp14['relief'],alp14['bg'] = DISABLED,'sunken','red'
    def onclick15(): alp15['state'],alp15['relief'],alp15['bg'] = DISABLED,'sunken','red'
    def onclick16(): alp16['state'],alp16['relief'],alp16['bg'] = DISABLED,'sunken','red'
    def onclick17(): alp17['state'],alp17['relief'],alp17['bg'] = DISABLED,'sunken','red'
    def onclick18(): alp18['state'],alp18['relief'],alp18['bg'] = DISABLED,'sunken','red'
    def onclick19(): alp19['state'],alp19['relief'],alp19['bg'] = DISABLED,'sunken','red'
    def onclick20(): alp20['state'],alp20['relief'],alp20['bg'] = DISABLED,'sunken','red'
    def onclick21(): alp21['state'],alp21['relief'],alp21['bg'] = DISABLED,'sunken','red'
    def onclick22(): alp22['state'],alp22['relief'],alp22['bg'] = DISABLED,'sunken','red'
    def onclick23(): alp23['state'],alp23['relief'],alp23['bg'] = DISABLED,'sunken','red'
    def onclick24(): alp24['state'],alp24['relief'],alp24['bg'] = DISABLED,'sunken','red'
    def onclick25(): alp25['state'],alp25['relief'],alp25['bg'] = DISABLED,'sunken','red'
    def onclick26(): alp26['state'],alp26['relief'],alp26['bg'] = DISABLED,'sunken','red'
        
    #--------------- BUTTONS ------------
    f = Frame(root,height=200,width=300,bg='#8D72E1')
    f.pack()
    f.place(x=175,y=280)
    alp1 = Button(f,text='A',padx=25,pady=8,bg='#ffd480',command=lambda:[click('A'),onclick1()])
    alp2 = Button(f,text='B',padx=25,pady=8,bg='#ffd480',command=lambda:[click('B'),onclick2()])
    alp3 = Button(f,text='C',padx=25,pady=8,bg='#ffd480',command=lambda:[click('C'),onclick3()])
    alp4 = Button(f,text='D',padx=25,pady=8,bg='#ffd480',command=lambda:[click('D'),onclick4()])
    alp5 = Button(f,text='E',padx=25,pady=8,bg='#ffd480',command=lambda:[click('E'),onclick5()])
    alp6 = Button(f,text='F',padx=25,pady=8,bg='#ffd480',command=lambda:[click('F'),onclick6()])
    alp7 = Button(f,text='G',padx=25,pady=8,bg='#ffd480',command=lambda:[click('G'),onclick7()])
    alp8 = Button(f,text='H',padx=25,pady=8,bg='#ffff80',command=lambda:[click('H'),onclick8()])
    alp9 = Button(f,text='I',padx=25,pady=8,bg='#ffff80',command=lambda:[click('I'),onclick9()])
    alp10= Button(f,text='J',padx=25,pady=8,bg='#ffff80',command=lambda:[click('J'),onclick10()])
    alp11= Button(f,text='K',padx=25,pady=8,bg='#ffff80',command=lambda:[click('K'),onclick11()])
    alp12= Button(f,text='L',padx=25,pady=8,bg='#ffff80',command=lambda:[click('L'),onclick12()])
    alp13= Button(f,text='M',padx=25,pady=8,bg='#ffff80',command=lambda:[click('M'),onclick13()])
    alp14= Button(f,text='N',padx=25,pady=8,bg='#ffff80',command=lambda:[click('N'),onclick14()])
    alp15= Button(f,text='O',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('O'),onclick15()])
    alp16= Button(f,text='P',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('P'),onclick16()])
    alp17= Button(f,text='Q',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('Q'),onclick17()])
    alp18= Button(f,text='R',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('R'),onclick18()])
    alp19= Button(f,text='S',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('S'),onclick19()])
    alp20= Button(f,text='T',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('T'),onclick20()])
    alp21= Button(f,text='U',padx=25,pady=8,bg='#ff99dd',command=lambda:[click('U'),onclick21()])
    alp22= Button(f,text='V',padx=25,pady=8,bg='#b3ffb3',command=lambda:[click('V'),onclick22()])
    alp23= Button(f,text='W',padx=25,pady=8,bg='#b3ffb3',command=lambda:[click('W'),onclick23()])
    alp24= Button(f,text='X',padx=25,pady=8,bg='#b3ffb3',command=lambda:[click('X'),onclick24()])
    alp25= Button(f,text='Y',padx=25,pady=8,bg='#b3ffb3',command=lambda:[click('Y'),onclick25()])
    alp26= Button(f,text='Z',padx=25,pady=8,bg='#b3ffb3',command=lambda:[click('Z'),onclick26()])


    alp1.grid(row=1,column=0,padx =7,pady=7)
    alp2.grid(row=1,column=1,padx =7,pady=7)
    alp3.grid(row=1,column=2,padx =7,pady=7)
    alp4.grid(row=1,column=3,padx =7,pady=7)
    alp5.grid(row=1,column=4,padx =7,pady=7)
    alp6.grid(row=1,column=5,padx =7,pady=7)
    alp7.grid(row=1,column=6,padx =7,pady=7)
    alp8.grid(row=2,column=0,padx =7,pady=7)
    alp9.grid(row=2,column=1,padx =7,pady=7)
    alp10.grid(row=2,column=2,padx =7,pady=7)
    alp11.grid(row=2,column=3,padx =7,pady=7)
    alp12.grid(row=2,column=4,padx =7,pady=7)
    alp13.grid(row=2,column=5,padx =7,pady=7)
    alp14.grid(row=2,column=6,padx =7,pady=7)
    alp15.grid(row=3,column=0,padx =7,pady=7)
    alp16.grid(row=3,column=1,padx =7,pady=7)
    alp17.grid(row=3,column=2,padx =7,pady=7)
    alp18.grid(row=3,column=3,padx =7,pady=7)
    alp19.grid(row=3,column=4,padx =7,pady=7)
    alp20.grid(row=3,column=5,padx =7,pady=7)
    alp21.grid(row=3,column=6,padx =7,pady=7)
    alp22.grid(row=4,column=1,padx =7,pady=7)
    alp23.grid(row=4,column=2,padx =7,pady=7)
    alp24.grid(row=4,column=3,padx =7,pady=7)
    alp25.grid(row=4,column=4,padx =7,pady=7)
    alp26.grid(row=4,column=5,padx =7,pady=7)
    
    #*********************************************** FUNCTIONS *******************************************************
    #---------- ACTIVE THE BUTTONS
    # def click(letter):
    #     pass:

    def click(letter):
        global t
        sr=' '
        if letter in guess:
            ind = guess.rfind(letter)
            mi.insert(ind,letter)

            for i in mi:
                if i != ' ':
                    sr+=i
            t+=1
            ent.delete(0,END)
            ent.insert(0,sr)
            if t== len(guess):
                answer = messagebox.askyesno('Result','Congratulation! You won the game \n Do you want to play Again  ')
                if answer == True:
                    restart()
                else:
                    close()


        else:
            not_word()


    count=3
   
    def not_word():
        global count
        if count != 0:
            count=count-1
            your='  '+str(count)
            enty.delete(0,END)
            enty.insert(0,your)
        else:
            answer = messagebox.askyesno("Result","Sorry!, You lost the game \n To Play Again ---> YES \n To Exit --> NO")
            if answer == True:
                    restart()
            else:
                    close()
                    
    #******************************************************   TOP    *******************************************************
    
    # -----------------LABEL-----------------------
    
    my = Label(root,text = "INPUT YOUR GUESS " , bg='#8D9EFF',relief="solid",font=('Arial 17'),height=1)
    my.pack()
    my.place(x=340,y=60)
    
    #---------------- ENTRY FIELD FOR WORD ------------

    ent=Entry(root,width=13,font='Noto 24',relief='sunken')
    ent.pack()
    ent.place(x=340,y=120)


    #--------------- NEW WORD ---------------------------
    def restart():
        global run
        run = True
        root.destroy()

    but = Button(root,text="New Word",width=20,border=2,font=('Monospace 15'),bg='#B3FFAE', relief="raised",command=restart)
    but.pack()
    but.place(x=345,y=185)



    #************************************************ LEFT & RIGHT ****************************************************

    #--------------- WORD IMAGES ----------------

    img = ImageTk.PhotoImage(Image.open(myli[p]))
    frame1 = Frame(root,width=200,height=200,bg="#8D72E1",highlightbackground="black", highlightthickness=3)
    frame1.pack()
    mylab = Label(frame1,image=img)
    mylab.grid(row=0,column=0)
    frame1.place(x=50,y=50)


    #-------------- HANGMAN IMAGE ---------------------


    frame2 = Frame(root,width=100,height=150,bg='#8D72E1')
    img2 = ImageTk.PhotoImage(Image.open("GAME.png"))
    mylab2 = Label(frame2,image=img2)
    mylab2.pack()
    frame2.pack()
    frame2.place(x=650,y=50)



    #*****************************************************   DOWN    *************************************************

    #----------------- EXIT BUTTON
    def close():
        global run
        run = False
        root.destroy()
        
    helv36 = tkFont.Font(family='Helvetica', size=13, weight='bold')
    button_exit = Button(root,text="Exit",padx=5,bg='#F75130',font =helv36,width=15,command=close)
    button_exit.pack()
    button_exit.place(x=650,y=520)
    
    hung = Label(root,text='PRESS EXIT TO CLOSE THE GAME',bg='#8D72E1',font=('Montserrat','13','bold'),relief="ridge")
    hung.pack()
    hung.place(x=595,y=565)

    #-------------NO OF GUESS LABEL AND TEXT FIELD
    frame3 = Frame(root,width=100,height=30)
    lab = Label(frame3,text="No of guess Remaining: ",borderwidth=2,bg='#8D72E1', font=('Open Sans','15'))
    enty = Entry(frame3,width=3,bd=2,font=20)
    you='  '+str(count)
    enty.insert(0,you)
    lab.grid(row=1,column=0)
    enty.grid(row=1,column=1)

    #lab.place(x=50,y=500)
    frame3.place(x=50,y=520)

    #checkbox 
    #totalentry


    #------------------------- MAINLOOP ---------------------
    root.mainloop()
