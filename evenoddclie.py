import xmlrpc.client
proxy=xmlrpc.client.ServerProxy(("http://localhost:8000/"))
n=int(input("enter number"))
print("is even"+(proxy.is_even(n)))
