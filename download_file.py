import openpyxl
from list_price import dict_price

def download_file(price, name, Заказать, Цуна):
    try:
        book = openpyxl.Workbook()
        sheet = book.active
        sheet["A1"] = "Период обеспечения 2 мес."
        sheet["A2"] = "Наименование товара"
        sheet["B2"] = "Количество"
        sheet["C2"] = "Себестоимость с доставкой"
        sheet["D2"] = "Сумма заказа, руб."
        list_index = []
        for index_price, item_price in enumerate(price):
            index_sheet = index_price + 3
            list_index.append(index_sheet)
            sheet[f"A{index_sheet}"] = name[index_price]
            number_pro = item_price / dict_price[name[index_price]]
            sheet[f"B{index_sheet}"] = number_pro
            sheet[f"C{index_sheet}"] = dict_price[name[index_price]]
            sheet[f"D{index_sheet}"] = item_price
        ind = list_index[-1] + 1
        sheet[f"A{ind}"] = "Итого:"
        sheet[f"B{ind}"] = Заказать
        sheet[f"D{ind}"] = Цуна
        book.save('Заказ в Китае бланк.xlsx')
        book.close()
        return 'Заказ в Китае бланк.xlsx'
    except Exception as e:
        print(e)