def isYearLeap(year):
    if year % 4 != 0 :
        return False;
    elif year % 100 != 0 :
        return True;
    elif year % 400 != 0 :
        return False;
    else :
        return True;

def daysInMonth(year, month):
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31;
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30;
        
    if month == 2 and isYearLeap(year):
        return 29
    else:
        return 28

def dayOfYear(year, month, day):
    if daysInMonth(year, month) >= day and day > 0:
        return True
    else:
        return False
    
print(dayOfYear(2000, 12, 13))