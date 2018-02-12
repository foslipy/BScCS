from xmlrpc.server import SimpleXMLRPCServer

def prime(n):
     f=0
     for i in range(2,n):
         if(n%i==0):
             f=1
             break
         else:
             f=0
         if(f==1):
             return 1
         else:
             return 0

server=SimpleXMLRPCServer(("localhost",8000))
print("listening on port 8000...")
server.register_function(prime,"prime")
server.serve_forever()
