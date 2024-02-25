import rev
from wpilib import SmartDashboard
from sim.spark_sim import CANSparkMax
from wpilib import SPI
from wpilib.drive import MecanumDrive
from navx import AHRS

from robot_map import CAN

class DriveTrain:
    def __init__(self, controller, LimeLight):
        # Intializes motors for the drive basse.
        self.frontRightMotor = CANSparkMax(CAN.frontRightChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.rearRightMotor = CANSparkMax(CAN.rearRightChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.frontLeftMotor = CANSparkMax(CAN.frontLeftChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.rearLeftMotor = CANSparkMax(CAN.rearLeftChannel, rev.CANSparkMax.MotorType.kBrushless)
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
        self.LimeLight = LimeLight
        self.TURN_CONST = 80
        self.DRIVE_CONST = 20
        self.MIN_SPEED = 0.05
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass
        self.putValues()

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
            self.gyroscope.reset()
        if self.controller.getPOV() == 90 and self.LimeLight.getNumber('tv'):
            self.pointAtTarget()
            
        self.putValues()

    def putValues(self):
        SmartDashboard.putNumber("yaw", self.gyroscope.getYaw())
        SmartDashboard.putNumber("frontRightMotor", self.frontRightMotor.get())
        SmartDashboard.putNumber("frontLeftMotor", self.frontLeftMotor.get())
        SmartDashboard.putNumber("rearRightMotor", self.rearRightMotor.get())
        SmartDashboard.putNumber("rearLeftMotor", self.rearLeftMotor.get())

    def pointAtTarget(self):
        '''points toward current limelight target. Returns cursor offset'''
        tx = self.LimeLight.getNumber('tx', 0)
        print(f"tx {tx}")
        if tx > 0:
            self.robotDrive.driveCartesian(0, 0, tx / self.TURN_CONST - self.MIN_SPEED)
        elif tx < 0:
            self.robotDrive.driveCartesian(0, 0, tx / self.TURN_CONST + self.MIN_SPEED)
    
    def driveAtSpeaker(self):
        '''drives toward speaker'''
        tx = self.LimeLight.getNumber('tx', 0)
        if tx > 0:
            turn_speed = -tx / self.TURN_CONST + self.MIN_SPEED
        elif tx < 0:
            turn_speed = -tx / self.TURN_CONST - self.MIN_SPEED
        
        ANGLE = 12
        diff = self.LimeLight.getNumber('ty') - ANGLE
        if diff > 0:
            drive_speed = -diff / self.DRIVE_CONST - self.MIN_SPEED
        elif diff < 0:
            drive_speed = -diff / self.DRIVE_CONST + self.MIN_SPEED
        if abs(tx) > 1 or abs(diff) > 1:
            self.robotDrive.driveCartesian(drive_speed, 0, turn_speed)
        else:
            self.robotDrive.stopMotor()
