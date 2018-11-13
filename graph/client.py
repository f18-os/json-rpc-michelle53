# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()

# define node
from node import *
leaf1 = node("leaf1")
leaf2 = node("leaf2")
root = node("root", [leaf1, leaf1, leaf2])

# Execute in server:
print("graph before increment")
root.show()
print('\n')
list = list_creation(root)
# do this increment remotely:
print("graph after increment")
list = server.nop_incrementation( list )

#root = back_to_tree( 'root', list)
root.show()
rpc.close() # Closes the socket 's' also
