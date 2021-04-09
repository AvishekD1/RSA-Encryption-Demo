from RSA import encrypt, decrypt, mult_inv, egcd, eugcd, pq

#Reading messages from file to decrypt
f = open("messages.txt", "r")
m = f.read()
a=[]
mA = m.split("$\n")
for i in mA:
    if (i.startswith("A: ")):
        a.append(i[3:len(i)])
f.close()

#read private key from file
f = open("keys.txt", "r")
k = f.read()
kA=""
x = k.split("$\n")
for i in x:
    if (i.startswith("A: ")):
        kA=(i[2:len(i)])
fkA = list(map(int, kA.strip().split()))
f.close()

#Decrypting messages
for i in a:
    dec_msg = decrypt(fkA, i[0:len(i)-1])
    print(dec_msg)

p2=pq()
q2=pq()

#RSA Modulus
n = p2 * q2
print("RSA Modulus(n) is:",n)
 
#Eulers Toitent
r= (p2-1)*(q2-1)
print("Eulers Toitent(r) is:",r)
 
#e Value Calculation
'''FINDS THE HIGHEST POSSIBLE VALUE OF 'e' BETWEEN 1 and 1000 THAT MAKES (e,r) COPRIME.'''
for i in range(1,1000):
    if(egcd(i,r)==1):
        e=i
print("The value of e is:",e)
 
#d, Private and Public Keys
eugcd(e,r)
d = mult_inv(e,r)

print("The value of d is:",d)

public = (e,n)
private = str(d)+" "+str(n)

with open ("keys.txt", 'a') as f1:
  f1.write("B: "+str(private)+"$\n")
f1.close()

print("Private Key is:",private)
print("Public Key is:",public)

#Write encrypted messages to a file
with open ("messages.txt", 'a') as f:
    message=""
    while(message!='exit'):
        message = input("Message: ")
        if (message == "exit"):
          exit()
        enc_msg=encrypt(public,message)
        c=""
        s=""
        for i in enc_msg:
            c=c+str(i)
            s=s+str(i)+","
        print("Your encrypted message is:",c)
        f.write("B: "+s+"$\n")
f.close()