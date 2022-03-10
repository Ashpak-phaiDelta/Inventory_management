

import db_access

class Product_detail():
    def filter_product_by(self,filter_dict,data):
        for key in filter_dict:
            if filter_dict[key]!=None:
                filter_Data=[]
                for res in data:
                    if res[key]==filter_dict[key]:
                        filter_Data.append(res)
                data=filter_Data
        return data

    def get_list_of(self, col_name, data):
        result=[]
        for res in data:
            result.append(res[col_name])
        return list(set(result))


col_name, results= db_access.get_all_product_details()
products=Product_detail()
category_list=products.get_list_of('category',results)
print(category_list)
print('---'*40)

filter_dict={'category': 'Beer'}
all_beer=products.filter_product_by(filter_dict,results)
for beer in all_beer:
    print(beer)
print('---'*40)

all_bira=products.filter_product_by({'brand_name': 'Bira'},all_beer)
for beer in all_bira:
    print(beer)
print('---'*40)
# filter_dict={'category': 'Whiskey ','brand_name': 'Black Dog '}


# data=filter_product_by(filter_dict,results)
# for col in data:
#     print(col)


