import rev
from wpilib import SmartDashboard
from sim.spark_sim import CANSparkMax

from robot_map import CAN

class Climber:
    def __init__(self, controller, JoystickCtrl):
        # Initialize motors for climbing
        self.climberOneChannel = CANSparkMax(CAN.climberOneChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.climberTwoChannel = CANSparkMax(CAN.climberOneChannel, rev.CANSparkMax.MotorType.kBrushless)
        
        self.climberOneChannel.restoreFactoryDefaults()
        self.climberTwoChannel.restoreFactoryDefaults()

        self.climberOneChannel.setInverted(True)
        self.climberTwoChannel.setInverted(True)

        # Sets up the controller and climber motors
        self.controller = controller
        self.JoystickCtrl = JoystickCtrl

        self.climber_speed = 0.2

del teleopPeriodic(self):
    # Handles the movement of the drive base
    if self.JoystickCtrl:
        # Contract arms
        if self.controller.getYButton(self):
            self.climberOneChannel.set(self.climber_speed)
            self.climberTwoChannel.set(-self.climber_speed)
        # Retract arms
        elif self.controller.getBButton(self):
            self.climberOneChannel.set(-self.climber_speed)
            self.climberTwoChannel.set(self.climber_speed)
        else:
            self.climberOneChannel.set(0)
            self.climberTwoChannel.set(0)
        
