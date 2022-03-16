
from datetime import datetime

from UI_maker import create_window
# from test import create_window

distributor_names=["Liqiud Gold","Nixon","Kishor"]
category_=["Beer","whiskey","Rum"]
brand_=["Kingfisher","Bira"]
product_=["Draught","Premium","Royal"]

inward_col_name={"Date":datetime.now().strftime("%d-%m-%Y"),"Batch":datetime.now().strftime("%d%m%Y"),'Distributor':distributor_names,"Invoice No.":None,"Category":category_,"Brand":brand_,"Product":product_,"Purchase Qty":None,"Purchase Rate":None,"Estimate sale rate":None}
inventory_data=["Date", "Batch", "Distributor","Invoice No.","Brand","Product","Qty available"]



Inward_UI=create_window("Inward",inward_col_name)
Inward_UI.add_button("add","yellow",Inward_UI.add_row,0,15)
Inward_UI.add_button("Confirm","cyan",Inward_UI.confim,len(inward_col_name)-1,15)



Inward_UI.tk.mainloop()

inventory_page=create_window("Invent_page",inventory_data)
inventory_page.feed_data()

inventory_page.tk.mainloop()