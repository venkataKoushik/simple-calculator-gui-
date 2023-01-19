import tkinter as t
equation=''
def add(character):
    global equation 
    equation+=(character)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, equation)


def calculation():
    try:
        global equation 
        result=str(eval(equation))
        equation=""
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, result)
    except Exception :
        text_result.insert(1.0, "Syntax Error")
        

def clear():
    global equation 
    equation=""
    text_result.delete(1.0, 'end')
    
slide=t.Tk()
slide.geometry("500x720")
slide.title("Calculator")
slide.configure(bg='#222222')
title_label=t.Label(slide,text="Calculator",bg='#222222' , fg="cyan", font=("Arial", 35))
title_label.grid(columnspan=5, sticky="news",pady=5)

text_result=t.Text(slide,height=3,width=30,font=("Arial", 20))
text_result.grid(columnspan=5,padx=23,pady=5)

button_1=t.Button(slide,text="c",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:clear())

button_1.grid(row=2,column=1,pady=5)
button_1=t.Button(slide,text="(",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('('))
button_1.grid(row=2,column=2,pady=5)
button_1=t.Button(slide,text=")",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add(')'))
button_1.grid(row=2,column=3,pady=5)
button_1=t.Button(slide,text="/",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('/'))
button_1.grid(row=2,column=4,pady=5)


button_1=t.Button(slide,text="7",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('7'))
button_1.grid(row=3,column=1,pady=5)
button_1=t.Button(slide,text="8",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('8'))
button_1.grid(row=3,column=2,pady=5)
button_1=t.Button(slide,text="9",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('9'))
button_1.grid(row=3,column=3,pady=5)
button_1=t.Button(slide,text="x",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('*'))
button_1.grid(row=3,column=4,pady=5)


button_1=t.Button(slide,text="4",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('4'))
button_1.grid(row=4,column=1,pady=5)
button_1=t.Button(slide,text="5",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('5'))
button_1.grid(row=4,column=2,pady=5)
button_1=t.Button(slide,text="6",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('6'))
button_1.grid(row=4,column=3,pady=5)
button_1=t.Button(slide,text="-",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('-'))
button_1.grid(row=4,column=4,pady=5)


button_1=t.Button(slide,text="1",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('1'))
button_1.grid(row=5,column=1,pady=5)
button_1=t.Button(slide,text="2",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('2'))
button_1.grid(row=5,column=2,pady=5)
button_1=t.Button(slide,text="3",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('3'))
button_1.grid(row=5,column=3,pady=5)
button_1=t.Button(slide,text="+",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('+'))
button_1.grid(row=5,column=4,pady=5)



button_1=t.Button(slide,text="00",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('00'))
button_1.grid(row=6,column=1,pady=5)
button_1=t.Button(slide,text="0",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('0'))
button_1.grid(row=6,column=2,pady=5)
button_1=t.Button(slide,text=".",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:add('.'))
button_1.grid(row=6,column=3,pady=5)
button_1=t.Button(slide,text="=",font=("Arial", 15, "bold" ),bg='deeppink',fg='black',height=3,width=8,command=lambda:calculation())
button_1.grid(row=6,column=4,pady=5)


slide.mainloop()

