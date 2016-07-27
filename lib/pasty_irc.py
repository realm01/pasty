from irc.client import Reactor

class IRC():
    def __init__(self, **kwargs):
        self.server = kwargs.get('server')
        self.port = int(kwargs.get('port'))
        self.username = kwargs.get('username')

        self.irc_reactor = Reactor()
    '''
        try:
            self.irc_client = self.irc_reactor.server().connect(self.server, self.port, self.username)
        except ic.ServerConnectionError:
            print('IRC client connection error')
            print(sys.exc_info()[1])

    def __del__(self):
        self.irc_client.quit()
    '''
    def connect(self):
        try:
            self.irc_client = self.irc_reactor.server().connect(self.server, self.port, self.username)
        except ic.ServerConnectionError:
            print('IRC client connection error')
            print(sys.exc_info()[1])

    def disconnect(self):
        self.irc_client.quit()

    def send(self, channel, msg):
        self.connect()
        self.irc_client.privmsg(channel, msg)
        self.disconnect()