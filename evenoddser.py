from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
    return n%2==0
server=SimpleXMLRPCServer(("localhost",8000))
print("listining on port 8000...")
server.register_function(is_even,"is even")
server.serve_forever()
