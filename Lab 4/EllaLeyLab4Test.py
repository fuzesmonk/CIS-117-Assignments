#Overview: Write a program that models an email message, then a test program to test the email emulator
#Define a message class that includes a sender, recipient, and body
#In the message class, have a constructor with self, sender, and recipient parameters
#Set Values for the sender and recipient
#Set body as an empty string

#An append method w/ self and line parameters.
#Line contains the line of text to add to the body of the message
#Each line should end with a newline character

#A to_string method that returns the string intepretation of the message
#It should include the sender, recipient, and body of the message

#A str_ok method that validates the string parameters

from EllaLeyLab4 import Message

done = True
while done:
    Letter = Message()

#   Setting Sender
    Letter.setSender('Ella')
    check = Letter.str_ok(Letter.sender)
    if check == False:
        break
#   Output Sender
    print(f"The sender is {Letter.sender}")
    Letter.setRecipient('Stephanie')
    check = Letter.str_ok(Letter.recipient)
    if check == False:
        break
    print(f"The recipient is {Letter.recipient}")
#   Message Body
    Letter.setBody("Test Body")
    Letter.appendBody("Hello World")
    Letter.appendBody("Goodbye World")
    ExpectedEntries = 0
    Letter.FinalMessage = [Letter.FinalMessage + line for line in Letter.body]
    print(f"The final message is {Letter.FinalMessage}")
        #   Diagnostics
#   print(Letter.sender)
#   print(Letter.recipient)
#   print(f"The final message is {Letter.FinalMessage}")
    done = False
