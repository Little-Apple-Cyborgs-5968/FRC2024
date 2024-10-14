import rev

from robot_map import CAN
from wpilib import DigitalInput

class Intake:
    def __init__(self, controller):
        self.limitSwitch = DigitalInput(0)

        # Intializes motor
        self.pivotMotorOne = rev.CANSparkMax(CAN.pivotOneChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.pivotMotorTwo = rev.CANSparkMax(CAN.pivotTwoChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.intakeMotorOne = rev.CANSparkMax(CAN.intakeOneChannel, rev.CANSparkMax.MotorType.kBrushless)
        self.intakeMotorTwo = rev.CANSparkMax(CAN.intakeTwoChannel, rev.CANSparkMax.MotorType.kBrushless)

        self.pivotMotorOne.restoreFactoryDefaults()
        self.pivotMotorTwo.restoreFactoryDefaults()
        self.pivotMotorTwo.setInverted(True)
        self.intakeMotorOne.restoreFactoryDefaults()
        self.intakeMotorTwo.restoreFactoryDefaults()

        self.pivotPIDControllerOne = self.pivotMotorOne.getPIDController()
        self.pivotPIDControllerTwo = self.pivotMotorTwo.getPIDController()

        self.pivotEncoderOne = self.pivotMotorOne.getEncoder()
        self.pivotEncoderTwo = self.pivotMotorTwo.getEncoder()

        self.controller = controller

        self.intakeInSpeed = 0.35
        self.intakeOutSpeed = 0.6
        
    def autonomousInit(self):
        self.pivotEncoderOne.setPosition(0)
        self.pivotEncoderTwo.setPosition(0)
        self.pivotOnePosition = 0
        self.pivotTwoPosition = 0

        self.pivotPIDControllerOne.setP(0.07)
        self.pivotPIDControllerOne.setI(0.0)
        self.pivotPIDControllerOne.setD(1.5)
        self.pivotPIDControllerOne.setFF(0)
        self.pivotPIDControllerOne.setOutputRange(-0.5, 0.5)

        self.pivotPIDControllerTwo.setP(0.07)
        self.pivotPIDControllerTwo.setI(0.0)
        self.pivotPIDControllerTwo.setD(1.5)
        self.pivotPIDControllerTwo.setFF(0)
        self.pivotPIDControllerTwo.setOutputRange(-0.5, 0.5)

    
    def autonomousPeriodic(self):
        self.pivotPIDControllerOne.setReference(self.pivotOnePosition, rev.CANSparkMax.ControlType.kPosition)
        self.pivotPIDControllerTwo.setReference(self.pivotTwoPosition, rev.CANSparkMax.ControlType.kPosition)

    def teleopInit(self):
        self.pivotEncoderOne.setPosition(0)
        self.pivotEncoderTwo.setPosition(0)
        self.pivotOnePosition = 0
        self.pivotTwoPosition = 0

         # Sets PID values for teleoperated.
        self.pivotPIDControllerOne.setP(0.1)
        self.pivotPIDControllerOne.setI(0.0)
        self.pivotPIDControllerOne.setD(1.5)
        self.pivotPIDControllerOne.setFF(0)
        self.pivotPIDControllerOne.setOutputRange(-0.5, 0.5)

        self.pivotPIDControllerTwo.setP(0.1)
        self.pivotPIDControllerTwo.setI(0.0)
        self.pivotPIDControllerTwo.setD(1.5)
        self.pivotPIDControllerTwo.setFF(0)
        self.pivotPIDControllerTwo.setOutputRange(-0.5, 0.5)

    def teleopPeriodic(self):

        self.moving = False

        if not self.limitSwitch.get() and not self.moving:
            self.pivotEncoderOne.setPosition(0)
            self.pivotEncoderTwo.setPosition(0)
            self.pivotOnePosition = 0
            self.pivotTwoPosition = 0

        # Handles control on the intake motors.
        if self.controller.getPOV() == 180:
            self.intakeMotorOne.set(self.intakeInSpeed)
            self.intakeMotorTwo.set(self.intakeInSpeed)
        elif self.controller.getPOV() == 0:
            self.intakeMotorOne.set(-self.intakeOutSpeed)
            self.intakeMotorTwo.set(-self.intakeOutSpeed)
        elif self.controller.getStartButton():
            self.intakeMotorOne.set(-0.4)
            self.intakeMotorTwo.set(-0.15)
        else:
            self.intakeMotorOne.set(0)
            self.intakeMotorTwo.set(0)
    
        # Handles control on the pivot motors. Base on one encoder to ensure spinning together
        if self.controller.getRightBumper():
            self.pivotPIDControllerOne.setP(0.05)
            self.pivotPIDControllerTwo.setP(0.05)
            self.pivotPIDControllerOne.setD(1)
            self.pivotPIDControllerTwo.setD(1)
            print("right bumper")
            #self.pivotOnePosition = self.pivotEncoderTwo.getPosition() - 0.25
            #self.pivotTwoPosition = self.pivotEncoderTwo.getPosition() - 0.25
            self.pivotOnePosition = -7.5
            self.pivotTwoPosition = -7.5
            self.moving = True
        elif self.controller.getLeftBumper():
            self.pivotPIDControllerOne.setP(0.05)
            self.pivotPIDControllerTwo.setP(0.05)
            self.pivotPIDControllerOne.setD(1)
            self.pivotPIDControllerTwo.setD(1)
            print("left bumper")
            #self.pivotOnePosition = self.pivotEncoderTwo.getPosition() + 0.5
            #self.pivotTwoPosition = self.pivotEncoderTwo.getPosition() + 0.5
            self.pivotOnePosition = 0.1
            self.pivotTwoPosition = 0.1
            self.moving = True
        elif self.controller.getPOV() == 90:
            self.pivotPIDControllerOne.setP(0.3)
            self.pivotPIDControllerTwo.setP(0.3)
            self.pivotPIDControllerOne.setD(3)
            self.pivotPIDControllerTwo.setD(3)
            self.pivotOnePosition = -2
            self.pivotTwoPosition = -2
        elif self.moving:
            self.pivotPIDControllerOne.setP(0.05)
            self.pivotPIDControllerTwo.setP(0.05)
            self.pivotPIDControllerOne.setD(1)
            self.pivotPIDControllerTwo.setD(1)
            self.pivotOnePosition = self.pivotEncoderTwo.getPosition()
            self.pivotTwoPosition = self.pivotEncoderTwo.getPosition()
            self.moving = False

        self.pivotPIDControllerOne.setReference(self.pivotOnePosition, rev.CANSparkMax.ControlType.kPosition)
        self.pivotPIDControllerTwo.setReference(self.pivotTwoPosition, rev.CANSparkMax.ControlType.kPosition)
        # print(f"1: {self.pivotEncoderOne.getPosition()} : {self.pivotOnePosition}")
        # print(f"2: {self.pivotEncoderTwo.getPosition()} : {self.pivotTwoPosition}")