import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
from datetime import date


data=[]

class Grid_loctor():
    def __init__(self,win,row,col):
        self.win=win
        self.row=row
        self.col=col

    def print_row(self):
        self.win.clear_row(self.row)



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
            label = self.tk.Label(self.window , text = col,width=15, justify= 'left')
            label.grid(column=list(self.column_names).index(col),row=0)

    def add_row(self):
        self.n_row=self.n_row+1
        self.grid_[str(self.n_row)]=[]
        for col in self.column_names:
            Entry = AutocompleteCombobox(self.window, width=15, completevalues=self.column_names[col])
            Entry.grid(row=self.n_row, column=list(self.column_names).index(col))
            self.grid_[str(self.n_row)].append(Entry)
        button_obj=Grid_loctor(self, self.n_row, len(self.column_names)+1)
        clear_button=self.tk.Button(self.window,text="clear",command=button_obj.print_row,takefocus=False)
        clear_button.grid(column=len(self.column_names)+1,row=self.n_row)    


    def clear_row(self,row):
        for i in self.grid_[str(row)]:
            i.set("")


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
                entry = tk.Entry(self.window,width=15)
                if col in row:
                    entry.grid(row=list(data).index(row)+1, column=list(self.column_names).index(col), sticky="ew")
                    entry.insert(0, row[col])
                else:
                    entry.grid(row=list(data).index(row)+1, column=list(self.column_names).index(col), sticky="ew")

            



