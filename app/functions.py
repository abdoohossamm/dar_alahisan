import datetime

def day_in_arabic() -> list:
    now = datetime.datetime.now()
    day = now.strftime("%A")
    days = {
        'Saturday':['السبت',1],
        'Sunday':['الاحد',2],
        'Monday':['الاثنين',3],
        'Tuesday':['الثلاثاء',4],
        'Wednesday':['الاربعاء',5],
        'Thursday':['الخميس',6],
        'Friday':['الجمعة',7],
        }
    for k, v in days.items():
        if day == k:
            return v
    return []