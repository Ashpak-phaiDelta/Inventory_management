import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from datetime import date

distributor_names=["Liqiud Gold","nixon","kishor"]
category_=["beer","whiskey","rum"]
brand_=["kingfisher","Bira"]
product_=["Draught","premium","royal"]

inward_col_name={'Distributor':distributor_names,"Invoice No.":None,"Category":category_,"Brand":brand_,"Product":product_,"Purchase Qty":None,"Purchase Rate":None,"Estimate sale rate":None}
inventory_data=["Date", "Batch", "Distributor","Invoice No.","Brand","Product"]

data=[]

class create_window():
    def __init__(self,window_name,colum_names):
        self.tk=tk
        self.window=self.tk.Tk()
        self.window.title(window_name)
        self.window.geometry("1250x500")
        self.column_names=colum_names
        self.n_row=0
        self.grid_={'0':colum_names}
        self.add_lable()

    def add_lable(self):
        for col in self.column_names:
            label = self.tk.Label(self.window , text = col)
            label.grid(column=list(self.column_names).index(col),row=0)

    def add_row(self):
        self.n_row=self.n_row+1
        self.grid_[str(self.n_row)]=[]
        for col in self.column_names:
            Entry = AutocompleteCombobox(self.window, completevalues=self.column_names[col])
            Entry.grid(row=self.n_row, column=list(self.column_names).index(col))
            self.grid_[str(self.n_row)].append(Entry)
        delete_button=self.tk.Button(self.window,text="delete",command=self.delete_row,bg="red")
        delete_button.grid(column=len(self.column_names)+1,row=self.n_row)    

    def delete_row(self):
        pass

    def add_button(self,text,color,func,col,row):
        add_button=self.tk.Button(self.window,text=text,command=func,bg=color)
        add_button.grid(column=col,row=row)

    def confim(self):
        global data
        data=self.fetch_data()
        print(data)

        self.window.destroy()

    def fetch_data(self):
        data=[]
        for i in range(1,self.n_row+1):
            row_data={}
            for col in self.column_names :
                row_data[col]=self.grid_[str(i)][list(self.column_names).index(col)].get()
            data.append(row_data)
        return data

    def feed_data(self):
        global data
        print("feeding Data : ",data)
        for row in data:
            for col in self.column_names:
                entry = tk.Entry(self.window)
                if col in row:
                    entry.grid(row=list(data).index(row)+1, column=list(self.column_names).index(col), sticky="ew")
                    entry.insert(0, row[col])
                else:
                    entry.grid(row=list(data).index(row)+1, column=list(self.column_names).index(col), sticky="ew")

            



Inward_UI=create_window("Inward",inward_col_name)
Inward_UI.add_button("add","yellow",Inward_UI.add_row,0,15)
Inward_UI.add_button("Confirm","cyan",Inward_UI.confim,10,15)


Inward_UI.tk.mainloop()

inventory_page=create_window("Invent_page",inventory_data)
inventory_page.feed_data()

inventory_page.tk.mainloop()