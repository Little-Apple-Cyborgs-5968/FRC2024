import wpilib
import wpilib.drive
from components.drive_train import DriveTrain
from robot_map import USB
from robotpy_ext.autonomous import AutonomousModeSelector
import ntcore
from components.limeLight import LimeLight


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """This function is called upon program startup."""
        self.controller = wpilib.XboxController(USB.controller1Channel)
        self.DriveTrain = DriveTrain(self.controller)
        self.components = {"DriveTrain": self.DriveTrain}
        self.auto = AutonomousModeSelector("autonomous", self.components)
        self.inst = ntcore.NetworkTableInstance.getDefault()
        self.inst.startServer()
        self.limeLight = LimeLight(self.inst)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.DriveTrain.autonomousInit()
        self.auto.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        self.DriveTrain.autonomousPeriodic()
        self.auto.periodic()
    
    def disabledInit(self):
        self.auto.disable()

    def teleopInit(self):
        """This function is run once each time the robot enters teleoperated mode."""
        self.DriveTrain.teleopInit()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.DriveTrain.teleopPeriodic()


if __name__ == "__main__":
    wpilib.run(MyRobot)
