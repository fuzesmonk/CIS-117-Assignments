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
    body = []
    FinalMessage = ""
    def str_ok(self, string):
        StringLength = len(string)
        if StringLength <= 50:
#            Diagnostics
#            print(f"Name: {string}")
            result = True
        else:
            print("Error: End of line expected")
            result = False
        return result
    #All the message parameters
    def setSender(self, sender):
        #Who is the message's sender
        self.sender = sender

    def setRecipient(self, recipient):
        #Who is recieving the message
        self.recipient = recipient

    def setBody(self, body):
    #The main body text of the message
        self.body = body
        Message.body.append(self.body)

    linecount = 0
    def appendBody(self, newText):
        if Message.linecount == 0:
            self.newText = newText
#           String Components
            Message.body.append(self.newText)
            Message.linecount += 1

        else:
            self.newText = newText
            Message.body.append(self.newText)
        print(f"Appended string = {Message.body}")


