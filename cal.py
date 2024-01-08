
'''
        <<---- Creating a Calender ---->>
'''

# Firstly, need to import the module
import calendar


# Manually Input From The User

yy = int(input("Enter a year: "))
mm = int(input("Enter a month: "))

# Then Print The Specific Calender 
print(calendar.month(yy,mm))
