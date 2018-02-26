import abc
import json

class Serializable(object):
    __metaclass__ = abc.ABCMeta

    def serialize(self):
        return json.dumps(self.__dict__).encode('utf-8')

class Packet(Serializable):

    def __init__(self, source, dest, msgType, msg):

        self.source = source
        self.dest = dest
        self.type = msgType
        self.message = msg

def json2Packet(jsonString):
    packetInfo = json.loads(jsonString)

    if packetInfo['type'] == 'bpdu':
        packetInfo['message']['id'] = str(packetInfo['message']['id'])
        packetInfo['message']['root'] = str(packetInfo['message']['root'])

    return Packet(packetInfo['source'],
                  packetInfo['dest'],
                  packetInfo['type'],
                  packetInfo['message'])


def makeBdpu(source, dest, root, cost, id):
    bdpuMsg = {'id': str(id), 'root': str(root), 'cost': cost}
    return Packet(source, dest, "bdpu", bdpuMsg)

def makeData(source, dest, id):
    return Packet(source, dest, 'data', {'id': id})
