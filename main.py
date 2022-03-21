from datetime import datetime


from UI import Window
import db_access as db



def clean_data(column,data):
    list_=[]
    for col in column:
        for i in data:
            list_.append(i[col])
        return list_        

def get_data_from_db(sql):
    column,data=db.run_sql_query(sql=sql)
    return clean_data(column, data)


#product_id,product_name ,brand_name,category
product_=get_data_from_db(sql='select distinct(product_name) from product_master')
brand_=get_data_from_db(sql='select distinct(brand_name) from product_master')
category_=get_data_from_db(sql='select distinct(category) from product_master')

distributor_names=["Liqiud Gold","Nixon","Kishor"]


inward_col_name={"Date":datetime.now().strftime("%d-%m-%Y"),"Batch":datetime.now().strftime("%d%m%Y"),'Distributor':distributor_names,"Invoice No.":None,"Category":category_,"Brand":brand_,"Product":product_,"Purchase Qty":None,"Purchase Rate":None,"Estimate sale rate":None}
inventory_data=["Date", "Batch", "Distributor","Invoice No.","Brand","Product","Qty available"]
sales_col_name={"Purchase Date":None,"Bill_No.":None,"Batch":None, "Product":product_,"selling rate":None, "Pruchase rate":None}



data=[
    {"Date":datetime.now().strftime("%d-%m-%Y"),"Batch":datetime.now().strftime("%d%m%Y"),'Distributor':"Liquid Gold","Invoice No.":"ajkk","Category":"Beer","Brand":"Kingfisher","Product":"Draught","Purchase Qty":100,"Purchase Rate":80,"Estimate sale rate":100},
    {"Date":datetime.now().strftime("%d-%m-%Y"),"Batch":datetime.now().strftime("%d%m%Y"),'Distributor':"Kishor","Invoice No.":"ajkk","Category":"Beer","Brand":"Bira","Product":"Draught","Purchase Qty":100,"Purchase Rate":90,"Estimate sale rate":100},
    {"Date":datetime.now().strftime("%d-%m-%Y"),"Batch":datetime.now().strftime("%d%m%Y"),'Distributor':"Liquid Gold","Invoice No.":"ajkk","Category":"Whisky","Brand":"Royal Stag","Product":"Draught","Purchase Qty":100,"Purchase Rate":120,"Estimate sale rate":140}
]

class Menu_bar():
    def __init__(self,win) :
        self.win=win
        self.menu={"Inward":self.inward_menu,"Sales":self.sales_menu,"Inventory":self.inventory_menu}

    def add_menu_bar(self):
        menu_frame=self.win.creat_frame(f_row=0,column_names=self.menu)
        for item in self.menu:
            menu_frame.add_button(text=item,func=self.menu[item],row=0,col=list(self.menu).index(item))

    def close_window(self):
        self.win.close_window()

    def inward_menu(self):
        self.close_window()
        inward_window()
        pass

    def sales_menu(self):
        self.close_window()
        sales_window()
        pass

    def inventory_menu(self):
        self.close_window()
        inventory_window()
        pass

def create_new_window(window_name):
    window=Window(window_name)
    menu_bar=Menu_bar(window)
    menu_bar.add_menu_bar()

    return window

def inward_window():
    Inward_UI=create_new_window("Inward")
    
    lable_frame=Inward_UI.creat_frame(f_row=1,column_names=inward_col_name)
    lable_frame.add_lable()

    entry_frame=Inward_UI.creat_frame(f_row=2,column_names=inward_col_name)
    entry_frame.add_row()

    button_frame=Inward_UI.creat_frame(f_row=10,column_names=lable_frame.column_names)
    add_row_button=button_frame.add_button(text="add",func=entry_frame.add_row,row=0,col=0,color='yellow')
    confirm_button=button_frame.add_button(text="confirm",func=entry_frame.confirm,row=0, col=10, color='cyan')


    Inward_UI.tk.mainloop()

def inventory_window():

    Inventory_UI=create_new_window("Inventory")
    
    LabelFrame=Inventory_UI.creat_frame(f_row=1,column_names=inventory_data)
    LabelFrame.add_lable()
    entry_frame=Inventory_UI.creat_frame(f_row=2,column_names=inward_col_name)
    entry_frame.enter_Data(data)


    print("creating inventroy app")
    Inventory_UI.tk.mainloop()
    pass

def sales_window():
    sales_UI=create_new_window("Sales")
    
    label_frame=sales_UI.creat_frame(f_row=1,column_names=sales_col_name)
    label_frame.add_lable()
    
    entry_frame=sales_UI.creat_frame(f_row=2,column_names=sales_col_name)
    entry_frame.add_row()

    button_frame=sales_UI.creat_frame(f_row=3,column_names=sales_col_name)
    add_row_button=button_frame.add_button(text="add",func=entry_frame.add_row,row=0,col=0,color="yellow")
    preview_button=button_frame.add_button(text="preview",func=entry_frame.fetch_data,row=0,col=10, color="cyan")




    print("creating sales_window")


inward_window()
