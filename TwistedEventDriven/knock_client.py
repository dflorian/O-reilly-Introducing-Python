from twisted.internet import reactor, protocol


class KnockClient(protocol.Protocol):
    """docstring for KnockClient"protocol.Protocol"""
    def connectionMade(self):
        self.transport.write("Knock knock".encode())

    def dataReceived(self, data: str):
        data = data.decode()
        print("response from server:", data)
        if data.startswith("Who's there?"):
            response = "Bob"
            self.transport.write(response.encode())
        else:
            self.transport.loseConnection()
            reactor.stop()


class KnockFactory(protocol.ClientFactory):
    """docstring for KnockFactory"""
    protocol = KnockClient


def main():
    f = KnockFactory()
    reactor.connectTCP("localhost", 8000, f)
    reactor.run()


if __name__ == "__main__":
    main()
