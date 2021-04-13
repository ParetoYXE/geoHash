from client_api import *



Init()





run = True


userName = ""

cmd = ""



print("Welcome to the Node Seed Chat Room")
userName = input("Enter your name for the chat room: ")
Load_Logs()

while(run):
	Load_Logs()
	time.sleep(1)
	Display_Data()
	print("----------------------")
	cmd = input("Enter SEND to send message. Hit enter to refresh")
	if(cmd.upper() == "SEND"):
		message = input("Enter your message: ")
		fullMessage = userName + ":" + message
		Write_to_Logs({"message":"write","data":fullMessage})
	