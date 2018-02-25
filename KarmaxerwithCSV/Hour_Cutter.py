from Hour_Parser import get_dates

date = get_dates()

def hour_cutter(string):
    new_date = "".join(num for num in string if num.isdigit())
    return new_date

def all_hours():
    hours_ago = []
    for stuff in date:
        time = hour_cutter(stuff)
        hours_ago.append(time)
    return hours_ago