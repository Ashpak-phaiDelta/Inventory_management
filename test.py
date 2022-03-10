import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox


distributor_names=["Liqiud Gold", "kishor", "nixon"]
category_=["beer","wishkey","rum"]
brand_=["kighfisher","mcdowelles","bira"]
product_=["100ml","50ml","60ml"]


col_name={'Distributor':distributor_names,"Category":category_,"Brand":brand_,"Product":product_,"Purchase Qty":None}


if __name__ == '__main__':
    root = tk.Tk()
    for col in col_name:
        label = tk.Label(text = col)
        label.grid(column=list(col_name).index(col),row=0)
        entry = AutocompleteCombobox(root, completevalues=col_name[col])
        entry.grid(row=1, column=list(col_name).index(col))
        tk.Button(text='delete').grid(row=1, column=len(col_name)+1)
    tk.Button(text='add').grid(row=15, column=0)
    tk.Button(text='confirm').grid(row=15, column=1)


    root.mainloop()
