#Write a program that reads in and validates a filename provided by the user, opens it and reads all of the lines. 

#Create a dictionary to hold the line numbers for each valid identifier found.  
#Your solution will need to process each line to determine whether a valid identifier exists on that line and if so, record both the line number and identifier found in the dictionary.

#A valid identifier must be a string consisting of only letters, numbers or underscores.  
#If a line contains an invalid identifier no record is made in the dictionary. 
#If a line contains a valid identifier already recorded in the dictionary append the line number to the dictionary log of where the identifier was found.



allowedchars = set("01234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")

#Validate File

done = True
while(done):
    FileName = input("Enter File name \n:")
    try:
        Files = open(FileName, "r", encoding="utf-8")
    except FileNotFoundError:
        print("Not a valid file")
        continue

    else:
        ValidData = {}
        line = 0
        done = False
        for lines in Files:
            print(lines.rstrip())
            #lines = lines.rstrip()
            #isString = set(lines)
            #if isString.issubset(allowedchars):
            #    print("True")
            #    ValidData.update({'lines': line})
            #    line = line + 1
            #    print(ValidData)
            #else:
            #    print("False")
            

            




    
