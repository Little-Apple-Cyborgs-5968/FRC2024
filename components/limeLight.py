import ntcore

class LimeLight:
    def __init__(self, inst, table = "limelight"):
        self.nt = inst.getTable(table)

    def getNumber(self, val, errorReturn = None):
        return self.nt.getNumber(val, errorReturn)
    
    def getAprilTagData(self, val, errorReturn = None):
        return self.nt.getNumberArray(val, errorReturn)