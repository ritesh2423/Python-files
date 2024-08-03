import hashlib
d1=input("enter data 1")
d2=input("enter data 2")
hash1 = hashlib.sha256(d1.encode())
hash2 = hashlib.sha256(d2.encode())
o1= hash1.hexdigest()
o2= hash2.hexdigest()
if(o1==o2):
    print("data input have same hash")
    print(o1)
    print(o2)
else:
    print(o1)
    print(o2)
    print("data hash are not same")