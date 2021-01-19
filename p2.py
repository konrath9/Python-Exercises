print ("Combina 15 números 4 a 4")
num = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
x1=x2=x3=x4=0
for x1 in range (0, 15):
  for x2 in range (x1+1, 15) :
    for x3 in range (x2+1, 15) :
      for x4 in range (x3+1, 15) :
          print (num[x1]," ",num[x2]," ",num[x3]," ",num[x4])