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


Letter = Message()
Letter.sender = 'Default Sender'
Letter.recipient = 'Default Recipient'
Letter.setBody("")
def main():
    done = True
    while done:
    #   Setting Sender
        Letter.setSender('Ella')
    #   Output Sender
        print(f"The sender is {Letter.sender}")
        Letter.setRecipient('Stephanie')
        print(f"The recipient is {Letter.recipient}")
    #   Message Body
        Letter.appendBody("For Christmas, I would like:")
        Letter.appendBody("New Keyboard Switches")
        Letter.appendBody("A VPC MongoosT-50CM3 Base")
#       String Length checker validation
        Letter.appendBody("A VPC Constellation ALPHA-R, VPC MongoosT-50CM3 Throttle, and VPC Ace Flight Pedals")
        Letter.toString()
            #   Diagnostics
    #   print(Letter.sender)
    #   print(Letter.recipient)
    #   print(f"The final message is {Letter.FinalMessage}")
        done = False

if __name__ == "__main__":
    main()

'''
Test Run Results:
The sender is Ella
The recipient is Stephanie
Error: End of line expected
For Christmas, I would like:
New Keyboard Switches
A VPC MongoosT-50CM3 Base

'''