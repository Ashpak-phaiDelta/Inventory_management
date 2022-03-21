import mysql.connector
# from datetime import datetime, timedelta, date

#  database='inventory_managment',
#  user='ashpak',
#  password='test123456'


mydb = mysql.connector.connect(
  host="localhost",
  user="ashpak",
  password="test123456",
  database="inventory_managment",
  auth_plugin='mysql_native_password'
)


class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def get_results(db_cursor):
    desc = [d[0] for d in db_cursor.description]
    results = [dotdict(dict(zip(desc, res))) for res in db_cursor.fetchall()]
    return desc ,results


def run_sql_query(sql):
    cursor = mydb.cursor()
    cursor.execute(sql)
    desc , results = get_results(cursor)
    cursor.close()
    return desc, results

# desc, results =get_all_product_details()
# print(desc)
# for res in results:
#     # print(res)
#     if res['category']=='Whiskey ' and res['brand_name']=='Black Dog ':
#         print(res)


# for res in results:
#     if res['category']=="Whiskey ":
#         print(res)


