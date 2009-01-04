
# Copyright (c) 2001-2004 Twisted Matrix Laboratories.
# See LICENSE for details.


"""
An example client. Run simpleserv.py first before running this.
"""

from twisted.internet import reactor, protocol


class ElasticityClientProtocol(protocol.Protocol):
    """Once connected, send a message, then print the result."""
    
    def connectionMade(self):
        self.transport.write("hello, world!")
    
    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        print "Server said:", data
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print "connection lost"


class ElasticityClientProtocolFactory(protocol.ClientFactory):
    protocol = ElasticityClientProtocol

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


# this connects the protocol to a server runing on port 8000
def main():
    reactor.connectTCP("localhost", 8000, ElasticityClientProtocolFactory())
    reactor.run()


# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
