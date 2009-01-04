from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ElasticityClientProtocol(DatagramProtocol):
    strings = [
        "Hello, world!",
        "What a fine day it is.",
        "Bye-bye!"
    ]
    
    def startProtocol(self):
        self.transport.connect('127.0.0.1', 8000)
        self.sendDatagram()
    
    def sendDatagram(self):
        if len(self.strings):
            datagram = self.strings.pop(0)
            self.transport.write(datagram)
        else:
            reactor.stop()

    def datagramReceived(self, datagram, host):
        print 'Datagram received: ', repr(datagram)
        self.sendDatagram()


def main():
    reactor.listenUDP(0, ElasticityClientProtocol())
    reactor.run()


if __name__ == '__main__':
    main()