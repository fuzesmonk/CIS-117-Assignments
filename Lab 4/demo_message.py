##
#  Demonstrate the Message class.
#
from CIS_117_Lab7Soln import Message

# Create the message.
wishList = Message("Ann", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("Video games")
wishList.append("World peace")

# Display its contents.
print(wishList.toString())
