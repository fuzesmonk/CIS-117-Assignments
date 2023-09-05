'''The first thing your program needs to do is to assign variables for your family (last) name and your student ID.
Next your program will generate the values my_id and num_let.
The expression set will be computed and the results displayed.
Before exiting your program will display the current date and time.'''

from datetime import date

LastName = (input("Last Name: "))
StudentID = (input('Student Id: '))

print(LastName, StudentID)
my_id = LastName
my_id = len(my_id)
print(my_id)



for x in StudentID:
    num_let = int(x) + 1

print(f"Num let = {num_let} \n" )

exp1 = round((my_id / 2), 3)
exp2 = my_id % 2
exp3 = 2 + 3 + ... + num_let
exp4 = my_id + num_let
exp5 = abs(num_let - my_id)
exp6 = round(((my_id) / (num_let + 1100)), 3)
exp7 = bool((num_let % num_let) and (my_id * my_id))
exp8 = bool(1 or my_id / 0)
exp9 = round(3.15, 3)

print(f"Date of run: {date.today()}")
print(f"Expression 1: {exp1}")
print(f"Expression 2: {exp2}")
print(f"Expression 3: {exp3}")
print(f"Expression 4: {exp4}")
print(f"Expression 5: {exp5}")
print(f"Expression 6: {exp6}")
print(f"Expression 7: {exp7}")
print(f"Expression 8: {exp8}")
print(f"Expression 9: {exp9}")
