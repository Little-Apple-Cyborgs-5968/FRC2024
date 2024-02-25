import wpilib
import wpilib.drive
from components.drive_train import DriveTrain
from components.shooter import Shooter
from components.climber import Climber
from robot_map import USB
from robotpy_ext.autonomous import AutonomousModeSelector
import ntcore
from components.lime_light import LimeLight


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
        self.components = {"DriveTrain": self.DriveTrain, "Shooter": self.Shooter, "Climber": self.Climber, "LimeLight": self.LimeLight}
        self.auto = AutonomousModeSelector("autonomous", self.components)


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.DriveTrain.autonomousInit()
        self.Shooter.autonomousInit()
        self.Climber.autonomousInit()
        self.auto.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.DriveTrain.autonomousPeriodic()
        self.Shooter.autonomousPeriodic()
        self.Climber.autonomousPeriodic()
        self.auto.periodic()
    
    def disabledInit(self):
        self.auto.disable()

    def teleopInit(self):
        """This function is run once each time the robot enters teleoperated mode."""
        self.DriveTrain.teleopInit()
        self.Shooter.teleopInit()
        self.Climber.teleopInit()
        self.alliance = wpilib.DriverStation.getAlliance()
        self.location = wpilib.DriverStation.getLocation()
        # wpilib.SmartDashboard.getValue()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.DriveTrain.teleopPeriodic()
        self.Shooter.teleopPeriodic()
        self.Climber.teleopPeriodic()
        #if self.LimeLight.getNumber("tv"):
        #    print("target detected")
        #else:
        #    print("no target")
        # print(f"{self.alliance}, {self.location}")
        # wpilib.SmartDashboard.putNumber("david", 4) send transitory value to network tables
    
        


if __name__ == "__main__":
    wpilib.run(MyRobot)
