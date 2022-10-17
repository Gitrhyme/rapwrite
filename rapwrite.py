#Imports
import requests
import json
from tkinter import *
from tkinter import ttk

#Working On RapWrite
root = Tk()
root.call('source', 'forest-dark.tcl')
ttk.Style().theme_use('forest-dark')
root.title('RapWrite')
root.geometry('850x500')
#root.maxsize(850, 500)

#Main Frame
mainFrame = ttk.Frame(root)
mainFrame.pack(pady=5)

bottomFrame = ttk.Frame(root)
bottomFrame.pack(side='top', pady=5)

# Listbox
rhyme_Listbox = Listbox(mainFrame)
rhyme_Listbox.pack(side='left')

nRhyme_Listbox = Listbox(mainFrame)
nRhyme_Listbox.pack(side='left')

followUp_Listbox = Listbox(mainFrame)
followUp_Listbox.pack(side='left')

#Entry Box
string = Entry(bottomFrame, width=20, font=('Arial 14'))
string.pack()

#Scroll Bar
padScroll = Scrollbar(mainFrame)
padScroll.pack(side='right', fill='y')

#Text Box
versePad = Text(mainFrame, width=40, height=20, font=('Arial', 12), selectbackground='yellow', selectforeground='black', undo=True, yscrollcommand=padScroll.set)
versePad.pack()

padScroll.config(command=versePad.yview)

##API Request
def apiRequest(words):
  #API Request Section
    rhymeRequest = requests.get(f'http://api.datamuse.com/words?rel_rhy={words[-1]}').text

    rhymeRequest_info = json.loads(rhymeRequest)

    nryRequest = requests.get(f'http://api.datamuse.com/words?rel_nry={words[-1]}').text

    nryRequest_info = json.loads(nryRequest)

    bgaRequest = requests.get(f'http://api.datamuse.com/words?rel_bga={words[-1]}').text

    bgaRequest_info = json.loads(bgaRequest)
    return rhymeRequest_info, nryRequest_info, bgaRequest_info

 #Main Functions
def rhymeList(rhymeRequest_info):
  wordRhymes = []
  length = len(rhymeRequest_info)
  if length == 0:
    wordRhymes.append('No Rhymes...')
  else:
    for i in range(length):
      if rhymeRequest_info[i]['score'] >= 1:

        result = rhymeRequest_info[i]['word']
        wordRhymes.append(result)
  return wordRhymes

def nRhyme(nryRequest_info):
  nRhymes = []
  length = len(nryRequest_info)
  if length == 0:
    nRhymes.append('No Near Rhymes...')
  else:
    for i in range(length):
      if nryRequest_info[i]['score'] >= 1:

        result = nryRequest_info[i]['word']
        nRhymes.append(result)
  return nRhymes

def followUp(bgaRequest_info):
  bgaStarters = []
  length = len(bgaRequest_info)
  if length == 0:
    bgaStarters.append('No Follow Up...')
  else:
    for i in range(length):
      if bgaRequest_info[i]['score'] >= 1:

        result = bgaRequest_info[i]['word']
        bgaStarters.append(result)
  return bgaStarters

def listFill(rhyList, nryList, followUpList):
    for item in rhyList:
      rhyme_Listbox.insert(END, item)

    for item in nryList:
      nRhyme_Listbox.insert(END, item)

    for item in followUpList:
      followUp_Listbox.insert(END, item)

def delete():
  rhyme_Listbox.delete(0, END)
  nRhyme_Listbox.delete(0, END)
  followUp_Listbox.delete(0, END)

def button_command():
  text = string.get()
  words = text.split()

  rhymeRequest_info, nryRequest_info, bgaRequest_info = apiRequest(words)
    
  rhyList = rhymeList(rhymeRequest_info)
  nryList = nRhyme(nryRequest_info)
  bgaList = followUp(bgaRequest_info)

  delete()
  listFill(rhyList, nryList, bgaList)

  return None

unblock = ttk.Button(bottomFrame, text="Unblock", command=button_command)
unblock.pack()

mainFrame.mainloop()
