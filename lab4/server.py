import asyncio


async def handle_echo(reader, writer):
    addr = writer.get_extra_info('peername')

    data = await reader.read()
    message = data.decode()
    print("Received %r from %r" % (message, addr))

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.write(data)

    def connection_lost(self, exc):
        print('Connection ended')


loop = asyncio.get_event_loop()
coro = asyncio.start_server(EchoServerClientProtocol, '127.0.0.1', 8099)
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
