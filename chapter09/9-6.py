from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


multicast_ip = "224.0.0.1"
port =8001

class Multicast(DatagramProtocol):

    def startProtocol(self):
        self.transport.joinGroup(multicast_ip)
        self.transport.write('Notify', (multicast_ip, port))

    def datagramReceived(self, datagram, address):
        print "Datagram %s received from %s" % (repr(datagram), repr(address))
        if datagram == "Notify":
            self.transport.write("Acknowlege", address)


reactor.listenMulticast(port, Multicast(), listenMultiple=True)
reactor.run()
