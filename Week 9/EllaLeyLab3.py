#This week’s program will perform a data verification of data files,
# throwing an exception if the data input file violates certain conditions.
# If the data file is valid the program will process the data set.

#Reqs
#Verify the file exists
#The data in the file must start with an integer, n
#n is the amount of lines the file must have, throw error if not
#If valid file, first line, and number of lines, get sum of the values

def main():
    done = True
    while(done):
        #Does File Exist
        FileName = input("Enter File Name \n:")
        try:
            FileContent = open(FileName, "r", encoding="utf-8")

        except FileNotFoundError:
            print("Not a valid error")
            continue

        DataSum = 0
        firstline = True
        DataValidation = True
        for line in FileContent:
            try:
                line = int(line)
            except ValueError:
                print("File contains invalid data")
                DataValidation = False
                continue

            #Get expected number of lines
            if firstline == True:
                numberofLines = line
                firstline = False
                lineCount = 0
            else:
                #Add data to the sum
                lineCount = lineCount + 1
                DataSum = DataSum + line
        #Validating Logic
        #print(f"Number of expected lines is {numberofLines}")
        #print(f"Number of lines is {lineCount}")

        #Check if the number of lines matches the expected number of lines
        if DataValidation == True:
            if lineCount < numberofLines:
                print("Error: End of File Expected")
                continue
            elif lineCount > numberofLines:
                print("Error: End of File Expected")
                continue
            elif lineCount == numberofLines:
                print(f"The sum of the data is {DataSum}")
                break
            else:
                continue
        else:
            continue

if __name__ == "__main__":
    main()

'''
Testcase

Enter File Name 
:bad1.dat
Error: End of File Expected
Enter File Name 
:bad2.dat
File contains invalid data
Enter File Name 
:bad3.dat
File contains invalid data
Enter File Name 
:bad4.dat
Error: End of File Expected
Enter File Name 
:good.dat
The sum of the data is 55
'''