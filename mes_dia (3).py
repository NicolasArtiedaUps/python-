def main():
    testYears = [1900, 2000, 2016, 1987]
    testMonths = [2, 2, 1, 11]
    testResults = [28, 29, 31, 30]
    for i in range(len(testYears)):
        yr = testYears[i]
        mo = testMonths[i]
        print(yr, mo, "->", end="")
        result = daysInMonth(yr, mo)
        if result == testResults[i]:
            print("OK")
        else:
            print("Failed")
#end


def isYearLeap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#end

def daysInMonth(year, month):
    bisiesto=isYearLeap(year)
    dias=[]
    aux=1
    if bisiesto==True:
        for i in range(1,12):
            if month==aux:
                dias=[31,29,31,30,31,30,31,31,30,31,30,31]
                return dias[month-1]
            aux=aux+1
    elif bisiesto==False:
        for i in range(1,12):
            if month==aux:
                dias=[31,28,31,30,31,30,31,31,30,31,30,31]
                return dias[month-1]
            aux=aux+1
    else:
       return None
#end
main()
