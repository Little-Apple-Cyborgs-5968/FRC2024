from sim.sparksim import CANSparkMax
from wpilib import SPI
from wpilib.drive import MecanumDrive
from navx import AHRS

from robot_map import CAN

class DriveTrain:
    def __init__(self, controller):
        # Intializes motors for the drive basse.
        self.frontRightMotor = CANSparkMax(CAN.frontRightChannel, CANSparkMax.MotorType.kBrushless)
        self.rearRightMotor = CANSparkMax(CAN.rearRightChannel, CANSparkMax.MotorType.kBrushless)
        self.frontLeftMotor = CANSparkMax(CAN.frontLeftChannel, CANSparkMax.MotorType.kBrushless)
        self.rearLeftMotor = CANSparkMax(CAN.rearLeftChannel, CANSparkMax.MotorType.kBrushless)
        self.frontRightMotor.restoreFactoryDefaults()
        self.rearRightMotor.restoreFactoryDefaults()
        self.frontLeftMotor.restoreFactoryDefaults()
        self.rearLeftMotor.restoreFactoryDefaults()
        self.frontRightMotor.setInverted(True)
        self.rearRightMotor.setInverted(True)

        # Sets up the controller and drive train.
        self.controller = controller
        self.robotDrive = MecanumDrive(self.frontLeftMotor, self.rearLeftMotor, self.frontRightMotor,
                                       self.rearRightMotor)
        self.gyroscope = AHRS(SPI.Port.kMXP)
        self.gyroscope.reset()
        
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        # Handles the movement of the drive base.
        self.robotDrive.driveCartesian(
            -self.controller.getLeftY(),
            self.controller.getLeftX(),
            self.controller.getRightX(),
            -self.gyroscope.getRotation2d(),
        )

        if self.controller.getBackButton():
            self.DriveTrain.gyroscope.reset()