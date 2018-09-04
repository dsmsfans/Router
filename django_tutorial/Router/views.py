from django.shortcuts import render
from django.http import HttpResponse
import time
import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
data = pd.read_excel('Japan_test.xlsx')

Title = ['時間戳記','Brand','Model','Type','Network Type','Diamond Mode','Interface','Result',
         'Speedtest-ping(ms)','Speedtest-DL(Mbps)','Speedtest-UL(Mbps)','FTP(Ipv4)-DL Speed','Iperf-Jitter',
         'Iperf-lost','Iperf-ping loss','wrs21','streaming','Note']

Add_list = []
option = data["Result"] != None

def home_page(request):
    return render(request, 'home.html')

# def Search_page(request):
#     return render(request, 'search.html')

# def Add_page(request):
    return render(request, 'add.html')

def add(request): 
    request.encoding='utf-8'
    #Time
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    Add_list.append(local_time)
    #Brand
    if 'Brand' in request.GET:
        Add_list.append(request.GET['Brand'])
    
    #Model
    if 'Model' in request.GET:
        Add_list.append(request.GET['Model'])

    #Type
    if 'Type' in request.GET:
        Add_list.append(request.GET['Type'])
    
    #Network Type
    if 'Network Type' in request.GET:
        Add_list.append(request.GET['Network Type'])

    #Diamond Mode
    if 'Diamond mode' in request.GET:
        Add_list.append(request.GET['Diamond mode'])
    
    #Interface
    if 'Interface' in request.GET:
        Add_list.append(request.GET['Interface'])
    
    #Result
    if 'Result' in request.GET:
        Add_list.append(request.GET['Result'])
    
    #Streaming
    if 'Streaming' in request.GET:
        Add_list.append(request.GET['Streaming'])
    
    #Speed Add_list
    if 'ping' in request.GET:
        Add_list.append(request.GET['ping'])
    
    #Speed DL Add_list
    if 'DL' in request.GET:
        Add_list.append(request.GET['DL'])
    
    #Speed UL Add_list
    if 'UL' in request.GET:
        Add_list.append(request.GET['UL'])
    
    #FTP DL Add_list
    if 'FTPDL' in request.GET:
        Add_list.append(request.GET['FTPDL'])
    
    #Jitter
    if 'Jitter' in request.GET:
        Add_list.append(request.GET['Jitter'])
    
    #iperf loss
    if 'loss' in request.GET:
        Add_list.append(request.GET['loss'])
    
    #Ping loss
    if 'ping loss' in request.GET:
        Add_list.append(request.GET['ping loss'])
    
    #wrs21
    if 'wrs21' in request.GET:
        Add_list.append(request.GET['wrs21'])
    
    #Streaming
    if 'Streaming' in request.GET:
        Add_list.append(request.GET['Streaming'])
    
    #Note
    if 'Note' in request.GET:
        Add_list.append(request.GET['Note'])
    
    else:
        message = '你提交了空表单'
        
    message = "Completed"

    print(Add_list)
    data_toexcel()
    return HttpResponse(data.tail(5).to_html())

def search(request):
    global option
    option = data["Result"] != None
    request.encoding='utf-8'
    print('DADASFFFF')
    #Brand
    if 'Brand' in request.GET:
        option = option & data["Brand"].str.contains(request.GET['Brand'])
    
    #Model
    if 'Model' in request.GET:
        option = option & data["Model"].str.contains(request.GET['Model'])

    #Type
    if 'Type' in request.GET:
        option = option & data["Type"].str.contains(request.GET['Type'])
    
    #Network Type
    if 'Network Type' in request.GET:
        option = option & data["Network Type"].str.contains(request.GET['Network Type'])

    #Diamond Mode
    # if 'Diamond mode' in request.GET and request.GET['Diamond mode'] != None:
    #     option = option & data["Diamond mode"].str.contains(request.GET['Diamond mode'])
    
    #Interface
    if 'Interface' in request.GET:
        option = option & data["Interface"].str.contains(request.GET['Interface'])
    
    #Result
    if 'Result' in request.GET:
        option = option & data["Result"].str.contains(request.GET['Result'])

    return HttpResponse(data.loc[option].to_html()) 

def data_toexcel():
    global data
    output = pd.DataFrame([Add_list],columns = Title)
    data = data.append(output,ignore_index=True)
    data.to_excel('Japan_test.xlsx',na_rep=True,index=False)
    Add_list.clear()

def show_data(request):
    return HttpResponse(data.to_html())
    
    