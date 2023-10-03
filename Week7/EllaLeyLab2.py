#Write a program that reads in and validates a filename provided by the user, opens it and reads all of the lines.
#Create a dictionary to hold the line numbers for each valid identifier found.
#Your solution will need to process each line to determine whether a valid identifier exists on that line and if so, record both the line number and identifier found in the dictionary.
#A valid identifier must be a string consisting of only letters, numbers or underscores.
#If a line contains an invalid identifier no record is made in the dictionary.
#If a line contains a valid identifier already recorded in the dictionary append the line number to the dictionary log of where the identifier was found.




#Validate File
def main():
    allowedchars = set("01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
    done = True
    while(done):
        FileName = input("Enter File name \n:")
        try:
            Files = open(FileName, "r", encoding="utf-8")
        except FileNotFoundError:
            print("Not a valid file")
            continue

        Values = {}
        LineNum = 0
        for line in Files:
            LineNum = LineNum + 1
            line = line.rstrip()
            isString = set(line)
            if isString.issubset(allowedchars):
                if line not in Values:
                    Values[line] = []
                Values[line].append(LineNum)
            else:
                continue
        done = False
        print(Values)

if __name__ == "__main__":
    main()

"""Test Run
Enter File name 
:solong
Not a valid file
Enter File name 
:farewell
Not a valid file
Enter File name 
:t2.dat
{'apple': [1, 11], '1': [2, 3], 'ball': [4, 19], 'art': [5], 'dog': [6], 'pen': [8, 21], 'rat': [9], '4': [10], 'carrot': [13], 'orange': [15], 'ant': [16, 17, 18], 'stick': [20], '_': [22], 'goodbye': [25]}


"""