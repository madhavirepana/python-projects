# CURRENCY CONVERTER WITH USING GUI APPLICATION
# -------------------------------------------------

from tkinter import Tk, ttk
from tkinter import *
from tkinter.messagebox import showerror
import requests
import json

#colors 
cor0 = "#FFFFFF"  # white
cor1 = "#333333"  # black
cor2 = "#EE82EE"  # red

# creating the main window
window = Tk()
# this gives the window the width(300), height(320)
window.geometry('300x320')
# this is the title for the window
window.title('Currency Converter/developed by Madhavi')

window.configure(bg=cor0)
# this will make the window not resizable, since height and width is FALSE
window.resizable(height = FALSE, width=FALSE)

#frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor0)
main.grid(row=1, column=0)
#Converting all currencies by using API currencies and used convert() to give connection
def convert():
    try:
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

        currency_1 = combo1.get()
        currency_2 = combo2.get()
        amount = value.get()

        querystring = {"from":currency_1,"to":currency_2,"amount":amount}

        if currency_2 == 'USD':
            symbol = '$'
        elif currency_2 == 'INR':
            symbol = '₹'                        
        elif currency_2 == 'EUR':
            symbol = '€'
        elif currency_2 == 'BRL':
            symbol = 'R$'
        elif currency_2 == 'CAD':
            symbol = 'CA $'
        elif currency_2 == 'JPY':
            symbol = '¥'
        elif currency_2 == 'GBP':
            symbol = '£'
        elif currency_2 == 'BTC':
            symbol = '₿'
        elif currency_2 == 'LTC':
            symbol = 'Ł'
        elif currency_2 == 'ETH':
            symbol = 'Ξ'
        elif currency_2 == 'XMR':
            symbol = 'ɱ'
        elif currency_2 == 'XRP':
            symbol = 'XRP'
        elif currency_2 == 'USDT':
            symbol = '₮'
        elif currency_2 == 'LKR':
            symbol = 'Rs'
        elif currency_2 == 'TWD':
            symbol = 'NT$'
        elif currency_2 == 'TJS':
            symbol = 'TJS'
        elif currency_2 == 'THB':
            symbol = '฿'
        elif currency_2 == 'TMT':
            symbol = 'm'
        elif currency_2 == 'UZS':
            symbol = 'som'
        elif currency_2 == 'NPR':
            symbol = 'Rs'
        elif currency_2 == 'NZD':
            symbol = '$'
        elif currency_2 == 'KPW':
            symbol = '₩'
        elif currency_2 == 'PKR':
            symbol = 'Rs'
        elif currency_2 == 'PHP':
            symbol = '₱'
        elif currency_2 == 'SGD':
            symbol = 'S$'
        elif currency_2 == 'KRW':
            symbol = '₩'
        elif currency_2 == 'KRW':
            symbol = 'Rs'
        elif currency_2 == 'LKR':
            symbol = 'NT$'
        elif currency_2 == 'TJS':
            symbol = 'TJS'
            

        headers = {
            'x-rapidapi-host': "currency-converter18.p.rapidapi.com",
            'x-rapidapi-key': "90c59d6c9fmsh4599f814e2ffc92p17fc6djsndeaa0265ac61"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)
        converted_amount = data["result"]["convertedAmount"]
        formatted = symbol + " {:,.2f}".format(converted_amount)

        result['text'] = formatted

        print(converted_amount, formatted)
    except:
        showerror(title='Error', message='Please enter integer or float value')

#top frame


app_name=Label(top,text="Currency Converter",height=2,padx=40,pady=5,anchor=CENTER,font=('Arial 16 bold'),bg=cor2,fg=cor0)
app_name.place(x=0,y=0)

#main frame
result = Label(main, text = " ",width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg="#0000FF")
result.place(x=50, y=10)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD','JPY','GBP','BTC','LTC','ETH','XMR','XRP','USDT','LKR','TWD','TJS','THB','TMT','UZS','NPR'
            'NZD','KPW','PKR','PHP','SGD','KRW','LKR','TJS']

from_label = Label(main, text = "From", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg="#ff0000")
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text = "To", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg="#ff0000")
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

amount_label=Label(main, text = "Amount", width=8, height=1, pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg="#ff0000")
amount_label.place(x=50,y=145)
value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=55, y=170)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg='#9ACD32', fg=cor0,font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=220)

# this runs the window infinitely until it is closed
window.mainloop()
