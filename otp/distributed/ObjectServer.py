from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject

class ObjectServer(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('ObjectServer')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def setName(self, name):
        self.name = name
