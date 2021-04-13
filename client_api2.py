#######################################################################################################################
# Author: Liam Iverson                                                                                                #
#                                                                                                                     #
# Initial code base for the seed_node. Used for creating the actual digital asset and maintaining its logs.           #
#                                                                                                                     #
#######################################################################################################################

import sys
import time
import socket

import pygeoip
import geocoder


sys.path.insert(0, '..') # Import the files where the modules are located

from Peer2PeerNodeClient import Peer2PeerNode


#this this should be encrypted and decrypted by the client in a manner that does not expose the IPS publically.
#for now it is blank excluding your own client ip.
nodeMasterIPS = ["127.0.0.1"]

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

#create client node
client_node = Peer2PeerNode(IP_addres, 8002)


g = geocoder.ip('me')
cords = g.latlng

seedHash = (str(cords[0]) + str(cords[1])).replace('.','').replace('-','9')



#THIS IS JUST FOR TESTING. CONNECTS TO LOCAL TEST SEED NODE
nodeMasterIPS.append(IP_addres)
#COMMENT THIS OUT FOR PROPER USE



run = True

def Connect_to_Node(address):
	

	client_node.connect_with_node(address, 8000)
	
	time.sleep(1)
	
	client_node.send_to_nodes({"message":"AUTHLOC", "seed":seedHash})


def Write_to_Logs(data):
	client_node.send_to_nodes(data)


def Disconnect_from_Node():
	client_node.stop()

def Load_Logs():
	client_node.send_to_nodes({"message":"read"})



Connect_to_Node(IP_addres)

Write_to_Logs({"message":"write","data":"hello"})


while(run):
	#Load_Logs()
	time.sleep(10)

Disconnect_from_Node()
