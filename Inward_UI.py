import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox

n_row=0
distributor_names=["Liqiud Gold","nixon","kishor"]
category_=["beer","whiskey","rum"]
brand_=["kingfisher","Bira"]
product_=["Draught","premium","royal"]


col_name={'Distributor':distributor_names,"Invoice No.":None,"Category":category_,"Brand":brand_,"Product":product_,"Purchase Qty":None,"Purchase Rate":None,"Estimate sale rate":None}
grid_={'0':col_name}

inward_UI=tk.Tk()
inward_UI.title(" Inventory App ")    


def add_col_name():
    global col_name
    for col in col_name:
        label = tk.Label(text = col)
        label.grid(column=list(col_name).index(col),row=0)

def add_row():
    global n_row
    global col_name
    global grid_
    n_row=n_row+1
    grid_[str(n_row)]=[]
    for col in col_name:
        Entry = AutocompleteCombobox(inward_UI, completevalues=col_name[col])
        Entry.grid(row=n_row, column=list(col_name).index(col))
        grid_[str(n_row)].append(Entry)
    delete_button=tk.Button(inward_UI,text="delete",command=delete_row,bg="red")
    delete_button.grid(column=len(col_name)+1,row=n_row)    

def confirm():
    data=fetch_data()
    insert_data(data)

    pass

def fetch_data():
    data=[]
    for i in range(1,n_row+1):
        row_data={}
        for col in col_name:
            row_data[col]=grid_[str(i)][list(col_name).index(col)].get()
        data.append(row_data)
    print(data)
    return data

def delete_row():
    pass

def insert_data(data):
    test_={}
    for i in range(len(data)):
        for col in col_name:
            test_[col]=data[i][col]


add_col_name()
add_row()


add_button=tk.Button(inward_UI,text="Add",command=add_row,bg="yellow")
add_button.grid(column=0,row=15)

confirm_button=tk.Button(inward_UI,text="Confirm",command=confirm,bg="cyan")
confirm_button.grid(column=10,row=15)

inward_UI.mainloop()

