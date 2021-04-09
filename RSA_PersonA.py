from RSA import encrypt, decrypt, mult_inv, egcd, eugcd, pq
 
#Reading messages from file to decrypt
f = open("messages.txt", "r")
m = f.read()
b=[]
mB = m.split("$\n")
for i in mB:
    if (i.startswith("B: ")):
        b.append(i[3:len(i)])
f.close()

#read private key from file
f = open("keys.txt", "r")
k = f.read()
kB=""
x = k.split("$\n")
for i in x:
    if (i.startswith("B: ")):
        kB=(i[2:len(i)])
fkB = list(map(int, kB.strip().split()))
f.close()

#Decrypting messages
for i in b:
    dec_msg = decrypt(fkB, i[0:len(i)-1])
    print(dec_msg)

p1=pq()
q1=pq()

#RSA Modulus
n = p1 * q1
print("RSA Modulus(n) is:",n)
 
#Eulers Toitent
r= (p1-1)*(q1-1)
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

with open ("keys.txt", 'w') as f1:
  f1.write("A: "+str(private)+"$\n")
f1.close()

print("Private Key is:",private)
print("Public Key is:",public)

#Write encrypted messages to a file
with open ("messages.txt", 'w') as f:
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
      f.write("A: "+s+"$\n")
f.close()