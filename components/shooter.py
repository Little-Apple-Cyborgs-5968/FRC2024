import rev

from robot_map import CAN

class Shooter:
    def __init__(self, controller):
        # Intializes motor
        self.shooterMotor = rev.CANSparkMax(CAN.shooterChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.shooterSpeed = 0.7
        self.controller = controller
        
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Handles the movement of the drive base.
        if self.controller.getXButton():
            self.shooterMotor.set(self.shooterSpeed)
        else:
            self.shooterMotor.set(0)
    
