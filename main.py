import uvicorn
from fastapi import FastAPI, Request, Body, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from datetime import datetime
import psycopg2
import pandas as pd
import openpyxl
from statistics import mean

from download_file import download_file
from conn_db import *
from bd_zak import get_zak
from get_session import get_engine_from_settings
from dict_month import dict_month, dict_month_earth_2022
from dict_cat import dict_cat, dict_mno, dict_rename, dict_name
from get_date import get_date

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/fin/', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/')
async def hello_1(action1: str = Form(...)):
    if action1 == 'download':
        return FileResponse('Заказ в Китае бланк.xlsx', media_type='application/octet-stream', filename='Заказ в Китае бланк.xlsx')


@app.get('/', response_class=HTMLResponse)
async def read_item_1(request: Request):
    return templates.TemplateResponse("zakaz.html", {"request": request})

@app.get('/analiz', response_class=HTMLResponse)
async def read_item_2(request: Request):
    return templates.TemplateResponse("analiz.html", {"request": request})

@app.get('/analiz_tabl', response_class=HTMLResponse)
async def analiz_tabl(request: Request):
    return templates.TemplateResponse("analiz_tabl.html", {"request": request})

@app.post("/zakaz")
async def zakaz(data=Body()):
    list_mouth = []
    list_categ = []
    chbox17 = data
    for value_mouth in range(1, 16):
        if chbox17[f"chbox{value_mouth}"] == True:
            list_categ.append(1)
        if chbox17[f"chbox{value_mouth}"] == False:
            list_categ.append(0)
    for value_categ in range(16, 19):
        if chbox17[f"chbox{value_categ}"] == True:
            list_mouth.append(1)
        if chbox17[f"chbox{value_categ}"] == False:
            list_mouth.append(0)
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    DATE_zak = get_date()
    list_name = []
    list_sale_name = []
    full_list_prodaj = []
    full_list_dostup = []
    list_zakaza = []
    list_sebest = []
    table_df = pd.read_sql(f"SELECT * FROM warehouses WHERE ДАТА = '{DATE_zak}'", con=get_engine_from_settings())
    for index_categ, item_categ in enumerate(list_categ):
        if item_categ == 1:
            for item_name in table_df[table_df.Категория_товара == f'{dict_cat[index_categ][0]}'].Название_товара:
                if item_name not in list_name:
                    list_name.append(item_name)
                    list_sebest.append(dict_cat[index_categ][1])
    for item_sale_name in list_name:
        list_sale_name_time = []
        for item_name in table_df[table_df.Название_товара == f'{item_sale_name}'].Продажи_через_2_месяца:
            list_sale_name_time.append(item_name)
        list_sale_name.append(sum(list_sale_name_time))
    count = 0
    for index_mouth, item_mouth in enumerate(list_mouth):
        if item_mouth == 1:
            if count == 0:
                count += 1
                for item_sum in list_sale_name:
                    zakaz = item_sum * dict_mno[index_mouth]
                    full_list_prodaj.append(int(zakaz))
            elif count > 0:
                full_list_prodaj.clear()
            break
    for item_dostup in list_name:
        list_dostup_time = []
        for item_dostup_1 in table_df[table_df.Название_товара == f'{item_dostup}'].Доступно_для_продажи:
            list_dostup_time.append(item_dostup_1)
        full_list_dostup.append(sum(list_dostup_time))
    it = 0
    while it < 5:
        for index_re, item_re in enumerate(list_name):
            if item_re in dict_rename:
                insex_list = list_name.index(f"{dict_rename[item_re]}")
                sum_ostat = list_sale_name[index_re] + list_sale_name[insex_list]
                list_sale_name[insex_list] = sum_ostat
                list_name.pop(index_re)
                list_sale_name.pop(index_re)
                full_list_prodaj.pop(index_re)
                full_list_dostup.pop(index_re)
                list_sebest.pop(index_re)
        it += 1
        continue
    for inde, itemm in enumerate(full_list_prodaj):
        raznoch = itemm - full_list_dostup[inde]
        if raznoch > 0:
            list_zakaza.append(raznoch)
        elif raznoch <= 0:
            list_zakaza.append(0)
    list_new_name = []
    list_new_zaka = []
    list_new_summa_zaku = []
    for index, item in enumerate(list_zakaza):
        if item > 0:
            list_new_name.append(list_name[index])
            list_new_zaka.append(item)
            sum_sebes = item * list_sebest[index]
            sum_viruchka = '{0:,}'.format(int(sum_sebes)).replace(',', ' ') + " " + "руб."
            list_new_summa_zaku.append(sum_viruchka)
    return {
        "number": list_new_name,
        "number1": list_new_zaka,
        "number2": list_new_summa_zaku,
    }
    
@app.post("/zakaz_1")
async def zakaz_1(data=Body()):
    list_sum_sebes = []
    list_sum_namder = []
    list_sum = []
    list_mouth = []
    for index_1, item_1 in enumerate(data["zakaz_sht"]):
        if item_1 != "":
            sum_sebes = int(item_1) * dict_name[data["zakaz_sht1"][index_1]]
            sum_sebes_1 = '{0:,}'.format(int(sum_sebes)).replace(',', ' ') + " " + "руб."
            list_sum_sebes.append(sum_sebes_1)
            list_sum.append(sum_sebes)
            list_sum_namder.append(int(item_1))
    sum_namder = '{0:,}'.format(int(sum(list_sum_namder))).replace(',', ' ') + " " + "шт."
    sum_sum = '{0:,}'.format(int(sum(list_sum))).replace(',', ' ') + " " + "руб."
    for value_categ in range(0, 3):
        if data["zakaz_sht2"][value_categ] == True:
            list_mouth.append(1)
        if data["zakaz_sht2"][value_categ] == False:
            list_mouth.append(0)
    for index_mouth, item_mouth in enumerate(list_mouth):
        if item_mouth == 1:
            if index_mouth == 0:
                name_period = "Период обеспечения 2 мес."
                break
            elif index_mouth == 1:
                name_period = "Период обеспечения 3 мес."
                break
            elif index_mouth == 2:
                name_period = "Период обеспечения 6 мес."
                break
    book = openpyxl.Workbook()
    sheet = book.active
    sheet["A1"] = f"{name_period}"
    sheet["A2"] = "Наименование товара"
    sheet["B2"] = "Количество"
    sheet["C2"] = "Себестоимость с доставкой"
    sheet["D2"] = "Сумма заказа, руб."
    list_index = []
    for index_price, item_price in enumerate(list_sum):
        index_sheet = index_price + 3
        list_index.append(index_sheet)
        sheet[f"A{index_sheet}"] = data["zakaz_sht1"][index_price]
        sheet[f"B{index_sheet}"] = list_sum_namder[index_price]
        sheet[f"C{index_sheet}"] = dict_name[data["zakaz_sht1"][index_price]]
        sheet[f"D{index_sheet}"] = item_price
    ind = list_index[-1] + 1
    sheet[f"A{ind}"] = "Итого:"
    sheet[f"B{ind}"] = sum_namder
    sheet[f"D{ind}"] = sum_sum
    book.save('Заказ в Китае бланк.xlsx')
    book.close()
    return {
        "zakaz_sht": list_sum_sebes,
        "zakaz_sht1": sum_namder,
        "zakaz_sht2": sum_sum,
    }

@app.post("/ABC_analiz")
async def ABC_analiz(data=Body()):
    mouth = data["analiz"]
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    list_price = []
    list_katalog = []
    list_Процен_прибыли = []
    list_Накопленная_доля = []
    list_Индекс = []
    if mouth == "1 месяц":
        table_df = pd.read_sql(
            f"SELECT * FROM profit", con=get_engine_from_settings())
        for item_price in table_df["Прибыли"]:
            list_price.append(item_price)
        for item_katalog in table_df["Категория"]:
            list_katalog.append(item_katalog)
        for item_Процен_прибыли in table_df["Процен_прибыли"]:
            list_Процен_прибыли.append(item_Процен_прибыли)
        for item_Накопленная_доля in table_df["Накопленная_доля"]:
            list_Накопленная_доля.append(item_Накопленная_доля)
        for item_Индекс in table_df["Индекс"]:
            list_Индекс.append(item_Индекс)
    if mouth == "3 месяц":
        table_df = pd.read_sql(
            f"SELECT * FROM profit_90", con=get_engine_from_settings())
        for item_price in table_df["Прибыли"]:
            list_price.append(item_price)
        for item_katalog in table_df["Категория"]:
            list_katalog.append(item_katalog)
        for item_Процен_прибыли in table_df["Процен_прибыли"]:
            list_Процен_прибыли.append(item_Процен_прибыли)
        for item_Накопленная_доля in table_df["Накопленная_доля"]:
            list_Накопленная_доля.append(item_Накопленная_доля)
        for item_Индекс in table_df["Индекс"]:
            list_Индекс.append(item_Индекс)
    if mouth == "1 год":
        table_df = pd.read_sql(
            f"SELECT * FROM profit_365", con=get_engine_from_settings())
        for item_price in table_df["Прибыли"]:
            list_price.append(item_price)
        for item_katalog in table_df["Категория"]:
            list_katalog.append(item_katalog)
        for item_Процен_прибыли in table_df["Процен_прибыли"]:
            list_Процен_прибыли.append(item_Процен_прибыли)
        for item_Накопленная_доля in table_df["Накопленная_доля"]:
            list_Накопленная_доля.append(item_Накопленная_доля)
        for item_Индекс in table_df["Индекс"]:
            list_Индекс.append(item_Индекс)
    len_list_katalog = len(list_katalog)
    return {
        "message": list_price,
        "message1": list_katalog,
        "message2": len_list_katalog,
        "message3": list_Процен_прибыли,
        "message4": list_Накопленная_доля,
        "message5": list_Индекс,
    }            


@app.post("/createTable")
async def createTable(data=Body()):
    market = data["analiz1"]
    date_full = data["analiz2"].split(" ")
    date_a = datetime.strptime(date_full[0], "%d.%m.%Y").date()
    date_b = datetime.strptime(date_full[2], "%d.%m.%Y").date()
    date_midle = int(str(date_b - date_a).split(" ")[0])
    date = data["analiz2"].replace("-", ".").replace(" ", "").split(".")
    date_old = str(date[2] + "-" + date[1] + "-" + date[0])
    date_new = str(date[5] + "-" + date[4] + "-" + date[3])
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    list_date = []
    list_date_1 = []
    list_name = ["Маркетплейс", ]
    list_market = ["OZON                          ", "Wildberries                   ", "Яндекс.Маркет                 "]
    list_1 = []
    list_2 = []
    list_3 = []
    list_strok = [0, 0,]
    if market == "-":
        table_df = pd.read_sql(
            f"SELECT * FROM zakazi WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}'",
            con=get_engine_from_settings())
        for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
            if item_Принят_в_обработку not in list_date:
                list_date.append(item_Принят_в_обработку)
                list_date_1.append(item_Принят_в_обработку.strip())
                list_name.append('Количество/Цена продажи')
        list_date.sort(reverse=True)
        list_date_1.sort(reverse=True)
        list_date_1.insert(0, "")
        for index_mark, item_mark in enumerate(list_market):
            if index_mark == 0:
                list_1.append('OZON')
            if index_mark == 1:
                list_2.append('Wildberries')
            if index_mark == 2:
                list_3.append('Яндекс.Маркет')
            list_strok.append(0)
            for item_date in list_date:                
                time_list_Колич= []
                time_list_Sale= []
                for item_1_Выруч in table_df[(table_df.Принят_в_обработку == f'{item_date}') & (table_df.Маркетплейс == f'{item_mark}')].Количество_заказов:
                    time_list_Колич.append(item_1_Выруч)
                for item_1_Sale in table_df[(table_df.Принят_в_обработку == f'{item_date}') & (table_df.Маркетплейс == f'{item_mark}')].Цена_заказов:
                    time_list_Sale.append(item_1_Sale)
                if index_mark == 0:
                    sum_str = '{0:,}'.format(int(sum(time_list_Sale))).replace(',', ' ')
                    list_1.append(str(sum(time_list_Колич)) + '/' + str(sum_str))
                if index_mark == 1:
                    sum_str = '{0:,}'.format(int(sum(time_list_Sale))).replace(',', ' ')
                    list_2.append(str(sum(time_list_Колич)) + '/' + str(sum_str))
                if index_mark == 2:
                    sum_str = '{0:,}'.format(int(sum(time_list_Sale))).replace(',', ' ')
                    list_3.append(str(sum(time_list_Колич)) + '/' + str(sum_str))
    else:
        table_df = pd.read_sql(
            f"SELECT * FROM zakazi WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}'",
            con=get_engine_from_settings())
        for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
            if item_Принят_в_обработку not in list_date:
                list_date.append(item_Принят_в_обработку)
                list_date_1.append(item_Принят_в_обработку.strip())
                list_name.append('Количество/Цена продажи')
        list_date.sort(reverse=True)
        list_date_1.sort(reverse=True)
        list_date_1.insert(0, "")
        list_strok.append(0)
        list_1.append(market)
        for item_date in list_date:                
            time_list_Колич= []
            time_list_Sale= []
            for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_date}'].Количество_заказов:
                time_list_Колич.append(item_1_Выруч)
            for item_1_Sale in table_df[table_df.Принят_в_обработку == f'{item_date}'].Цена_заказов:
                time_list_Sale.append(item_1_Sale)
            sum_str = '{0:,}'.format(int(sum(time_list_Sale))).replace(',', ' ')
            list_1.append(str(sum(time_list_Колич)) + '/' + str(sum_str))
    len_list = len(list_date_1)
    list_len_strok = len(list_strok)
    return {
        "message": list_date_1,
        "message1": len_list,
        "message2": list_name,
        "message3": list_1,
        "message4": list_2,
        "message5": list_3,
        "message6": list_len_strok,
    }


@app.post("/analiz")
async def analiz(data=Body()):
    categ = data["analiz"]
    market = data["analiz1"]
    date_full = data["analiz2"].split(" ")
    date_a = datetime.strptime(date_full[0], "%d.%m.%Y").date()
    date_b = datetime.strptime(date_full[2], "%d.%m.%Y").date()
    date_midle = int(str(date_b - date_a).split(" ")[0])
    date = data["analiz2"].replace("-", ".").replace(" ", "").split(".")
    date_old = str(date[2] + "-" + date[1] + "-" + date[0])
    date_new = str(date[5] + "-" + date[4] + "-" + date[3])
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    list_viruchka = []
    list_prof = []
    list_valov = []
    list_collich = []
    list_rentab = []
    list_categ_rentab = []
    list_categ_rentab_1 = []
    list_value_rentab = []
    list_date = []
    list_date_1 = []
    list_price_for_date = []
    list_stat = []
    list_stat_1 = []
    list_numb_coll = []
    list_name = []
    list_name_1 = []
    list_name_2 = []
    list_sum_name = []
    list_sum_name_1 = []
    if categ == "-":
        if market == "-":
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            for item_categ_rentab in table_df["Категория_товара"]:
                if item_categ_rentab not in list_categ_rentab:
                    list_categ_rentab.append(item_categ_rentab)
                    list_categ_rentab_1.append(item_categ_rentab.strip())
            for item in list_categ_rentab:
                time_list = []
                for item_1 in table_df[table_df.Категория_товара == f'{item}'].Процент_рентабельности:
                    time_list.append(item_1)
                try:
                    midle_rent = round((mean(time_list)), 1)
                except:
                    midle_rent = 0
                list_value_rentab.append(midle_rent)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            for item_stat in table_df["Статус_заказа"]:
                if item_stat not in list_stat:
                    list_stat.append(item_stat)
                    list_stat_1.append(item_stat.strip())
            for item_Название_товара in table_df["Название_товара"]:
                if item_Название_товара not in list_name:
                    list_name.append(item_Название_товара)
                    list_name_1.append(item_Название_товара.strip())
            for item_Название_sum in list_name:
                time_Название_sum = []
                for item_Название_sum_1 in table_df[table_df.Название_товара == f'{item_Название_sum}'].Валовая_прибыль:
                    time_Название_sum.append(item_Название_sum_1)
                list_sum_name.append(int(sum(time_Название_sum)))
            for item_pop in range(1, 6):
                try:
                    maxim = max(list_sum_name)
                    index_maxim = list_sum_name.index(maxim)
                    list_sum_name_1.append(maxim)
                    list_sum_name.pop(index_maxim)
                    list_name_2.append(list_name_1[index_maxim])
                    list_name_1.pop(index_maxim)
                except:
                    list_sum_name_1.append("Товара нет")
                    list_name_2.append(0)
            for item_stat_nub in list_stat:
                time_stat_nub = []
                for item_1_stat_nub in table_df[table_df.Статус_заказа == f'{item_stat_nub}'].Количество_товара:
                    time_stat_nub.append(item_1_stat_nub)
                list_numb_coll.append(int(sum(time_stat_nub)))
        else:
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            for item_categ_rentab in table_df["Категория_товара"]:
                if item_categ_rentab not in list_categ_rentab:
                    list_categ_rentab.append(item_categ_rentab)
                    list_categ_rentab_1.append(item_categ_rentab.strip())
            for item in list_categ_rentab:
                time_list = []
                for item_1 in table_df[table_df.Категория_товара == f'{item}'].Процент_рентабельности:
                    time_list.append(item_1)
                try:
                    midle_rent = round((mean(time_list)), 1)
                except:
                    midle_rent = 0
                list_value_rentab.append(midle_rent)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            for item_stat in table_df["Статус_заказа"]:
                if item_stat not in list_stat:
                    list_stat.append(item_stat)
                    list_stat_1.append(item_stat.strip())
            for item_Название_товара in table_df["Название_товара"]:
                if item_Название_товара not in list_name:
                    list_name.append(item_Название_товара)
                    list_name_1.append(item_Название_товара.strip())
            for item_Название_sum in list_name:
                time_Название_sum = []
                for item_Название_sum_1 in table_df[table_df.Название_товара == f'{item_Название_sum}'].Валовая_прибыль:
                    time_Название_sum.append(item_Название_sum_1)
                list_sum_name.append(int(sum(time_Название_sum)))
            for item_pop in range(1, 6):
                try:
                    maxim = max(list_sum_name)
                    index_maxim = list_sum_name.index(maxim)
                    list_sum_name_1.append(maxim)
                    list_sum_name.pop(index_maxim)
                    list_name_2.append(list_name_1[index_maxim])
                    list_name_1.pop(index_maxim)
                except:
                    list_sum_name_1.append("Товара нет")
                    list_name_2.append(0)
            for item_stat_nub in list_stat:
                time_stat_nub = []
                for item_1_stat_nub in table_df[table_df.Статус_заказа == f'{item_stat_nub}'].Количество_товара:
                    time_stat_nub.append(item_1_stat_nub)
                list_numb_coll.append(int(sum(time_stat_nub)))
            for item_Выруч in list_date:
                time_list_Выруч = []
                for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                    time_list_Выруч.append(item_1_Выруч)
                midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                list_price_for_date.append(midle_rent_Выруч)
    else:
        if market == "-":
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Категория_товара = '{categ}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            for item_categ_rentab in table_df["Категория_товара"]:
                if item_categ_rentab not in list_categ_rentab:
                    list_categ_rentab.append(item_categ_rentab)
                    list_categ_rentab_1.append(item_categ_rentab.strip())
            for item in list_categ_rentab:
                time_list = []
                for item_1 in table_df[table_df.Категория_товара == f'{item}'].Процент_рентабельности:
                    time_list.append(item_1)
                try:
                    midle_rent = round((mean(time_list)), 1)
                except:
                    midle_rent = 0
                list_value_rentab.append(midle_rent)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            for item_stat in table_df["Статус_заказа"]:
                if item_stat not in list_stat:
                    list_stat.append(item_stat)
                    list_stat_1.append(item_stat.strip())
            for item_Название_товара in table_df["Название_товара"]:
                if item_Название_товара not in list_name:
                    list_name.append(item_Название_товара)
                    list_name_1.append(item_Название_товара.strip())
            for item_Название_sum in list_name:
                time_Название_sum = []
                for item_Название_sum_1 in table_df[table_df.Название_товара == f'{item_Название_sum}'].Валовая_прибыль:
                    time_Название_sum.append(item_Название_sum_1)
                list_sum_name.append(int(sum(time_Название_sum)))
            for item_pop in range(1, 6):
                try:
                    maxim = max(list_sum_name)
                    index_maxim = list_sum_name.index(maxim)
                    list_sum_name_1.append(maxim)
                    list_sum_name.pop(index_maxim)
                    list_name_2.append(list_name_1[index_maxim])
                    list_name_1.pop(index_maxim)
                except:
                    list_sum_name_1.append("Товара нет")
                    list_name_2.append(0)
            for item_stat_nub in list_stat:
                time_stat_nub = []
                for item_1_stat_nub in table_df[table_df.Статус_заказа == f'{item_stat_nub}'].Количество_товара:
                    time_stat_nub.append(item_1_stat_nub)
                list_numb_coll.append(int(sum(time_stat_nub)))
            for item_Выруч in list_date:
                time_list_Выруч = []
                for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                    time_list_Выруч.append(item_1_Выруч)
                midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                list_price_for_date.append(midle_rent_Выруч)
        else:
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}' AND Категория_товара = '{categ}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            for item_categ_rentab in table_df["Категория_товара"]:
                if item_categ_rentab not in list_categ_rentab:
                    list_categ_rentab.append(item_categ_rentab)
                    list_categ_rentab_1.append(item_categ_rentab.strip())
            for item in list_categ_rentab:
                time_list = []
                for item_1 in table_df[table_df.Категория_товара == f'{item}'].Процент_рентабельности:
                    time_list.append(item_1)
                try:
                    midle_rent = round((mean(time_list)), 1)
                except:
                    midle_rent = 0
                list_value_rentab.append(midle_rent)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            for item_stat in table_df["Статус_заказа"]:
                if item_stat not in list_stat:
                    list_stat.append(item_stat)
                    list_stat_1.append(item_stat.strip())
            for item_Название_товара in table_df["Название_товара"]:
                if item_Название_товара not in list_name:
                    list_name.append(item_Название_товара)
                    list_name_1.append(item_Название_товара.strip())
            for item_Название_sum in list_name:
                time_Название_sum = []
                for item_Название_sum_1 in table_df[table_df.Название_товара == f'{item_Название_sum}'].Валовая_прибыль:
                    time_Название_sum.append(item_Название_sum_1)
                list_sum_name.append(int(sum(time_Название_sum)))
            for item_pop in range(1, 6):
                try:
                    maxim = max(list_sum_name)
                    index_maxim = list_sum_name.index(maxim)
                    list_sum_name_1.append(maxim)
                    list_sum_name.pop(index_maxim)
                    list_name_2.append(list_name_1[index_maxim])
                    list_name_1.pop(index_maxim)
                except:
                    list_sum_name_1.append("Товара нет")
                    list_name_2.append(0)
            for item_stat_nub in list_stat:
                time_stat_nub = []
                for item_1_stat_nub in table_df[table_df.Статус_заказа == f'{item_stat_nub}'].Количество_товара:
                    time_stat_nub.append(item_1_stat_nub)
                list_numb_coll.append(int(sum(time_stat_nub)))
            for item_Выруч in list_date:
                time_list_Выруч = []
                for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                    time_list_Выруч.append(item_1_Выруч)
                midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                list_price_for_date.append(midle_rent_Выруч)
    sum_viruchka = '{0:,}'.format(int(sum(list_viruchka))).replace(',', ' ')
    summ = '{0:,}'.format(int(sum(list_prof))).replace(',', ' ')
    summ_val = '{0:,}'.format(int(sum(list_valov))).replace(',', ' ')
    summ_collich = '{0:,}'.format(sum(list_collich)).replace(',', ' ')
    try:
        summ_rentab = round(mean(list_rentab), 1)
    except:
        summ_rentab = 0
    return {
        "message": f"{summ}",
        "message1": f"{summ_val}",
        "message2": f"{summ_collich}",
        "message3": f"{summ_rentab}",
        "message4": list_categ_rentab_1,
        "message5": list_value_rentab,
        "message6": list_date_1,
        "message7": list_price_for_date,
        "message8": list_stat_1,
        "message9": list_numb_coll,
        "message10": list_name_2,
        "message11": list_sum_name_1,
        "message12": sum_viruchka,
    }
    
@app.post("/analiz_1")
async def analiz_1(data=Body()):
    categ = data["analiz"]
    market = data["analiz1"]
    date_full = data["analiz2"].split(" ")
    date_a = datetime.strptime(date_full[0], "%d.%m.%Y").date()
    date_b = datetime.strptime(date_full[2], "%d.%m.%Y").date()
    date_midle = int(str(date_b - date_a).split(" ")[0])
    date = data["analiz2"].replace("-", ".").replace(" ", "").split(".")
    date_old = str(date[2] + "-" + date[1] + "-" + date[0])
    date_new = str(date[5] + "-" + date[4] + "-" + date[3])
    prodaj = data["analiz3"]
    valova = data["analiz4"]
    kollich = data["analiz5"]
    pocheitt = data["analiz6"]
    viruchka = data["analiz7"]
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
    list_viruchka = []
    list_prof = []
    list_valov = []
    list_collich = []
    list_rentab = []
    list_date = []
    list_date_1 = []
    list_price_for_date = []
    if categ == "-":
        if market == "-":
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
        else:
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
    else:
        if market == "-":
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Категория_товара = '{categ}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
        else:
            table_df = pd.read_sql(
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}' AND Категория_товара = '{categ}'",
                con=get_engine_from_settings())
            for item_viruchka in table_df["Цена_продажи"]:
                list_viruchka.append(item_viruchka)
            for item_Выручка in table_df["Выручка"]:
                list_prof.append(item_Выручка)
            for item_Валовая_прибыль in table_df["Валовая_прибыль"]:
                list_valov.append(item_Валовая_прибыль)
            for item_Количество_товара in table_df["Количество_товара"]:
                list_collich.append(item_Количество_товара)
            for item_Процент_рентабельности in table_df["Процент_рентабельности"]:
                list_rentab.append(item_Процент_рентабельности)
            if date_midle <= 31:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку.strip())
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Принят_в_обработку == f'{item_Выруч}'].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 31 and date_midle <= 61:
                for item_Принят_в_обработку in table_df["Неделя_обработку"]:
                    if item_Принят_в_обработку not in list_date:
                        list_date.append(item_Принят_в_обработку)
                        list_date_1.append(item_Принят_в_обработку)
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_1_Выруч in table_df[table_df.Неделя_обработку == item_Выруч].Выручка:
                        time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
            elif date_midle > 61:
                for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                    data_tinne = item_Принят_в_обработку.split("-")
                    if data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"] not in list_date:
                        list_date.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                        list_date_1.append(data_tinne[1] + "-" + dict_month[f"{data_tinne[1]}"])
                list_date.sort(reverse=True)
                list_date_1.sort(reverse=True)
                for item_Выруч in list_date:
                    time_list_Выруч = []
                    for item_mounth in dict_month_earth_2022[item_Выруч]:
                        for item_1_Выруч in table_df[table_df.Принят_в_обработку == item_mounth].Выручка:
                            time_list_Выруч.append(item_1_Выруч)
                    midle_rent_Выруч = round((sum(time_list_Выруч)), 1)
                    list_price_for_date.append(midle_rent_Выруч)
    sum_viruchka = '{0:,}'.format(int(sum(list_viruchka))).replace(',', ' ')
    summ = '{0:,}'.format(int(sum(list_prof))).replace(',', ' ')
    summ_val = '{0:,}'.format(int(sum(list_valov))).replace(',', ' ')
    summ_collich = '{0:,}'.format(sum(list_collich)).replace(',', ' ')
    try:
        summ_rentab = round(mean(list_rentab), 1)
    except:
        summ_rentab = 0
    raz_sum_viruchka = int((int(viruchka.replace(" ", "")) - int(sum_viruchka.replace(" ", ""))) / (int(viruchka.replace(" ", "")) / 100))
    raz_sum_prodaj = int((int(prodaj.replace(" ", "")) - int(summ.replace(" ", ""))) / (int(prodaj.replace(" ", "")) / 100))
    raz_sum_valova = int((int(valova.replace(" ", "")) - int(summ_val.replace(" ", ""))) / (int(valova.replace(" ", "")) / 100))
    raz_sum_kollich = int((int(kollich.replace(" ", "")) - int(summ_collich.replace(" ", ""))) / (int(kollich.replace(" ", "")) / 100))
    raz_sum_pocheitt = int((float(pocheitt) - float(summ_rentab)) / (float(pocheitt) / 100))
    return {
        "message": f"{summ}",
        "message1": f"{summ_val}",
        "message2": f"{summ_collich}",
        "message3": f"{summ_rentab}",
        "message4": sum_viruchka,
        "message5": str(raz_sum_viruchka) + "%",
        "message6": str(raz_sum_prodaj) + "%",
        "message7": str(raz_sum_valova) + "%",
        "message8": str(raz_sum_kollich) + "%",
        "message9": str(raz_sum_pocheitt) + "%",
        "message10": list_price_for_date,
        "message11": raz_sum_viruchka,
        "message12": raz_sum_prodaj,
        "message13": raz_sum_valova,
        "message14": raz_sum_kollich,
        "message15": raz_sum_pocheitt,
    }
    



if __name__ == '__main__':
    uvicorn.run(app)
