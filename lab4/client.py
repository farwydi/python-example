import asyncio


class Client:

    def __init__(self):
        self.loop = asyncio.get_event_loop()

        self.addr = ''
        self.port = ''

        print("h, help for more info")

    def cmd_reader(self):
        cmd = input('\rEnter cmd: ').lower()

        if len(cmd) > 4 and cmd[:3] == "con" and cmd[4:] == "x":
            payload = cmd[4:].split(":")
            if cmd[4:] == "x":
                payload = ('127.0.0.1', '8099')
            if len(payload) != 2:
                print("addr mast be: 127.0.0.1:8099)")
                return
            self.addr, self.port = payload
            self.loop.run_until_complete(self.connect_to_server())
        elif cmd == "h" or cmd == "help":
            print("con [:addr] - подключится к серверу.")
            print("con x - подключится к 127.0.0.1:8099.")

    async def connect_to_server(self):
        try:
            reader, writer = await asyncio.open_connection(self.addr, self.port,
                                                           loop=self.loop)
            print("Connect successful!")

            name = input('Введите ваше имя: ')
            writer.write(name.encode())

            while True:
                cmd = input('\rEnter cmd: ').lower()

                if len(cmd) > 5 and cmd[:3] == "con":
                    pass
                elif len(cmd) == 2 and cmd[:2] == "lg":
                    pass
                elif len(cmd) == 2 and cmd[:2] == "ls":
                    writer.write("ls".encode())
                    data = await reader.readline()
                    print('Players: %r' % data.decode())
                elif cmd == "h" or cmd == "help":
                    print("ls - Список участников")
                    print("lg - Список доступных игр")
                    print("con [:game name] - подключится к открытой игре")
                else:
                    print("Не верная команда")

        except OSError as e:
            print(e)

    def connect_to_game(self, name: str):
        pass

    def list_of_users(self):
        pass

    def list_of_game(self):
        pass

    def __del__(self):
        self.loop.close()


# async def tcp_echo_client(message):
#     reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
#                                                    loop=self.loop)
#
#     print('Send: %r' % message)
#     writer.write(message.encode())
#
#     data = await reader.read(100)
#     print('Received: %r' % data.decode())
#
#     print('Close the socket')
#     writer.close()


if __name__ == "__main__":
    c = Client()
    while True:
        c.cmd_reader()
