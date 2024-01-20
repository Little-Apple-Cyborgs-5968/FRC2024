import ntcore

class LimeLight:
    def __init__(self, inst, table = "limelight"):
        self.nt = inst.getTable(table)

    def getNumber(self, val, errorReturn = 0):
        return self.nt.getNumber(val, errorReturn)