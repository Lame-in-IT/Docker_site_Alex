import psycopg2
from conn_db import *
from dict_cat import dict_cat, dict_mno
from get_date import get_date

def get_zak(list_mouth, list_categ):
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST, port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    DATE_zak = get_date()
    list_prodaj = []
    full_list_prodaj = []
    list_ostat = []
    for index_categ, item_categ in enumerate(list_categ):
        time_list_prodaj = []
        if item_categ == 1:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT Продажи_через_2_месяца FROM warehouses WHERE ДАТА = '{DATE_zak}' AND Категория_товара = '{dict_cat[index_categ]}'"
                )
                list_prod = cursor.fetchall()
                for item_prod in list_prod:
                    for item_prod_1 in item_prod:
                        time_list_prodaj.append(item_prod_1)
        elif item_categ == 0:
            time_list_prodaj.append(0)
        list_prodaj.append(sum(time_list_prodaj))
    count = 0
    for index_mouth, item_mouth in enumerate(list_mouth):
        if item_mouth == 1:
            if count == 0:
                count += 1
                for item_sum in list_prodaj:
                    zakaz = item_sum * dict_mno[index_mouth]
                    full_list_prodaj.append(int(zakaz))
            elif count > 0:
                full_list_prodaj.clear()
                break
    for index_categ_1, item_categ_1 in enumerate(list_categ):
        time_list_prodaj_1 = []
        if item_categ_1 == 1:
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT Доступно_для_продажи FROM warehouses WHERE ДАТА = '{DATE_zak}' AND Категория_товара = '{dict_cat[index_categ_1]}' AND Маркетплейс = 'Яндекс Маркет'"
                )
                list_prod_1 = cursor.fetchall()
                for item_prod_1 in list_prod_1:
                    for item_prod_2 in item_prod_1:
                        time_list_prodaj_1.append(item_prod_2)
        elif item_categ_1 == 0:
            time_list_prodaj_1.append(0)
        list_ostat.append(sum(time_list_prodaj_1))
    list_zakaza = []
    for inde, itemm in enumerate(full_list_prodaj):
        raznoch = itemm - list_ostat[inde]
        if raznoch > 0:
            list_zakaza.append(raznoch)
        elif raznoch <= 0:
            list_zakaza.append(0)
    return list_zakaza
    
            
            
    
if __name__ == '__main__':
    get_zak()
    