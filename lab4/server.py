import asyncio

USER_LIST = []


class EchoServerClientProtocol(asyncio.Protocol):
    def __init__(self):
        self.transport = None
        self.name = ""

    def connection_made(self, transport):
        peer_name = transport.get_extra_info('peername')
        print('Connection from {}'.format(peer_name))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        if self.name == "":
            self.name = message
            USER_LIST.append(self.name)
        else:
            print('Data received: {!r}'.format(message))
            # print('Send: {!r}'.format(message))
            # self.transport.write(data)

            if message == "ls":
                # print(USER_LIST.__str__().encode())
                print(USER_LIST.__str__().encode())
                self.transport.write(USER_LIST.__str__().encode())

    def connection_lost(self, exc):
        USER_LIST.remove(self.name)


loop = asyncio.get_event_loop()
# Each client connection will create a new protocol instance
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8099)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
