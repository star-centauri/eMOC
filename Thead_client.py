import pysftp
import traceback
import socket
import os

from utilities import *
from project import *

def client_receive_project(uri):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    try:
        sftp = pysftp.Connection('bibcegos.nce.ufrj.br', username='bruna_dosvox', password='16048112Teamo', cnopts=cnopts)
        with sftp as s:
            with s.cd('emoc'):
                sftp.get_d(uri, os.getcwd(), preserve_mtime=True)
                with s.cd(uri):
                    return s.listdir()
    except:
        print(traceback.format_exc())
        sftp.close()


def client_sign_up(uri, userName, content):
    fileName = userName+".txt"
    rq2 = json.dumps(content, indent=None, separators=(",", ":"), default=decimal_default)
    try:
        with open(fileName, "w") as f:
            f.write(rq2)
    except Exception as e:
        print("type error: " + str(e))
        return

    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    try:
        sftp = pysftp.Connection('bibcegos.nce.ufrj.br', username='bruna_dosvox', password='16048112Teamo', cnopts=cnopts)
        with sftp as s:
            with s.cd('emoc'):
                with s.cd(uri):
                    s.put(fileName)
    except:
        print(traceback.format_exc())
        sftp.close()

'''
from __future__ import print_function
import sys
import threading
import Pyro4

from subscribe_employee import Colaborador

class ColaborationChatt(object):
    def __init__(self, uri, signUp, layout):
        self.chatbox = Pyro4.core.Proxy(uri)
        self.nick = ''
        self.signUp = signUp
        self.layout = layout
        self.abort = 0

    @Pyro4.expose
    @Pyro4.oneway
    def events(self, nick, events): #parecido com envio de mensagens
        if nick != self.nick:
            print("")

    def inicialization(self, tableEvents):
        for t in tableEvents:
            self.layout.events_group.addLayout(t)

    def start(self):
        self.nick = self.signUp.get_userId()
        self.chatbox.join(self.nick, self)

class DaemonThread(threading.Thread):
    def __init__(self, chatter):
        threading.Thread.__init__(self)
        self.chatter = chatter
        self.setDaemon(True)

    def run(self):
        with Pyro4.core.Daemon() as daemon:
            daemon.register(self.chatter)
            daemon.requestLoop(lambda: not self.chatter.abort)

def client_receive_project(uri):
    factory = Pyro4.Proxy(uri)
    return factory.sendProject()

def client_sign_up(uri, userName):
    factory = Pyro4.Proxy(uri)
    return factory.signUp(userName)

def inicialization_colaboration(uri, signUser, layout):
    chatter = ColaborationChatt(uri, signUser, layout)
    daemonthread = DaemonThread(chatter)
    daemonthread.start()
    chatter.start()

if sys.version_info < (3, 0):
    input = raw_input

uri = input("enter factory server object uri: ").strip()
factory = Pyro4.Proxy(uri)

# create several things.
print("Creating things.")
thing1 = factory.createSomething(1)
thing2 = factory.createSomething(2)
thing3 = factory.createSomething(3)

# interact with them on the server.
print("Speaking stuff.")
thing1.speak("I am the first")
thing2.speak("I am second")
thing3.speak("I am last then...")
'''
