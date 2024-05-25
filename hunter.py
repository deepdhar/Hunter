from tkinter import *

root = Tk()
root.title("Hunter")
root.geometry("1200x620")
limitCount = 20000


subject = Entry(root, width=95, borderwidth=5, font=('Arial 12'))
subject.grid(row=0, column=0, columnspan=4, padx=15, pady=10, ipady=6)

sendEmailButton = Button(root, text="Send Email", padx=60, pady=5, background="#fc4765", font=('Arial 12'))
sendEmailButton.grid(row=0, column=5, ipady=0, padx=30)

label = Label(root, text="Receiver's list: ", font=('Arial, 13'), anchor="w", width=20)
label.grid(row=1, column=0, padx=2, pady=(30,0))

limit = Label(root, text="Today's limit: "+str(limitCount), font=('Arial, 13'), anchor="w", width=20, fg='red')
limit.grid(row=1, column=2, padx=2, pady=(0,0))

button1 = Button(root, text="", width=25, background="#79f795")
button2 = Button(root, text="", width=25, background="#79f795")
button3 = Button(root, text="", width=25, background="#79f795")
button4 = Button(root, text="", width=25, background="#79f795")
button5 = Button(root, text="", width=25, background="#79f795")
button6 = Button(root, text="", width=25, background="#79f795")
button7 = Button(root, text="", width=25, background="#79f795")
button8 = Button(root, text="", width=25, background="#79f795")
button9 = Button(root, text="", width=25, background="#79f795")
button10 = Button(root, text="", width=25, background="#79f795")
button11 = Button(root, text="", width=25, background="#79f795")
button12 = Button(root, text="", width=25, background="#79f795")

button1.grid(row=2, column=0, pady=10, ipady=5)
button2.grid(row=2, column=1, pady=10, ipady=5)
button3.grid(row=2, column=2, pady=10, ipady=5)
button4.grid(row=2, column=3, pady=10, ipady=5)
button5.grid(row=3, column=0, pady=10, ipady=5)
button6.grid(row=3, column=1, pady=10, ipady=5)
button7.grid(row=3, column=2, pady=10, ipady=5)
button8.grid(row=3, column=3, pady=10, ipady=5)
button9.grid(row=4, column=0, pady=10, ipady=5)
button10.grid(row=4, column=1, pady=10, ipady=5)
button11.grid(row=4, column=2, pady=10, ipady=5)
button12.grid(row=4, column=3, pady=10, ipady=5)


pdfLabel = Label(root, text="Paste HTML below for PDF conversion", font=('Arial, 13'), anchor='w', width=45).grid(row=5, column=0, padx=2, columnspan=2, pady=(20,0))
htmlToPdf = Text(root, width=105, borderwidth=5, height=15,)
htmlToPdf.grid(row=6, column=0, columnspan=4, rowspan=5, padx=15, pady=(5,15))

selectedSender = ""

def senderButtonClick(buttonNo, email):
    senderButton1.configure(bg="#5799fa")
    senderButton2.configure(bg="#5799fa")
    senderButton3.configure(bg="#5799fa")
    senderButton4.configure(bg="#5799fa")
    senderButton5.configure(bg="#5799fa")
    selectedSender = email
    if(buttonNo=="button1"):
        senderButton1.configure(bg="#1a60c9")
    elif(buttonNo=="button2"):
        senderButton2.configure(bg="#1a60c9")
    elif(buttonNo=="button3"):
        senderButton3.configure(bg="#1a60c9")
    elif(buttonNo=="button4"):
        senderButton4.configure(bg="#1a60c9")
    elif(buttonNo=="button5"):
        senderButton5.configure(bg="#1a60c9")
    print(selectedSender)

senderButton1Text = "test@outlook.com"
senderButton2Text = "sender@hotchat.com"
senderButton3Text = "deep@travels.com"
senderButton4Text = "subham@mia.com"
senderButton5Text = "trevor69@hotmail.com"

senderButton1 = Button(root, text=senderButton1Text, width=25, bg="#5799fa", pady=8, command=lambda: senderButtonClick("button1", senderButton1Text))
senderButton1.grid(row=2, column=5)
senderButton2 = Button(root, text=senderButton2Text, width=25, background="#5799fa", pady=8, command=lambda: senderButtonClick("button2", senderButton2Text))
senderButton2.grid(row=3, column=5)
senderButton3 = Button(root, text=senderButton3Text, width=25, background="#5799fa", pady=8, command=lambda: senderButtonClick("button3", senderButton3Text))
senderButton3.grid(row=4, column=5)
senderButton4 = Button(root, text=senderButton4Text, width=25, background="#5799fa", pady=8, command=lambda: senderButtonClick("button4", senderButton4Text))
senderButton4.grid(row=5, column=5)
senderButton5 = Button(root, text=senderButton5Text, width=25, background="#5799fa", pady=8, command=lambda: senderButtonClick("button5", senderButton5Text))
senderButton5.grid(row=6, column=5)

senderButton6 = Button(root, text="Load More...", width=25, background="#1e6ee6", pady=8).grid(row=7, column=5)
uploadSenderButton = Button(root, text="Upload", width=25, background="#f2d552", pady=8).grid(row=9, column=5)

root.mainloop()

