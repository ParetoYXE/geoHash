from p2pnetwork.node import Node


class Peer2PeerNode (Node):


    connectedNodes = []
    seedHash = ""
    dataCube = []
    weight = 0
    broadcast = False
    broadcastId = ""

    # Python class constructor
    def __init__(self, host, port):
        super(Peer2PeerNode, self).__init__(host, port, None)
        print("MyPeer2PeerNode: Started")

    # all the methods below are called when things happen in the network.
    # implement your network node behavior to create the required functionality.

    def outbound_node_connected(self, node):
        print("outbound_node_connected: " + node.id)
        
    def inbound_node_connected(self, node):
        print("inbound_node_connected: " + node.id)

    def inbound_node_disconnected(self, node):
        print("inbound_node_disconnected: " + node.id)

    def outbound_node_disconnected(self, node):
        print("outbound_node_disconnected: " + node.id)

    def node_message(self, node, data):
    
        #print("node_message from " + node.id + ": " + str(data))
        if(data["message"] == "AUTHLOC"):
            if(self.seedHash == data["seed"]):
                self.connectedNodes.append(node.id)
                print("Node in region approved for access")
            else:
                print("Node outside region")

        elif(data["message"] == "write"):
            if(node.id in self.connectedNodes):
                self.dataCube.append(data["data"])
                print("Node write successful")
            else:
                print("Node not approved to write")

        elif(data["message"] == "read"):
            if(node.id in self.connectedNodes):
                self.broadcast = True
                self.broadcastId = node.id
                print("Node read successful")
            else:
                print("Node not approved to read")




    def node_disconnect_with_outbound_node(self, node):
        print("node wants to disconnect with oher outbound node: " + node.id)
        
    def node_request_to_stop(self):
        print("node is requested to stop!")
        