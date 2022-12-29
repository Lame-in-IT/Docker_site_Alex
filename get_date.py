from datetime import datetime
from datetime import date, timedelta

def get_date():
    corrent_date_1 = "{:%Y, %m, %d}".format(datetime.now())
    format_date = corrent_date_1.split(",")
    year = int(format_date[0])
    month = int(format_date[1])
    day = int(format_date[2])
    first_date = date(year, month, day)
    duration = timedelta(days=1)
    list_last_day = []
    for d in range(duration.days + 1):
        day = first_date - timedelta(days=d)
        list_last_day.append(day)
    return list_last_day[1]
    
if __name__ == '__main__':
    get_date()