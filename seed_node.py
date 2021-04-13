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




def broadcastupdate():
	seed_node.send_to_nodes("Test")


def confirmOriginalSeed():
	pass


#List of preserved logs. Encrypted for public access.
seedHash = ""
data = []

sys.path.insert(0, '..') # Import the files where the modules are located

from Peer2PeerNode import Peer2PeerNode

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

g = geocoder.ip('me')
cords = g.latlng


run = True

key = ""


key = input("Enter private key for node seed: ")


seedHash = (str(cords[0]) + str(cords[1])).replace('.','').replace('-','9')


seed_node = Peer2PeerNode(IP_addres, 8000)

	
seed_node.seedHash = seedHash


time.sleep(1)


seed_node.start()

cmd = ""
while(run):
	time.sleep(1)
	print(seed_node.broadcast)
	if(seed_node.broadcast):
		broadcastupdate()
		seed_node.broadcast = False
	


seed_node.stop()

