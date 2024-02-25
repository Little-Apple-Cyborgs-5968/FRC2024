import rev
from robot_map import CAN

class Climber:
    def __init__(self, controller):
        # Initialize motors for climbing
        self.climberMotorOne = rev.CANSparkMax(CAN.climberOneChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.climberMotorTwo = rev.CANSparkMax(CAN.climberTwoChannel, rev.CANSparkMax.MotorType.kBrushless)
        
        self.climberMotorOne.restoreFactoryDefaults()
        self.climberMotorTwo.restoreFactoryDefaults()

        # Sets up the controller and climber motors
        self.controller = controller

        self.climber_speed = 0.2

    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Contract arms
        if self.controller.getYButton():
            self.climberMotorOne.set(self.climber_speed)
            self.climberMotorTwo.set(self.climber_speed)
        # Retract arms
        elif self.controller.getBButton():
            self.climberMotorOne.set(-self.climber_speed)
            self.climberMotorTwo.set(-self.climber_speed)
        else:
            self.climberMotorOne.set(0)
            self.climberMotorTwo.set(0)
        