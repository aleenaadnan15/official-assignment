#Question num 21:

'''  convert seconds to day, hour, minutes and seconds   '''

seconds = int(input('enter num of seconds = '))

days = seconds / (60 * 60 * 24)
print('seconds into days:' ,days)

hours = seconds / (60 * 60)
print('seconds into hours:' ,hours)

minutes = seconds / (60)
print('seconds into minutes:' ,minutes)