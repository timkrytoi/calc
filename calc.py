import tkinter as tk


root = tk.Tk()
root.title('Калькулятор')
root.geometry('500x550')
root.resizable(False,False)
root['bg'] = 'black'


def calculate(operation):
    global formula


    if operation == 'C':
        formula = ''
    elif operation == 'del':
        formula = formula[0:-1]
    elif operation == 'x^2':
        formula = str((eval(formula))**2)
    elif operation == '=':
        formula  = str(eval(formula))
    else:
        if formula == '0':
            formula = ''
        formula += operation
    label_text.configure(text=formula)

#Создание кнопки для вывода вычеслений
formula = '0'
label_text = tk.Label(text=formula,font='Arial 20 bold',bg='black',fg='white')
label_text.place(x=11,y=50)

#СОЗДАЕМ КНОПКИ
buttons = ['C','del','*','=','1','2','3','/','4','5','6','+','7','8','9','-','+/-','0','%','x^2']
x =  18
y = 140
for  button in buttons:
    get_lbl = lambda x = button: calculate(x)
    tk.Button(text=button,bg='orange',font='Arial 13 bold',command=get_lbl).place(x=x,y=y,width=115,height=79)
    x += 117
    if x>400:
        x = 18
        y += 81



root.mainloop()