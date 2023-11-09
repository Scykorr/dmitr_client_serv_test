from socket import socket, AF_INET, SOCK_STREAM


class Client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect(
            (ip, port)
        )

    def connect(self, req):
        try:
            msg = self.cli.recv(1024).decode('utf-8')
        except Exception as e:
            print('ERROR: {0}'.format(
                str(e),
            ))
            msg = ''
            exit()
        if msg == 'YOU ARE CONNECTED!':
            val = self.listen(req)
            return val
        else:
            exit()

    def sender(self, text):
        self.cli.send(text.encode('utf-8'))
        while self.cli.recv(1024).decode('utf-8') != 'getted':
            self.cli.send(text.encode('utf-8'))

    def listen(self, req):
        if req:
            if req == 'disconnect':
                self.sender(req)
                print(self.cli.recv(1024).decode('utf-8'))
                exit()
            else:
                self.sender(req)
                data = json.loads(
                    self.cli.recv(63000).decode('utf-8')
                )
                if data['answer']:
                    print('SERVER ANSWER:\n\t{answ}'.format(
                        answ=data['answer']
                    ))
                    return data['answer']
                elif data['error']:
                    print('SERVER ERROR:\n\t{err}'.format(
                        err=data['error']
                    ))
                    return data['error']