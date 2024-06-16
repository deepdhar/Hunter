from tkinter import *
from tkinter import messagebox
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import random
from bs4 import BeautifulSoup
from fpdf import FPDF
from appwrite.client import Client
from appwrite.services.users import Users

# appwrite authentication work (not completed)
client = Client()
(client
    .set_project('PROJECT_ID')
    .set_endpoint('API_END_POINT')
    .set_key('API_KEY')
    .set_self_signed()
)
# appwrite till here


root = Tk()
root.configure(bg='#660dff')
root.title("Hunter")
root.geometry("640x400")

bodyIndex=1
subIndex=1
nameIndex=1
senderEmail=''

def Home():
    global NewRoot
    root.withdraw() # hide (close) the root/Tk window
    NewRoot = Toplevel(root)
    NewRoot.title("Hunter")
    NewRoot.geometry("1200x640")
    # use the NewRoot as the root now
    

    limitCount = 20000
    totalFromSender = 1
    mailingTo = "test@gmail.com"
    renewal_date = "2024-07-02"


    def getSubject():
        path = "subjects.xlsx"
        workbook = load_workbook(path)
        worksheet = workbook.active
        length = len(list(worksheet.values))
        global subIndex
        if(subIndex==length+1):
            subIndex=1
        subjectInput.delete(0,END)
        new_subject = worksheet["A"+str(subIndex)].value
        subjectInput.insert(0,new_subject)
        subIndex = subIndex+1
        
    def getSenderName():
        path = "names.xlsx"
        workbook = load_workbook(path)
        worksheet = workbook.active
        length = len(list(worksheet.values))
        global nameIndex
        if(nameIndex==length+1):
            nameIndex=1
        senderNameInput.delete(0,END)
        new_name = worksheet["A"+str(nameIndex)].value
        senderNameInput.insert(0,new_name)
        nameIndex = nameIndex+1

    def loadSenders():
        path = "senders.xlsx"
        workbook = load_workbook(path)
        worksheet = workbook.active
        senderEmailInput.delete(0,END)
        
        length = len(list(worksheet.values))
        for i in range(1, length+1):
            # print(worksheet["B"+str(i)].value)
            buttons = [senderEmailButton1, senderEmailButton2, senderEmailButton3, senderEmailButton4, senderEmailButton5, senderEmailButton6, senderEmailButton7, senderEmailButton8, senderEmailButton9, senderEmailButton10, senderEmailButton11, senderEmailButton12, senderEmailButton13, senderEmailButton14, senderEmailButton15]
            buttons[i-1].configure(text=worksheet["B"+str(i)].value, background='#b1e6fc')

    def senderButtonPressed(button):
        global senderEmail
        buttonText = button.cget('text')
        if "Not Updated" in buttonText:
            return
        else:
            senderEmail = buttonText
            senderEmailInput.delete(0,END)
            senderEmailInput.insert(0,senderEmail)


    def loadBody():
        path = "bodys.xlsx"
        workbook = load_workbook(path)
        worksheet = workbook.active
        length = len(list(worksheet.values))
        global bodyIndex
        if(bodyIndex==length+1):
            bodyIndex=1
        bodyInput.delete('1.0', END)
        new_body = worksheet["A"+str(bodyIndex)].value
        bodyInput.insert('1.0', new_body)
        bodyIndex = bodyIndex+1
        senderEmailCount1.delete(0,END)
        senderEmailCount1.insert(0,'1')
        

    def startSendingEmail():
        if senderEmailInput.get()=='' or subjectInput.get()=='' or senderNameInput.get()=='' or bodyInput.get('1.0',END)=='' or htmlInput.get('1.0',END)=='':
            print('check empty values')
        else:
            sub = subjectInput.get()
            if "$RANDOM$" in sub:
                randint = str(random.randint(234567214, 9933553743))
                new_sub = sub.replace("$RANDOM$", randint)
                subjectInput.delete(0,END)
                subjectInput.insert(0,new_sub)
            
            body = bodyInput.get('1.0', END)
            if "$RANDOM$" in body:
                randint = str(random.randint(234567214, 9933553743))
                new_body = body.replace("$RANDOM$", randint)
                bodyInput.delete('1.0',END)
                bodyInput.insert('1.0',new_body)
                
            html = htmlInput.get('1.0',END);
            soup = BeautifulSoup(html)
            saveToPDF(soup.get_text())
            print(soup.get_text())
                
    def saveToPDF(htmlText):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=11)
        pdf.cell(200, 10, txt=htmlText, ln=1, align='C')
            
        
        randint = str(random.randint(234567214, 9933553743))
        filename = randint  + ".pdf"
        pdf.output("PDF/" + filename)


    # first column section
    getSubjectButton = Button(NewRoot, text="Get Subject", padx=20, pady=0, background="#b1e6fc", font=('Arial 10'), anchor='center', command=getSubject)
    getSubjectButton.grid(row=0, column=0, columnspan=2, ipady=4)

    subjectInput = Entry(NewRoot, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    subjectInput.grid(row=1, column=0, columnspan=2, padx=15, pady=10, ipady=4)


    # second column section
    senderEmaillabel = Label(NewRoot, text="Sender Email: ", font=('Arial, 11'), anchor="w",)
    senderEmaillabel.grid(row=0, column=2, columnspan=2,)

    senderEmailInput = Entry(NewRoot, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailInput.grid(row=1, column=2, columnspan=2, padx=15, pady=10, ipady=4, ipadx=5)
    senderEmailCountInput = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCountInput.grid(row=1, column=4, ipady=4)


    # third column section
    senderNameInput = Entry(NewRoot, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderNameInput.grid(row=1, column=5, columnspan=2, padx=15, pady=10, ipady=4)

    # autoSenderNameButton = Button(NewRoot, text='Auto Load Name', background='#ff4255', anchor='w')
    # autoSenderNameButton.grid(row=0, column=5)

    getSenderNameButton = Button(NewRoot, text='Get Sender Name', background='#b1e6fc', anchor='e', command=getSenderName)
    getSenderNameButton.grid(row=0, column=6, padx=(0,15))


    # third row (row=2)
    loadSendersButton = Button(NewRoot, text='Load Senders', background='#b1e6fc', command=loadSenders)
    loadSendersButton.grid(row=2, column=0, pady=15)

    chooseJsonFolderButton = Button(NewRoot, text='Choose JSON Folder', background='#b1e6fc')
    chooseJsonFolderButton.grid(row=2, column=1, pady=15, padx=(0,15))


    mailToLabel = Label(NewRoot, text="Mail to " + str(mailingTo) + ". Total from sender: " + str(totalFromSender), font=('Arial, 11'), anchor="w")
    mailToLabel.grid(row=2, column=2, columnspan=2)

    remainingLimitLabel = Label(NewRoot, text="Remaining Limit: " + str(limitCount), font=('Arial, 11'), anchor="w")
    remainingLimitLabel.grid(row=2, column=5, columnspan=1)


    # fourth row (row=3)
    # first column buttons
    senderEmailButton1 = Button(NewRoot, text="1. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton1))
    senderEmailButton1.grid(row=3, column=0, padx=(5,0))
    senderEmailCount1 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount1.grid(row=3, column=1)

    senderEmailButton2 = Button(NewRoot, text="2. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton2))
    senderEmailButton2.grid(row=4, column=0, padx=(5,0))
    senderEmailCount2 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount2.grid(row=4, column=1)

    senderEmailButton3 = Button(NewRoot, text="3. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton3))
    senderEmailButton3.grid(row=5, column=0, padx=(5,0))
    senderEmailCount3 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount3.grid(row=5, column=1)

    senderEmailButton4 = Button(NewRoot, text="4. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton4))
    senderEmailButton4.grid(row=6, column=0, padx=(5,0))
    senderEmailCount4 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount4.grid(row=6, column=1)

    senderEmailButton5 = Button(NewRoot, text="5. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton5))
    senderEmailButton5.grid(row=7, column=0, padx=(5,0))
    senderEmailCount5 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount5.grid(row=7, column=1)

    # third column buttons
    senderEmailButton6 = Button(NewRoot, text="6. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton6))
    senderEmailButton6.grid(row=3, column=2, padx=(5,0))
    senderEmailCount6 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount6.grid(row=3, column=3)

    senderEmailButton7 = Button(NewRoot, text="7. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton7))
    senderEmailButton7.grid(row=4, column=2, padx=(5,0))
    senderEmailCount7 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount7.grid(row=4, column=3)

    senderEmailButton8 = Button(NewRoot, text="8. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton8))
    senderEmailButton8.grid(row=5, column=2, padx=(5,0))
    senderEmailCount8 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount8.grid(row=5, column=3)

    senderEmailButton9 = Button(NewRoot, text="9. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton9))
    senderEmailButton9.grid(row=6, column=2, padx=(5,0))
    senderEmailCount9 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount9.grid(row=6, column=3)

    senderEmailButton10 = Button(NewRoot, text="10. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton10))
    senderEmailButton10.grid(row=7, column=2, padx=(5,0))
    senderEmailCount10 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount10.grid(row=7, column=3)

    # fifth column buttons
    senderEmailButton11 = Button(NewRoot, text="11. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton11))
    senderEmailButton11.grid(row=3, column=5, padx=(5,0))
    senderEmailCount11 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount11.grid(row=3, column=6)

    senderEmailButton12 = Button(NewRoot, text="12. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton12))
    senderEmailButton12.grid(row=4, column=5, padx=(5,0))
    senderEmailCount12 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount12.grid(row=4, column=6)

    senderEmailButton13 = Button(NewRoot, text="13. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton13))
    senderEmailButton13.grid(row=5, column=5, padx=(5,0))
    senderEmailCount13 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount13.grid(row=5, column=6)

    senderEmailButton14 = Button(NewRoot, text="14. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton14))
    senderEmailButton14.grid(row=6, column=5, padx=(5,0))
    senderEmailCount14 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount14.grid(row=6, column=6)

    senderEmailButton15 = Button(NewRoot, text="15. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton15))
    senderEmailButton15.grid(row=7, column=5, padx=(5,0))
    senderEmailCount15 = Entry(NewRoot, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
    senderEmailCount15.grid(row=7, column=6)


    # seventh row (row=8)
    tagsTextBox = Text(NewRoot, width=45, borderwidth=5, height=3, background='#90f5e6')
    tagsTextBox.grid(row=8, column=2, columnspan=3, pady=(20,10))
    tagsTextBox.insert('1.0', "Tags:- $INVOICE$, $TRANSACTION$, $DATE$, \n $EMAIL$, $ITEMNO$, $RANDOM$")
    tagsTextBox.config(state=DISABLED)

    remainingLimitLabel = Label(NewRoot, text="next renewal date: " + str(renewal_date), font=('Arial, 11'), anchor="w")
    remainingLimitLabel.grid(row=8, column=5, columnspan=1, pady=20)

    startButton = Button(NewRoot, text="Start", background='#15d629', width=10, font=('Arial, 11'), command=startSendingEmail)
    startButton.grid(row=8, column=6, pady=20)


    # eigth row (row=9)
    htmlLabel = Label(NewRoot, text="Paste Html for PDF:", font=('Arial, 10'), anchor='center')
    htmlLabel.grid(row=9, column=0, columnspan=2, pady=10)
    htmlInput = Text(NewRoot, width=42, height=12, background='#90f5e6')
    htmlInput.grid(row=10, column=0, columnspan=2)

    loadBodyButton = Button(NewRoot, text='Load Body', background="#b1e6fc", font=('Arial 10'), anchor='center', command=loadBody)
    loadBodyButton.grid(row=9, column=2, columnspan=3)
    bodyInput = Text(NewRoot, width=45, height=12, background='#90f5e6')
    bodyInput.grid(row=10, column=2, columnspan=3)

    
    

def login():
    username = "user"
    password = "123"
    
    if username_entry.get()==username and password_entry.get()==password:
        root.after(1000, Home) # or whatever your Tk is called
        # redirect to the NewPage function after 1 seconds 
    else:
        messagebox.showerror(title='Error', message="Invalid login.")
    

    
frame = Frame(bg='#660dff')

login_label = Label(frame, text="Hunter", bg='#660dff', fg="#FFFFFF", font=("Arial", 30))
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

username_label = Label(frame, text="Username", bg='#660dff', fg="#FFFFFF", font=("Arial", 16, 'bold'))
username_label.grid(row=1, column=0, padx=(0,20))

password_label = Label(frame, text="Password", bg='#660dff', fg="#FFFFFF", font=("Arial", 16, 'bold'))
password_label.grid(row=2, column=0, padx=(0,20))

username_entry = Entry(frame, font=("Arial", 16))
username_entry.grid(row=1, column=1, pady=20)

password_entry = Entry(frame, show="*", font=("Arial", 16))
password_entry.grid(row=2, column=1, pady=20)

login_button = Button(frame, text="Sign In", bg="#DC143C", fg="#FFFFFF", padx=20, pady=1, font=("Arial", 16), command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=20)



frame.pack()
root.mainloop()



# def Is_Valid():
#     # same as before...
#     if LogInAttempt:
#         print (" One of the accounts have successfully logged in ")
#         IsValidText.config(text=" You have logged in! ", fg="black", highlightthickness=1)
#         root.after(1000, NewPage) # or whatever your Tk is called
#         # redirect to the NewPage function after 1 seconds 
#     else:
#         print (" One of the accounts inputted the wrong credentials! ")
#         IsValidText.config(text=" Invalid username or Password! ", fg="black", highlightthickness=1)
        