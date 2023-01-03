import multiprocessing
from time import sleep
import os
import webbrowser
import httpx
import re

filesent = ''

def termainal():
  global filesent
  os.system('cls' if os.name == 'nt' else 'clear')
  ip = input("Enter an ip address: ")
  while True:
    option = input("1) Send file\n2) Request a file\n3) See a sent file\n4) Cancel sent file\nEnter your choice: ")
    if option == "1":
      name = input("File name: ")
      file = open("name.txt", "w").write(name)
      print("File sent")
    elif option == "2":
      username = input("Username: ")
      password = input("Password: ")
      file = input("File name: ")
      # req = httpx.get(ip+"/request/"+username+"/"+password+"/"+file)
      # data = req.text
      # data = re.sub("NEWLINECHAR", "\n", data)
      # file = open(file, "w").write(data)
      webbrowser.open(ip+"/request/"+username+"/"+password+"/"+file)
      print("File transfer complete")
    elif option == "3":
      req = httpx.get(ip)
      if req.text != filesent:
        # filesent = req.text
        # req = httpx.get(ip+"/sent")
        # file = open(filesent, "w")
        # file.write(req.text)
        # file.close()
        webbrowser.open(ip+"/sent")
        print("File transfer complete")
      else:
        print("You have the latest sent file")
    elif option == "4":
      file = open("name.txt", "w")
      file.write("")
      file.close()
      print("Cancelled")
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
  

termainal()