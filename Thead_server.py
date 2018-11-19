import pysftp
import traceback
import socket
import os

from utilities import *
from project import *
from subscribe_employee import Colaborador

class Variables(object):
    project = dict(EMPTY_PROJECT)

class ProjectServerThread(QThread):
    signal = pyqtSignal(dict)

    def __init__(self, pj):
        Variables.project = pj
        self.versaoObservacao = 0
        QThread.__init__(self)

    def run(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((get_ip_address(), 0))

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        nameObservation = "{0}_{1}".format(s.getsockname()[0], self.versaoObservacao)

        try:
            sftp = pysftp.Connection('bibcegos.nce.ufrj.br', username='bruna_dosvox', password='16048112Teamo', cnopts=cnopts)
            with sftp as f:
                with f.cd('emoc'):
                    while f.isdir(nameObservation):
                        self.versaoObservacao = self.versaoObservacao + 1
                        nameObservation = "{0}_{1}".format(s.getsockname()[0], self.versaoObservacao)

                    self.signal.emit({"URL": nameObservation})
                    f.mkdir(nameObservation)
                    with f.cd(nameObservation):
                        cwd = os.getcwd()
                        roteFile = cwd + '\\' + Variables.project["project_name"] + '.boris';
                        f.put(roteFile)
        except:
            print(traceback.format_exc())
            sftp.close()

'''
from __future__ import print_function
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Pyro4
import json
import copy

from subscribe_employee import Colaborador
from utilities import *
from project import *

class Variables(object):
    project = dict(EMPTY_PROJECT)

@Pyro4.expose
class Factory(object):
    def sendProject(self):
        cp_project = copy.deepcopy(Variables.project)
        received = str(json.dumps(dict(cp_project), indent=None, separators=(",", ":"), default=decimal_default))
        return received

    def signUp(self, userName):
        sign = Colaborador(userName)
        self._pyroDaemon.register(sign)
        return sign

    # def createSomething(self, number):
    #     # create a new item
    #     thing = Thingy(number)
    #     # connect it to the Pyro daemon to make it a Pyro object
    #     self._pyroDaemon.register(thing)
    #     # Return it. Pyro's autoproxy feature turns it into a proxy automatically.
    #     # If that feature is disabled, the object itself (a copy) is returned,
    #     # and the client won't be able to interact with the actual Pyro object here.
    #     return thing


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class ChatBox(object):
    def __init__(self):
        self.channels = {}  # registered channels { channel --> (nick, client callback) list }
        self.nicks = []  # all registered nicks on this server

    def getChannels(self):
        return list(self.channels.keys())

    def getNicks(self):
        return self.nicks

    def connect_manager(self, nick):
        if nick in self.nick:
            raise ValueError("Esse nick já existe")
        self.channels[nick] = []
        self.channels[nick].append((nick, ''))
        self.nicks.append(nick)


    def join(self, nick, callback):
        if nick in self.nicks:
            raise ValueError("Esse nick já está em uso.")

        self.channels[nick] = []
        self.channels[nick].append((nick, callback))
        self.nicks.append(nick)
        self.publish(nick, callback.signUp)

    def leave(self, channel, nick):
        if channel not in self.channels:
            print('IGNORED UNKNOWN CHANNEL %s' % channel)
            return
        for (n, c) in self.channels[channel]:
            if n == nick:
                self.channels[channel].remove((n, c))
                break
        self.publish(channel, 'SERVER', '** ' + nick + ' left **')
        if len(self.channels[channel]) < 1:
            del self.channels[channel]
            print('REMOVED CHANNEL %s' % channel)
        self.nicks.remove(nick)
        print("%s LEFT %s" % (nick, channel))

    def publish(self, nick, callback):
        for (n, c) in self.channels[nick][:]:  # use a copy of the list
            try:
                c.inicialization(nick, callback)  # oneway call
            except Pyro4.errors.ConnectionClosedError:
                if (n, c) in self.channels[nick]:
                    self.channels[nick].remove((n, c))

class ProjectServerThread(QThread):
    signal = pyqtSignal(dict)

    def __init__(self, pj):
        Variables.project = pj
        QThread.__init__(self)

    def run(self):
        Pyro4.Daemon.serveSimple({
            Factory: "eMOC.Colaboration"
        }, ns=False)

        Pyro4.config.COMMTIMEOUT = 7200
'''
