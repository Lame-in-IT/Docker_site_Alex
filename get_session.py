from conn_db import postgresql as settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
import pandas as pd
from statistics import mean


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_settings():
    keys = ["pguser", "pgpasswd", "pdhost", "pgport", "pgdb"]
    if not all(key in keys for key in settings.keys()):
        raise Exception("Файл настроек не правельный")
    return get_engine(settings["pguser"],
                      settings["pgpasswd"],
                      settings["pdhost"],
                      settings["pgport"],
                      settings["pgdb"])


def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)()
    return session


def gwet():
    table_df = pd.read_sql(
        "SELECT * FROM market WHERE Принят_в_обработку >= '2022-11-01' AND Принят_в_обработку <= '2022-11-19'", con=get_engine_from_settings())
    list_cat = []
    list_Выручка = []
    list_Количество_товара = []
    for item_Выручка in table_df["Категория_товара"]:
        if item_Выручка not in list_cat:
            list_cat.append(item_Выручка)
    for item in list_cat:
        time_list = []
        for item_1 in table_df[table_df.Категория_товара == f'{item}'].Процент_рентабельности:
            time_list.append(item_1)
        a = round((mean(time_list)), 1)
        list_Выручка.append(a)


if __name__ == '__main__':
    gwet()