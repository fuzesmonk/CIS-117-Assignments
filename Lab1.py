'''The first thing your program needs to do is to assign variables for your family (last) name and your student ID.
Next your program will generate the values my_id and num_let.
The expression set will be computed and the results displayed.
Before exiting your program will display the current date and time.'''

import datetime

lastname = 'Ley'
studentid = 1282149

for x in studentid:
    my_id = my_id + x
    print(my_id)

for lets in lastname:
    num_let = num_let + 1
    print(num_let)

exp1 = my_id / 2
exp2 = my_id % 2
exp3 = 2 + 3 + 4 + num_let
exp4 = my_id + num_let
exp5 = abs(num_let - my_id)
exp6 = (my_id) / (num_let + 1100)
exp7 = (num_let % num_let) and (my_id * my_id)
exp8 = my_id / 0
exp9 = round(3.15, 1)


