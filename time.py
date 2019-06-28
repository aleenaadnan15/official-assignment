#Question num 20:

'''  convert all units of time into seconds   '''

years = int(input('enter time in years = '))
months = int(input('enter time in months = '))
weeks = int(input('enter time in weeks = '))
days = int(input('enter time in days = '))
hours = int(input('enter time in hours = '))
mins = int(input('enter time in mins = '))

years = 365 * 24 * 60 * 60 
print('years to sec:' ,years)
months =  30 * 24 * 60 * 60
print('months to sec:' ,months)
weeks = 7 * 24 * 60 * 60
print('weeks to sec:' ,weeks)
days = 24 * 60 * 60
print('days to sec:' ,days)
hours = 60 * 60
print('hours to sec:' ,hours)
mins = 60
print('mins to sec:' ,mins)