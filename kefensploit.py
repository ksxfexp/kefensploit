import time
import os
import webbrowser
from pyfiglet import Figlet
from os import name
import string
from random import *
import hashlib


time.sleep(2)
webbrowser.open('https://www.instagram.com/kfsexp/')

time.sleep(2)

f = Figlet(font='roman')
print(f.renderText('ksxfex'))
time.sleep(1)

print("sınırsız yazı yazmak için 01 ")
print("şifre oluşturmak için 02 ")
print("md5 oluşturmak için 03")
 
islm = input("işlem numarasını girin :")

if islm == "01":
    snrsz = input("neyi tekrarliyalım :")    
    while True:
        print(snrsz)
 
if islm == "02":
    print("şifreniz oluşturuyor % 50 ")     
time.sleep(1)
print("şifreniz oluşturuyor % 100 ")     
characters = string.ascii_letters + string.punctuation + string.digits
password = "".join(choice(characters) for x in range(randint(7, 14)))
print(password)

if islm == "03":
    sifr = input("neyi hashliyelim :")
time.sleep(1)
sifrele=hashlib.md5()
sifrele.update(sifr.encode("utf-8"))
cikti=sifrele.hexdigest()
print(cikti)
