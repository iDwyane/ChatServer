
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor

class IphoneChat(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)
        print("clients are %s" % self.factory.clients)


    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        dataStr = data.decode() # 将字节数组转换字符
        a = dataStr.split(":")
        if len(a) > 1:
            comman = a[0]
            content = a[1]
            # return
            msg = ""
            if comman == "iam":
                self.name = content
                msg = self.name + " has joind"
            elif comman == "msg":
                msg = self.name + ":" + content

            print(msg)

    #         for c in self.factory.clients:
    #             c.message(msg)
    #
    # def message(self,message):
    #     self.transport.write(message + "\n")

factory = Factory()
factory.protocol = IphoneChat
factory.clients = []

reactor.listenTCP(12345, factory)
print("Iphone Chat server started")
reactor.run()