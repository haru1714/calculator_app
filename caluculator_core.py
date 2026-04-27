on_number = 0
now_number = 0
on_operator = 0 #　+を1、-を2で考える
pre_number = 0
pre_operator = 0



def update_number(now_number,on_number): #入力数値を並べる関数
    now_number = now_number * 10 + on_number
    return now_number

def operator_input(on_operator,pre_operator,pre_number,now_number) #演算子の入力関数
    if pre_operator == 0:
        pre_operator = on_operator
        pre_number = now_number
    
    else:
        if pre_operator == 1:
            pre_number = now_number + pre_number
        elif pre_operator == 2:
            pre_number = pre_number - now_number 
        now_number = 0
        pre_operator = on_operator

    return(pre_operator,pre_number,now_number)

def exe_equal(pre_operator,pre_number,now_number) #イコール処理
    if pre_operator == 1:
        now_number = pre_number + now_number
    elif pre_operator == 2:
        now_number = pre_number - now_number

    pre_operator = 0
    pre_number = 0
    return(pre_operator,pre_number,now_number)     

