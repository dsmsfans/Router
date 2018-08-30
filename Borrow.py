import pandas as pd
import time

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
data = pd.read_excel('Borrow.xlsx')

Title = ['時間戳記','Brand','Model','Name']
borrow_list = []

def Insert():
    #Time
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    borrow_list.append(local_time)
    
    #Brand
    insert = input("Brand: ")
    borrow_list.append(insert)
    
    #Model
    insert = input("Model: ")
    borrow_list.append(insert)

    #Name
    insert = input("Name: ")
    borrow_list.append(insert)

    ques = input("Save the record?[y/n] ")
    if ques == 'y':
        data_toexcel()

def data_toexcel():
    global data
    output = pd.DataFrame([borrow_list],columns = Title)
    data = data.append(output,ignore_index=True)
    data.to_excel('Borrow.xlsx',na_rep=True,index=False)
    print(data.tail(5))
    
Insert()