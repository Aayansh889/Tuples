def palind(r):
    e=len(r)-1
    s=0
    while s<e:
        if r[s]!=r[e]:
            return False
        s+=1
        e-=1
    return True

x=(2,6,7,7,6,3)
if (palind(x)):
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")