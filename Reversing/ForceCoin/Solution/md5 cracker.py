import hashlib
import threading
from itertools import combinations, combinations_with_replacement,product

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','-',' ','*','#','@','!','&','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#letters = ['-',' ','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','%','!','#','$','&','*','|','/','@']
result = '2d3114bcc2e5c58bbac77f04237723d9'.upper()
comb = product(letters, repeat=4)
def find():
    j=0
    for c in comb:
        pin = ''.join(c)
        j+=1
        if(j==10000):
            print('mil - '+pin[0])
            j=0
        text= pin

        for i in range(20):
            text = str(hashlib.md5(bytes(text,'ascii')).hexdigest()).replace('-','').upper()

        if(text==result):
            print("correct pin "+pin)
            return True
    
'''threads=[]
for i in range(14,16):
    threads.append(threading.Thread(target=find, args=(letters[i],), daemon=True))
for i in range(len(threads)):   
    threads[i].start()
for i in range(len(threads)):   
    threads[i].join()'''
find()
#5cRt

