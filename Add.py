import pandas as pd
import time

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
data = pd.read_excel('Japan_test.xlsx')

Title = ['時間戳記','Brand','Model','Type','Network Type','Diamond Mode','Interface','Result',
         'Speedtest-ping(ms)','Speedtest-DL(Mbps)','Speedtest-UL(Mbps)','FTP(Ipv4)-DL Speed','Iperf-Jitter',
         'Iperf-lost','Iperf-ping loss','wrs21','streaming','Note']

insert_list = []

def Insert():
    #Time
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    insert_list.append(local_time)
    
    #Brand
    insert = input("Brand: ")
    insert_list.append(insert)
    
    #Model
    insert = input("Model: ")
    insert_list.append(insert)
    
    #Type
    insert = input("Type: ")
    insert_list.append(insert)
    
    #Network
    insert = input("Network Type: ")
    insert_list.append(insert)
    
    #Diamond Mode
    insert = input("Diamond Mode: ")
    insert_list.append(insert)
    
    #Interface
    insert = input("Interface: ")
    insert_list.append(insert)
    
    #Result
    insert = input("Result: ")
    insert_list.append(insert)
    
    #Speedtest-ping(ms)
    insert = input("Speedtest-ping(ms): ")
    insert_list.append(insert)
    
    #Speedtest-DL(Mbps)
    insert = input("Speedtest-DL(Mbps): ")
    insert_list.append(insert)
    
    #Speedtest_UL(Mbps)
    insert = input("Speedtest-UL(Mbps): ")
    insert_list.append(insert)
    
    #FTP(Ipv4)-DL Speed
    insert = input("FTP(Ipv4)-DL Speed: ")
    insert_list.append(insert)
    
    #Iperf-Jitter
    insert = input("Iperf-Jitter: ")
    insert_list.append(insert)
    
    #Iperf-lost
    insert = input("Iperf-lost: ")
    insert_list.append(insert)
    
    #Iperf-ping loss
    insert = input("Iperf-ping loss: ")
    insert_list.append(insert)
    
    #wrs21
    insert = input("wrs21: ")
    insert_list.append(insert)
    
    #Streaming
    insert = input("streaming: ")
    insert_list.append(insert)
    
    #Note
    insert = input("Note: ")
    insert_list.append(insert)
    
    ques = input("Save the record?[y/n] ")
    if ques == 'y':
        data_toexcel()
        

def show_latest():
    print(data.tail(5))


def data_toexcel():
    global data
    output = pd.DataFrame([insert_list],columns = Title)
    data = data.append(output,ignore_index=True)
    data.to_excel('Japan_test.xlsx',na_rep=True,index=False)
    print(data.tail(5))

def Add():
    print("----------------------Adding Machine:----------------------")
    ques = input("1.Add Machine\n2.Show Latest\n")
    if ques == "1":
        Insert()
    elif ques == "2":
        show_latest()
    else:
        print("Error")
        Add()