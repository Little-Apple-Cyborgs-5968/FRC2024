import wpilib
import wpilib.drive
from wpilib import SmartDashboard
from components.drive_train import DriveTrain
from components.shooter import Shooter
from components.climber import Climber
from components.intake import Intake
from components.lime_light import LimeLight
from robot_map import USB
from robotpy_ext.autonomous import AutonomousModeSelector
import ntcore


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """This function is called upon program startup."""

        self.controller= wpilib.XboxController(USB.controllerChannel)
        self.inst = ntcore.NetworkTableInstance.getDefault()
        self.inst.startServer()
        self.LimeLight = LimeLight(self.inst)
        self.DriveTrain = DriveTrain(self.controller, self.LimeLight)
        self.Shooter = Shooter(self.controller)
        self.Climber = Climber(self.controller)
        self.Intake = Intake(self.controller)
        self.components = {"DriveTrain": self.DriveTrain, "Shooter": self.Shooter, "Climber": self.Climber, "Intake": self.Intake, "LimeLight": self.LimeLight}
        self.auto = AutonomousModeSelector("autonomous", self.components)


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.DriveTrain.autonomousInit()
        self.Shooter.autonomousInit()
        self.Climber.autonomousInit()
        self.Intake.autonomousInit()
        self.auto.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.DriveTrain.autonomousPeriodic()
        self.Shooter.autonomousPeriodic()
        self.Climber.autonomousPeriodic()
        self.Intake.autonomousPeriodic()
        self.auto.periodic()
        self.putValues()
    
    def disabledInit(self):
        self.auto.disable()

    def teleopInit(self):
        """This function is run once each time the robot enters teleoperated mode."""
        self.DriveTrain.teleopInit()
        self.Shooter.teleopInit()
        self.Climber.teleopInit()
        self.Intake.teleopInit()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.DriveTrain.teleopPeriodic()
        self.Shooter.teleopPeriodic()
        self.Climber.teleopPeriodic()
        self.Intake.teleopPeriodic()
        self.putValues()
    
    def putValues(self):
        #gyro
        SmartDashboard.putNumber("yaw", self.DriveTrain.gyroscope.getYaw())
        #groundmotors
        SmartDashboard.putNumber("frontRightMotor", self.DriveTrain.frontRightMotor.get())
        SmartDashboard.putNumber("frontLeftMotor", self.DriveTrain.frontLeftMotor.get())
        SmartDashboard.putNumber("rearRightMotor", self.DriveTrain.rearRightMotor.get())
        SmartDashboard.putNumber("rearLeftMotor", self.DriveTrain.rearLeftMotor.get()) 
        #misc motors
        SmartDashboard.putNumber("pivotMotorOne", self.Intake.pivotMotorOne.get())
        SmartDashboard.putNumber("pivotMotorTwo", self.Intake.pivotMotorTwo.get())
        SmartDashboard.putNumber("intakeMotorOne", self.Intake.intakeMotorOne.get())
        SmartDashboard.putNumber("intakeMotorTwo", self.Intake.intakeMotorTwo.get())
        SmartDashboard.putNumber("shooterMotor", self.Shooter.shooterMotor.get())
        SmartDashboard.putNumber("climberMotorOne", self.Climber.climberMotorOne.get())
        SmartDashboard.putNumber("climberMotorTwo", self.Climber.climberMotorTwo.get())
        #alliance
        SmartDashboard.putString("alliance", str(wpilib.DriverStation.getAlliance()))
        if wpilib.DriverStation.getLocation() != None:
            SmartDashboard.putNumber("location", float(wpilib.DriverStation.getLocation()))
        #print("banan") might be importnat
        


if __name__ == "__main__":
    wpilib.run(MyRobot)
