import wpilib
from robot_map import USB


class Controller:
    def __init__(self):
        self.JoystickCtrl = False
        if self.JoystickCtrl:
            self.hardware = wpilib.Joystick(USB.controller1Channel)
        else:
            self.hardware= wpilib.XboxController(USB.controller1Channel)
    
    def getLeftY(self):
        if self.JoystickCtrl:
            return self.hardware.getY()
        else:
            return self.hardware.getLeftY()
    
    def getLeftX(self):
        if self.JoystickCtrl:
            return self.hardware.getX()
        else:
            return self.hardware.getLeftX()
    
    def getRightY(self):
        if self.JoystickCtrl:
            return self.hardware.getX()
        else:
            return self.hardware.getRightX()
    
    def getBackButton(self):
        if self.JoystickCtrl:
            return None
        else:
            return self.hardware.getBackButton()
    
    def getLeftBumper(self):
        if self.JoystickCtrl:
            return None
        else:
            return self.hardware.getLeftBumper()
        
    def getLeftBumper(self):
        if self.JoystickCtrl:
            return None
        else:
            return self.hardware.getRightBumper()