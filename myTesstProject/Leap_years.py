year = int(input("Eanter a year to check leap year or not?"'\t'))

if(year%400 == 0) and (year % 100 ==0):
    print("This is leap year",year)
elif (year%4==0)and(year%100 !=0):
    print("This is leap year",year) 
else:
    print("This is not leap year")   