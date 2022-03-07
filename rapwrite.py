#Imports
import requests
import json
from tkinter import *

#Working On RapWrite
root = Tk()
root.title('RapWrite')
root.geometry('400x400')

# Listbox
rhyme_Listbox = Listbox(root)
rhyme_Listbox.pack(pady=15)

followUp_Listbox = Listbox(root)
followUp_Listbox.pack(pady=15)

##Input String That Gets Examined
def delete():
  rhyme_Listbox.delete(0, END)
  followUp_Listbox.delete(0, END)

def button_command():
  text = string.get()
  words = text.split()
  #API Request Section

  rhymeRequest = requests.get(f'http://api.datamuse.com/words?rel_rhy={words[-1]}').text

  rhymeRequest_info = json.loads(rhymeRequest)

  trgRequest = requests.get(f'http://api.datamuse.com/words?rel_trg={words[-1]}').text

  trgRequest_info = json.loads(trgRequest)

  bgaRequest = requests.get(f'http://api.datamuse.com/words?rel_bga={words[-1]}').text

  bgaRequest_info = json.loads(bgaRequest)

  #Main Functions
  def rhymeList():
    wordRhymes = []
    length = len(rhymeRequest_info)
    for i in range(length):
      if rhymeRequest_info[i]['score'] >= 1:

        result = rhymeRequest_info[i]['word']
        wordRhymes.append(result)
    return wordRhymes

  def followUp():
    bgaStarters = []
    length = len(bgaRequest_info)
    for i in range(length):
      if bgaRequest_info[i]['score'] >= 1:

        result = bgaRequest_info[i]['word']
        bgaStarters.append(result)
    return bgaStarters

  rhyList = rhymeList()
  bgaList = followUp()

  delete()

  for item in rhyList:
    rhyme_Listbox.insert(END, item)

  for item in bgaList:
    followUp_Listbox.insert(END, item)
  return None


string = Entry(root)
string.pack()

Button(root, text="Unblock", command=button_command).pack()

root.mainloop()
