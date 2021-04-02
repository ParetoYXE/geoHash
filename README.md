# geoHash

## Proposal for Development
  
  The purpose of GeoHash will be to develop a decentralized Peer to Peer networking operating over TCP Sockets that is tied to a physical internet of things where      "server" nodes running linux on a RaspberryPI will operate as the base infrastructure for the P2P Network but will operate independently and be tied to a unique geolocational hash. The purpose of providing each server node with a unique geolocaitonal hash is to intimatly tie it to the locaiton it was originally generated at on the earth and make sure it is the only one providing routing and seed information for that "region". Regions can be thought as localized rooms who are controlled by the owner of the original server node who posseses limited control over how the room operates, this room is only accessible to individuals falling within the geolocational cooridantes used to generate it creating a form of digital real estate. How users and clients interact with the node is up to the owner. A chat room some form of MMO using the seed as world generator?
For the scope of this project I will be limiting it to several basic features but hypothetically the API/Seed can be expanded for numerous uses. 
  
  
## Use and Operation

  Each server node will communicate on a Peer to Peer network operating over TCP Sockets implemented in Python. Each Server node will broadcast to all other nodes within the network when
                1) It has been created and who controls it (Encrypted Key for ID)
                2) When its Seed has been updated due to user/client engagement

 creating a form of simplified blockchain where all nodes are aware of all other nodes and track their general statues for consistency and confirmation of who owns assets within the network.
 
## The Seed 

  The Seed is essentially what gives each sever node a concept of "value" or "weight" within the network. Each Seed is an encrypted log that is locked both by the original owner of the nodes secret key and the unique GPS coordinates used to initially generate it. This seed will grow in complexity as users interact with the node in the manner specified by the owner. 
  For this initial development the owner will assumed to running an encrypted chat log where the clients remain anonymous and all logs are preserved privetly unless made public by the node owner.
