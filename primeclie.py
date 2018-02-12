import xmlrpc.client
proxy=xmlrpc.client.ServerProxy("http://localhost:/8000")
n=int(input("enter number"))
if(proxy.prime(n)==0):
    print("number is prime")
else:
    print("number is not prime")
    
