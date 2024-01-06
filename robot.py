import wpilib 
from wpilib.drive import MecanumDrive
from rev import CANSparkMax
from robot_map import USB, CAN
from navx import AHRS

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """This function is called upon program startup."""
        self.controller = wpilib.XboxController(USB.controller1Channel)

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

        self.robotDrive = MecanumDrive(self.frontLeftMotor, self.rearLeftMotor, self.frontRightMotor,
                                       self.rearRightMotor)
        
        self.gyroscope = AHRS(wpilib.SPI.Port.kMXP)
        self.gyroscope.reset()


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass
    
    def disabledInit(self):
        pass

    def teleopInit(self):
        """This function is run once each time the robot enters teleoperated mode."""
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robotDrive.driveCartesian(
            self.controller.getLeftY(),
            self.controller.getLeftX(),
            self.controller.getRightX(),
            self.gyroscope.getRotation2d(),
        )


if __name__ == "__main__":
    wpilib.run(MyRobot)