from tkinter import *
import requests
from bs4 import BeautifulSoup

def parser():
    page = requests.get('https://lenta.ru/news/2018/05/30/zhiv/')
    soup = BeautifulSoup(page.text, 'html.parser')
    title = soup.title.string
    text1 = soup.find_all('meta', property="description")
    print(text1)
    return text1

def Hello():
    x=parser()
    text1 = Text(main_window)
    text1.pack()
    text1.insert(3.0, x)

main_window = Tk()
main_window.title('Парсер lenta.ru')

name = StringVar()


name_label = Label(text="Введите url:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1, padx=5, pady=5)

url = Label(text="Введите url:")
print(name_entry.get())

message_button = Button(text="Click Me", command=Hello)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")

main_window.mainloop()