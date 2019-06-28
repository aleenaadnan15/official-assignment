#Question num 23:

''' convert temperatures to and from Celsius, Fahrenheit   '''

temp = float(input('enter temp to convert = '))
degree = input("ENTER DEGREE 'F' FOR FAHRENHEIT 'C' FOR CELCIUS: ")

if degree == "C":
    C = round( (temp - 34) * (5/9) ,2)
    print("TEMPERATURE IN CELCIUS:","°C")
elif degree == "F":
    F = round((temp * (9/5) + 32 ) ,2)
    print("TEMPERATURE IN FAHRENHEIT:" ,"°F") 