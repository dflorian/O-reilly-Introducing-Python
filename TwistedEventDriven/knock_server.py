from twisted.internet import protocol, reactor


class Knock(protocol.Protocol):
    def dataReceived(self, data):
        data = data.decode()
        print('Client:', data)
        if data.startswith("Knock knock"):
            response = "Who's there?"
        else:
            response = data + " who?"
        print("Server: ", response)
        self.transport.write(response.encode())


class KnockFactory(protocol.Factory):
    """docstring for KnockFactory"protocol.Factory"""
    def buildProtocol(self, addr):
        print("You've reached the factory")
        return Knock()


reactor.listenTCP(8000, KnockFactory())
reactor.run()
