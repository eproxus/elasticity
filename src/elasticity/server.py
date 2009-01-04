from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ElasticityServerProtocol(DatagramProtocol):
    def datagramReceived(self, datagram, address):
        self.transport.write(datagram, address)


def main():
    reactor.listenUDP(8000, ElasticityServerProtocol())
    reactor.run()


if __name__ == '__main__':
    main()
