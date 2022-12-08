import uvicorn
from fastapi import FastAPI, Request, Body, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import psycopg2
import pandas as pd
from statistics import mean

from download_file import download_file
from conn_db import *
from bd_zak import get_zak
from get_session import get_engine_from_settings

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
async def read_item(request: Request):
    return templates.TemplateResponse("zakaz.html", {"request": request})


@app.post("/hello_2")
async def hello_2(data=Body()):
    list_mouth = []
    list_categ = []
    chbox17 = data
    for value_mouth in range(1, 15):
        if chbox17[f"chbox{value_mouth}"] == True:
            list_categ.append(1)
        if chbox17[f"chbox{value_mouth}"] == False:
            list_categ.append(0)
    for value_categ in range(15, 18):
        if chbox17[f"chbox{value_categ}"] == True:
            list_mouth.append(1)
        if chbox17[f"chbox{value_categ}"] == False:
            list_mouth.append(0)
    data_zak = get_zak(list_mouth, list_categ)
    return {
        "number": data_zak[0],
        "number1": data_zak[1],
        "number2": data_zak[2],
        "number3": data_zak[3],
        "number4": data_zak[4],
        "number5": data_zak[5],
        "number6": data_zak[6],
        "number7": data_zak[7],
        "number8": data_zak[8],
        "number9": data_zak[9],
        "number10": data_zak[10],
        "number11": data_zak[11],
        "number12": data_zak[12],
        "number13": data_zak[13],
    }


@app.post("/hello")
async def hello(data=Body()):
    number = '{0:,}'.format(data["number"]).replace(',', ' ')
    number1 = '{0:,}'.format(data["number1"]).replace(',', ' ')
    number2 = '{0:,}'.format(data["number2"]).replace(',', ' ')
    number3 = '{0:,}'.format(data["number3"]).replace(',', ' ')
    number4 = '{0:,}'.format(data["number4"]).replace(',', ' ')
    number5 = '{0:,}'.format(data["number5"]).replace(',', ' ')
    number6 = '{0:,}'.format(data["number6"]).replace(',', ' ')
    number7 = '{0:,}'.format(data["number7"]).replace(',', ' ')
    number8 = '{0:,}'.format(data["number8"]).replace(',', ' ')
    number9 = '{0:,}'.format(data["number9"]).replace(',', ' ')
    number10 = '{0:,}'.format(data["number10"]).replace(',', ' ')
    number11 = '{0:,}'.format(data["number11"]).replace(',', ' ')
    number12 = '{0:,}'.format(data["number12"]).replace(',', ' ')
    number13 = '{0:,}'.format(data["number13"]).replace(',', ' ')
    number14 = '{0:,}'.format(data["number14"]).replace(',', ' ')
    number15 = '{0:,}'.format(data["number15"]).replace(',', ' ')
    Бутылка_SL_05л = [data["number"], "Бутылка SL 0.5л"]
    Бутылка_1л = [data["number1"], "Бутылка 1л"]
    Шейкер_SL_черный = [data["number2"], "Шейкер SL черный"]
    Шейкер_SL_4_цвета = [data["number3"], "Шейкер SL 4 цвета"]
    Полотенце_SL = [data["number4"], "Полотенце SL"]
    Овощечистка_нерж = [data["number5"], "Овощечистка нерж"]
    Планшет_85 = [data["number6"], "Планшет 8,5"]
    Планшет_85_цвет = [data["number7"], "Планшет 8,5 цвет"]
    Планшет_10 = [data["number8"], "Планшет 10"]
    Планшет_12 = [data["number9"], "Планшет 12"]
    Лампа_ночник = [data["number10"], "Лампа ночник"]
    Портмоне = [data["number11"], "Портмоне"]
    Магнитная_лампа_Baseus = [data["number12"], "Магнитная лампа Baseus"]
    Магнит_Baseus = [data["number13"], "Магнит Baseus"]
    Заказать = data["number14"]
    Цуна = data["number15"]
    list_data = [Бутылка_SL_05л[0], Бутылка_1л[0], Шейкер_SL_черный[0],
                 Шейкер_SL_4_цвета[0], Полотенце_SL[0], Овощечистка_нерж[0],
                 Планшет_85[0], Планшет_85_цвет[0], Планшет_10[0], Планшет_12[0],
                 Лампа_ночник[0], Портмоне[0], Магнитная_лампа_Baseus[0],
                 Магнит_Baseus[0]]
    list_data_name = [Бутылка_SL_05л[1], Бутылка_1л[1], Шейкер_SL_черный[1],
                      Шейкер_SL_4_цвета[1], Полотенце_SL[1], Овощечистка_нерж[1],
                      Планшет_85[1], Планшет_85_цвет[1], Планшет_10[1], Планшет_12[1],
                      Лампа_ночник[1], Портмоне[1], Магнитная_лампа_Baseus[1],
                      Магнит_Baseus[1]]
    list_price = []
    list_name = []
    for index, item in enumerate(list_data):
        if item > 0:
            list_price.append(item)
            list_name.append(list_data_name[index])
    download_file(list_price, list_name, Заказать, Цуна)
    return {
        "message": f"{number}",
        "message1": f"{number1}",
        "message2": f"{number2}",
        "message3": f"{number3}",
        "message4": f"{number4}",
        "message5": f"{number5}",
        "message6": f"{number6}",
        "message7": f"{number7}",
        "message8": f"{number8}",
        "message9": f"{number9}",
        "message10": f"{number10}",
        "message11": f"{number11}",
        "message12": f"{number12}",
        "message13": f"{number13}",
        "message14": f"{number14} шт.",
        "message15": f"{number15} руб.",
    }


@app.get('/analiz', response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("analiz.html", {"request": request})


@app.post("/analiz")
async def analiz(data=Body()):
    categ = data["analiz"]
    market = data["analiz1"]
    date = data["analiz2"].replace("-", ".").replace(" ", "").split(".")
    date_old = str(date[2] + "-" + date[1] + "-" + date[0])
    date_new = str(date[5] + "-" + date[4] + "-" + date[3])
    connection = psycopg2.connect(database=POSTGRES_DB, host=POSTGRES_HOST,
                                  port=POSTGRES_PORT, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
    connection.autocommit = True
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
            for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                if item_Принят_в_обработку not in list_date:
                    list_date.append(item_Принят_в_обработку)
                    list_date_1.append(item_Принят_в_обработку.strip())
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
                f"SELECT * FROM market WHERE Принят_в_обработку >= '{date_old}' AND Принят_в_обработку <= '{date_new}' AND Маркетплейс = '{market}'",
                con=get_engine_from_settings())
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
            for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                if item_Принят_в_обработку not in list_date:
                    list_date.append(item_Принят_в_обработку)
                    list_date_1.append(item_Принят_в_обработку.strip())
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
            for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                if item_Принят_в_обработку not in list_date:
                    list_date.append(item_Принят_в_обработку)
                    list_date_1.append(item_Принят_в_обработку.strip())
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
            for item_Принят_в_обработку in table_df["Принят_в_обработку"]:
                if item_Принят_в_обработку not in list_date:
                    list_date.append(item_Принят_в_обработку)
                    list_date_1.append(item_Принят_в_обработку.strip())
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
    summ = '{0:,}'.format(int(sum(list_prof))).replace(',', ' ')
    summ_val = '{0:,}'.format(int(sum(list_valov))).replace(',', ' ')
    summ_collich = '{0:,}'.format(sum(list_collich)).replace(',', ' ')
    try:
        summ_rentab = round(mean(list_rentab), 1)
    except:
        summ_rentab = 0
    list_date_1.sort(reverse=True)
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
    }


if __name__ == '__main__':
    uvicorn.run(app)
