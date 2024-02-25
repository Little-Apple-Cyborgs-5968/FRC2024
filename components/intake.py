import rev

from robot_map import CAN

class Intake:
    def __init__(self, controller):
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
        self.intakeMotorTwo.setInverted(True)

        self.pivotPIDControllerOne = self.pivotMotorOne.getPIDController()
        self.pivotPIDControllerOne.setP(0.5)
        self.pivotPIDControllerOne.setI(0.0)
        self.pivotPIDControllerOne.setD(1)
        self.pivotPIDControllerOne.setFF(0)
        self.pivotPIDControllerOne.setOutputRange(-0.5, 0.5)
        
        self.pivotPIDControllerTwo.setP(0.5)
        self.pivotPIDControllerTwo.setI(0.0)
        self.pivotPIDControllerTwo.setD(1)
        self.pivotPIDControllerTwo.setFF(0)
        self.pivotPIDControllerTwo.setOutputRange(-0.5, 0.5)

        self.controller = controller

        self.intakeSpeed = 0.35
        
    def autonomousInit(self):
        pass
    
    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        self.pivotEncoderOne.setPosition(0)
        self.pivotEncoderTwo.setPosition(0)
        self.pivotOnePosition = 0
        self.pivotTwoPosition = 0

         # Sets PID values for teleoperated.
        self.pivotPIDControllerOne.setP(0.5)
        self.pivotPIDControllerOne.setI(0.0)
        self.pivotPIDControllerOne.setD(1)
        self.pivotPIDControllerOne.setFF(0)
        self.pivotPIDControllerOne.setOutputRange(-0.5, 0.5)

        self.pivotPIDControllerTwo.setP(0.5)
        self.pivotPIDControllerTwo.setI(0.0)
        self.pivotPIDControllerTwo.setD(1)
        self.pivotPIDControllerTwo.setFF(0)
        self.pivotPIDControllerTwo.setOutputRange(-0.5, 0.5)

    def teleopPeriodic(self):
        # Handles control on the intake motors.
        if self.controller.getPOV() == 180:
            self.intakeMotorOne.set(self.intakeSpeed)
            self.intakeMotorTwo.set(self.intakeSpeed)
        elif self.controller.getPOV() == 0:
            self.intakeMotorOne.set(-self.intakeSpeed)
            self.intakeMotorTwo.set(-self.intakeSpeed)
        else:
            self.intakeMotorOne.set(0)
            self.intakeMotorTwo.set(0)
    
        # Handles control on the pivot motors.
        self.moving = False
        if self.controller.getRightBumper():
            self.pivotOnePosition = self.pivotEncoderOne.getPosition() - 0.25
            self.pivotTwoPosition = self.pivotEncoderTwo.getPosition() - 0.25
            self.moving = True
        elif self.controller.getLeftBumper():
            self.pivotOnePosition = self.pivotEncoderOne.getPosition() + 0.5
            self.pivotTwoPosition = self.pivotEncoderTwo.getPosition() + 0.5
            self.moving = True
        elif self.moving:
            self.pivotOnePosition = self.pivotEncoderOne.getPosition()
            self.pivotTwoPosition = self.pivotEncoderTwo.getPosition()
            self.moving = False

        self.pivotPIDControllerOne.setReference(self.pivotOnePosition, rev.CANSparkMax.ControlType.kPosition)
        self.pivotPIDControllerTwo.setReference(self.pivotTwoPosition, rev.CANSparkMax.ControlType.kPosition)
        print(f"1: {self.pivotEncoderOne.getPosition()} : {self.pivotOnePosition}")
        print(f"2: {self.pivotEncoderTwo.getPosition()} : {self.pivotTwoPosition}")
