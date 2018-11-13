from node import *
import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import ( JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import node
from node import list_creation
@service_class
class ServerServices( object ):

    @request
    def nop_create_list( self, graph ):
        return list_creation( graph )
    @request
    def nop_incrementation( self, list ):
        root = back_to_tree( 'root', list )
        increment( root )
        return list_creation( root )        

ss = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
ss.bind( ( 'localhost', 50001 ) )
ss.listen( 10 )

while True:
    s, _ = ss.accept()
    # JSONRpc object spawns internal thread to serve the connection.
    JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)