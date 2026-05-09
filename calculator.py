
import tkinter as tk

on_number = 0
now_number = 0
on_operator = 0 #　+を1、-を2で考える
pre_number = 0
pre_operator = 0
number = 0

def update_number(now_number,on_number): #入力数値を並べる関数
    now_number = now_number * 10 + on_number
    
    return now_number

def operator_input(on_operator,pre_operator,pre_number,now_number): #演算子の入力関数

    if pre_operator == 0:
        pre_operator = on_operator
        pre_number = now_number
        now_number = 0
    
    else:
        if pre_operator == 1:
            pre_number = now_number + pre_number
        elif pre_operator == 2:
            pre_number = pre_number - now_number 
        now_number = 0
        pre_operator = on_operator

    return(pre_operator,pre_number,now_number)

def exe_equal(pre_operator,pre_number,now_number): #イコール処理
    if pre_operator == 1:
        now_number = pre_number + now_number
    elif pre_operator == 2:
        now_number = pre_number - now_number

    pre_operator = 0
    pre_number = 0
    return(pre_operator,pre_number,now_number)  

def number_click(number): #数字のクリック関数
    global now_number
    global pre_operator
    global pre_number

    now_number = update_number(now_number,number)
    formula = build_display(pre_operator,pre_number,now_number)
    update_display(formula)

def operator_click(number):
    global pre_operator
    global pre_number
    global now_number

    pre_operator,pre_number,now_number = operator_input(number,pre_operator,pre_number,now_number)
    formula = build_display(pre_operator,pre_number,now_number)
    update_display(formula)



def build_display(pre_operator,pre_number,now_number): #式作成関数
    if pre_operator == 0:
        formula = str(now_number)
    elif pre_operator == 1 and now_number == 0:
        formula = str(pre_number) + "+"
    elif pre_operator == 2 and now_number == 0:
        formula = str(pre_number) + "-"
    elif pre_operator == 1 and now_number != 0:
        formula = str(pre_number) + "+" + str(now_number)
    elif pre_operator == 2 and now_number != 0:
        formula = str(pre_number) + "-" + str(now_number)

    return(formula)


def update_display(now_number): #Tkinterへの反映
    entry.config(state="normal")
    entry.delete(0,tk.END)
    entry.insert(0,str(now_number))
    entry.config(state="readonly")

#ビジュアル
root = tk.Tk()
root.title("電卓")
root.geometry("400x600")

icon = tk.PhotoImage(file="calculator_icon.png")
root.iconphoto(True,icon)

entry = tk.Entry(root,justify="right")
entry.config(state="normal")
entry.insert(0,"0")
entry.config(state="readonly")

btn_1 = tk.Button(root,text="1",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(1))
btn_2 = tk.Button(root,text="2",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(2))
btn_3 = tk.Button(root,text="3",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(3))
btn_4 = tk.Button(root,text="4",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(4))
btn_5 = tk.Button(root,text="5",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(5))
btn_6 = tk.Button(root,text="6",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(6))
btn_7 = tk.Button(root,text="7",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(7))
btn_8 = tk.Button(root,text="8",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(8))
btn_9 = tk.Button(root,text="9",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(9))
btn_0 = tk.Button(root,text="0",width="5",font=("Arial",30),activebackground="gray",command=lambda:number_click(0))
btn_plus = tk.Button(root,text="+",width="5",font=("Arial",30),activebackground="gray",command=lambda:operator_click(1))
btn_minus = tk.Button(root,text="-",width="5",font=("Arial",30),activebackground="gray",command=lambda:operator_click(2))
btn_equal = tk.Button(root,text="=")

entry.grid(row=0,column=0,columnspan=3)
btn_1.grid(row=1,column=0)
btn_2.grid(row=1,column=1)
btn_3.grid(row=1,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)
btn_0.grid(row=4,column=1)
btn_plus.grid(row=4,column=0) 
btn_minus.grid(row=4,column=2) 





root.mainloop()

















