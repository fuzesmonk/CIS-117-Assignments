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



class Message:
    FinalMessage = ""
    def str_ok(self, string):
        StringLength = len(string)
        if StringLength <= 50:
#            Diagnostics
#            print(f"Name: {string}")
            return True
        else:
            print("Error: End of line expected")
            return False

    #All the message parameters
    def setSender(self, sender):
        if self.str_ok(sender):
        #Who is the message's sender
            self.sender = sender

    def setRecipient(self, recipient):
        if self.str_ok(recipient):
        #Who is recieving the message
            self.recipient = recipient

    def setBody(self, body):
        if self.str_ok(body):
    #The main body text of the message
            self.body = body
            FinalMessage = ""

    def appendBody(self, newText):
        if self.str_ok(newText):
            Message.FinalMessage = Message.FinalMessage + newText + '\n'

    def toString(self):
        print(Message.FinalMessage)


