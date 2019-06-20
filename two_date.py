import datetime

Current_Date = datetime.datetime.now()
Previous_Date = datetime.datetime(1995, 11, 15, 2,27,45,198765)

print("CURRENT DATE :", Current_Date)
print("MY BIRTH DATE :", Previous_Date)

No_Of_Days = Current_Date - Previous_Date 
print("I AM", No_Of_Days.days, "DAYS OLD")
print("\n************************************\n")