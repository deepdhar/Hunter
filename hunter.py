from tkinter import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import random
from bs4 import BeautifulSoup
from fpdf import FPDF

root = Tk()
root.title("Hunter")
root.geometry("1200x640")
limitCount = 20000
totalFromSender = 1
mailingTo = "test@gmail.com"
renewal_date = "2024-06-03"
subjects = [
    "Order ID confirmation"
]
body = [
    "Hello how are you. Thanks for your order ID $7676945",
    "Hey Greetings. Here's your order ID $7676945",
    "Good Morning Sir. We will get your order deliver soon. Order Ref ID $7676945",
]
bodyIndex=1
subIndex=1
nameIndex=1
senderEmail=''

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
getSubjectButton = Button(root, text="Get Subject", padx=20, pady=0, background="#b1e6fc", font=('Arial 10'), anchor='center', command=getSubject)
getSubjectButton.grid(row=0, column=0, columnspan=2, ipady=4)

subjectInput = Entry(root, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
subjectInput.grid(row=1, column=0, columnspan=2, padx=15, pady=10, ipady=4)


# second column section
senderEmaillabel = Label(root, text="Sender Email: ", font=('Arial, 11'), anchor="w",)
senderEmaillabel.grid(row=0, column=2, columnspan=2,)

senderEmailInput = Entry(root, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailInput.grid(row=1, column=2, columnspan=2, padx=15, pady=10, ipady=4, ipadx=5)
senderEmailCountInput = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCountInput.grid(row=1, column=4, ipady=4)


# third column section
senderNameInput = Entry(root, width=48, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderNameInput.grid(row=1, column=5, columnspan=2, padx=15, pady=10, ipady=4)

# autoSenderNameButton = Button(root, text='Auto Load Name', background='#ff4255', anchor='w')
# autoSenderNameButton.grid(row=0, column=5)

getSenderNameButton = Button(root, text='Get Sender Name', background='#b1e6fc', anchor='e', command=getSenderName)
getSenderNameButton.grid(row=0, column=6, padx=(0,15))


# third row (row=2)
loadSendersButton = Button(root, text='Load Senders', background='#b1e6fc', command=loadSenders)
loadSendersButton.grid(row=2, column=0, pady=15)

chooseJsonFolderButton = Button(root, text='Choose JSON Folder', background='#b1e6fc')
chooseJsonFolderButton.grid(row=2, column=1, pady=15, padx=(0,15))


mailToLabel = Label(root, text="Mail to " + str(mailingTo) + ". Total from sender: " + str(totalFromSender), font=('Arial, 11'), anchor="w")
mailToLabel.grid(row=2, column=2, columnspan=2)

remainingLimitLabel = Label(root, text="Remaining Limit: " + str(limitCount), font=('Arial, 11'), anchor="w")
remainingLimitLabel.grid(row=2, column=5, columnspan=1)


# fourth row (row=3)
# first column buttons
senderEmailButton1 = Button(root, text="1. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton1))
senderEmailButton1.grid(row=3, column=0, padx=(5,0))
senderEmailCount1 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount1.grid(row=3, column=1)

senderEmailButton2 = Button(root, text="2. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton2))
senderEmailButton2.grid(row=4, column=0, padx=(5,0))
senderEmailCount2 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount2.grid(row=4, column=1)

senderEmailButton3 = Button(root, text="3. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton3))
senderEmailButton3.grid(row=5, column=0, padx=(5,0))
senderEmailCount3 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount3.grid(row=5, column=1)

senderEmailButton4 = Button(root, text="4. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton4))
senderEmailButton4.grid(row=6, column=0, padx=(5,0))
senderEmailCount4 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount4.grid(row=6, column=1)

senderEmailButton5 = Button(root, text="5. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton5))
senderEmailButton5.grid(row=7, column=0, padx=(5,0))
senderEmailCount5 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount5.grid(row=7, column=1)

# third column buttons
senderEmailButton6 = Button(root, text="6. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton6))
senderEmailButton6.grid(row=3, column=2, padx=(5,0))
senderEmailCount6 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount6.grid(row=3, column=3)

senderEmailButton7 = Button(root, text="7. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton7))
senderEmailButton7.grid(row=4, column=2, padx=(5,0))
senderEmailCount7 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount7.grid(row=4, column=3)

senderEmailButton8 = Button(root, text="8. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton8))
senderEmailButton8.grid(row=5, column=2, padx=(5,0))
senderEmailCount8 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount8.grid(row=5, column=3)

senderEmailButton9 = Button(root, text="9. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton9))
senderEmailButton9.grid(row=6, column=2, padx=(5,0))
senderEmailCount9 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount9.grid(row=6, column=3)

senderEmailButton10 = Button(root, text="10. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton10))
senderEmailButton10.grid(row=7, column=2, padx=(5,0))
senderEmailCount10 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount10.grid(row=7, column=3)

# fifth column buttons
senderEmailButton11 = Button(root, text="11. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton11))
senderEmailButton11.grid(row=3, column=5, padx=(5,0))
senderEmailCount11 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount11.grid(row=3, column=6)

senderEmailButton12 = Button(root, text="12. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton12))
senderEmailButton12.grid(row=4, column=5, padx=(5,0))
senderEmailCount12 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount12.grid(row=4, column=6)

senderEmailButton13 = Button(root, text="13. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton13))
senderEmailButton13.grid(row=5, column=5, padx=(5,0))
senderEmailCount13 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount13.grid(row=5, column=6)

senderEmailButton14 = Button(root, text="14. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton14))
senderEmailButton14.grid(row=6, column=5, padx=(5,0))
senderEmailCount14 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount14.grid(row=6, column=6)

senderEmailButton15 = Button(root, text="15. Not Updated", background='#bf82ed', width=30, anchor='w', padx=5, command=lambda: senderButtonPressed(senderEmailButton15))
senderEmailButton15.grid(row=7, column=5, padx=(5,0))
senderEmailCount15 = Entry(root, width=4, borderwidth=5, font=('Arial 10'), background="#90f5e6")
senderEmailCount15.grid(row=7, column=6)


# seventh row (row=8)
tagsTextBox = Text(root, width=45, borderwidth=5, height=3, background='#90f5e6')
tagsTextBox.grid(row=8, column=2, columnspan=3, pady=(20,10))
tagsTextBox.insert('1.0', "Tags:- $INVOICE$, $TRANSACTION$, $DATE$, \n $EMAIL$, $ITEMNO$, $RANDOM$")
tagsTextBox.config(state=DISABLED)

renewalDateLabel = Label(root, text="next renewal date: " + str(renewal_date), font=('Arial, 11'), anchor="w")
remainingLimitLabel.grid(row=8, column=5, columnspan=1, pady=20)

startButton = Button(root, text="Start", background='#15d629', width=10, font=('Arial, 11'), command=startSendingEmail)
startButton.grid(row=8, column=6, pady=20)


# eigth row (row=9)
htmlLabel = Label(root, text="Paste Html for PDF:", font=('Arial, 10'), anchor='center')
htmlLabel.grid(row=9, column=0, columnspan=2, pady=10)
htmlInput = Text(root, width=42, height=12, background='#90f5e6')
htmlInput.grid(row=10, column=0, columnspan=2)

loadBodyButton = Button(root, text='Load Body', background="#b1e6fc", font=('Arial 10'), anchor='center', command=loadBody)
loadBodyButton.grid(row=9, column=2, columnspan=3)
bodyInput = Text(root, width=45, height=12, background='#90f5e6')
bodyInput.grid(row=10, column=2, columnspan=3)

root.mainloop()