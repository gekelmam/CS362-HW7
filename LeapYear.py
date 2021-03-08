def LeapYearfunc(year):
    if(year % 4== 0):
        if ((year % 100) == 0):
            return "Leap Year"
        else:
            return (str(year) + " Is a leap year.")
    else:
        return ("Not a leap year.")