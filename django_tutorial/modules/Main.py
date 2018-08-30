from Search import Selection
from Search import refresh
from Add import Add
import sys     

def Work():
    work = int(input("1.Search\n2.Import\n3.Exit\nSelection:\n"))
    if work == 1:
        Selection()
        Search_again()
    elif work == 2:
        Add()
        #print("developing")
    elif work == 3:
        sys.exit()
    else:
        print("Error")
        Work()

def Search_again():
    exit = input("Another search?[y/n]")
    if exit == 'y':
        refresh()
        Work()
    else:
        sys.exit()
Work()