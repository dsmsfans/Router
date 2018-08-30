import pandas as pd

Brand_flag = 0
Model_flag = 0
Type_flag = 0
Diamond_mode_flag = 0
Interface_flag = 0
Result_flag = 0

#pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
data = pd.read_excel('Japan_test.xlsx')

#global option
option = data["Result"] != None


def check_flag():
    global option
    if Brand_flag or Model_flag or Type_flag or Interface_flag or Result_flag or Diamond_mode_flag != 0:
        if Brand_flag == 1:
            brand = input("Input your Brand: ")
            option = option & data["Brand"].str.contains(brand)
            
        if Model_flag == 1:
            model = str(input("Input your Model: "))
            option = option & data["Model"].str.contains(model)
            
        if Type_flag == 1:
            what_type = str(input("Input your Type: "))
            option = option & data["Type"].str.contains(what_type)
        
        if Diamond_mode_flag == 1:
            diamond_mode = str(input("Input your Diamond_Mode: "))
            option = option & data["Diamond Mode"].str.contains(diamond_mode)
            
        if Interface_flag == 1:
            interface = str(input("Input your Interface: "))
            option = option & data["Interface"].str.contains(interface)
            
        if Result_flag == 1:
            result = str(input("Input your Result: "))
            option = option & data["Result"].str.contains(result)
            
        print(data.loc[option])
            
    else:
        print("Please choose some option!\n")
    
def Selection():
    print("----------------------Select the header:----------------------")
    header = int(input("1.Brand\n2.Model\n3.Type\n4.Diamond_Mode\n5.Interface\n6.Result\n\nselection:\n"))
    if header < 1 or header > 6 or type(header) != int:
        print("Wrong number!\nSelect again")
        Selection()
    header_select(header)

def header_select(selection):
    global Brand_flag,Model_flag,Type_flag,Interface_flag,Result_flag,Diamond_mode_flag
    #Brand
    if selection == 1:
        Brand_flag = 1
    #Model
    if selection == 2:
        Model_flag = 1
    #Type
    if selection == 3:
        Type_flag = 1
        
    # Diamond_Mode
    if selection == 4:
        Diamond_mode_flag = 1

    #Interface
    if selection == 5:
        Interface_flag = 1
    #Result
    if selection == 6:
        Result_flag = 1
    Select_Again()

def Select_Again():
    i = input("Select More Option?[y/n]")
    if i == "y":
        Selection()
    elif i == "n":
        check_flag()
    else:
        print("Error")
        Select_Again()
        
def refresh():
    global Brand_flag,Model_flag,Type_flag,Interface_flag,Result_flag,Diamond_mode_flag,option
    option = data["Result"] != None
    Brand_flag = 0
    Model_flag = 0
    Type_flag = 0
    Diamond_mode_flag = 0
    Interface_flag = 0
    Result_flag = 0
    
