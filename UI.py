import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox

class Grid_loctor():
    def __init__(self,frame,row,col):
        self.frame=frame
        self.row=row
        self.col=col

    def print_row(self):
        print("row number ",self.row, " was cleared")

    def clear_row(self):
        self.frame.clear_row(self.row)

class Window():
    def __init__(self,window_name):
        self.tk=tk
        self.window=self.tk.Tk()
        self.window.title(window_name)
        self.window.geometry("1250x500")
        self.frame_row=0
        self.frame_col=0

    def close_window(self):
        self.window.destroy()

    def clean_window(self):
        pass
        #need to creat method to clear all window contents

    def creat_frame(self,f_row=0,f_col=0,column_span=1,row_span=1, column_names=None,row_names=None):        
        self.frame_obj=Frame(self.window,f_row,f_col, column_span,row_span,column_names,row_names)
        return self.frame_obj
       
class Frame():
    def __init__(self,window,row,col,column_span=1,row_span=1,column_names=None,row_names=None):
        self.window=window
        self.frame=tk.Frame(window)
        self.column_names=column_names
        self.row_names=row_names
        self.n_row=0
        self.n_col=0
        self.grid_={'0':column_names}
        self.frame.grid(row=row,column=col,columnspan=column_span,rowspan=row_span,sticky='nsew')
        self.data=[]

    def add_lable(self):
        for i in self.column_names:
            label=tk.Label(self.frame,text=i, width=15,justify="left")
            label.grid(column=list(self.column_names).index(i),row=0)

    def add_row(self):
        self.n_row=self.n_row+1
        self.grid_[str(self.n_row)]=[]
        for col in self.column_names:
            entry= AutocompleteCombobox(self.frame, width=15, completevalues=self.column_names[col])
            entry.grid(row=self.n_row, column=list(self.column_names).index(col))
            self.grid_[str(self.n_row)].append(entry)
        button_obj=Grid_loctor(self, self.n_row, len(self.column_names)+1)
        clear_button=tk.Button(self.frame,text="clear",command=button_obj.clear_row,takefocus=False)
        clear_button.grid(column=len(self.column_names)+1,row=self.n_row)    

    def enter_Data(self,data):
        for row_entry in data:
            for col in self.column_names:
                entry = tk.Entry(self.frame,width=15)
                entry.grid(row=list(data).index(row_entry) ,column=list(self.column_names).index(col), sticky="ew")
                if col in row_entry:
                    entry.insert(0,row_entry[col])

    def temp(self):
        print("temp fuc is passed")

    def add_button(self,text,func,col,row,color=None):
        add_button=tk.Button(self.frame,text=text,command=func,bg=color)
        add_button.grid(column=col,row=row)


    def confirm(self):
        self.data=self.fetch_data()
        self.window.destroy()

    def fetch_data(self):
        self.data=[]
        for i in range(1,self.n_row+1):
            row_data={}
            for col in self.column_names :
                row_data[col]=self.grid_[str(i)][list(self.column_names).index(col)].get()
            self.data.append(row_data)
        for i in self.data.copy():
            e=None
            for key in i:
                if i[key]!="":
                    e=False
            if e is None:
                self.data.pop(self.data.index(i))
        print(self.data)
        return self.data

    def clear_row(self,row):
        for i in self.grid_[str(row)]:
            i.set("")


    def bill_preview(self):
        self.data=self.fetch_data()
        