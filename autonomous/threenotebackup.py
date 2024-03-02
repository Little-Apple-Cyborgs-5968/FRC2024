from robotpy_ext.autonomous import StatefulAutonomous, state, timed_state

class Autonomous(StatefulAutonomous):
    MODE_NAME = "THREENOTEBACKUP"

    def intialize(self):
        self.intial_called = None

    @timed_state(duration=2, first=True, next_state="fire")
    def start(self):
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="next")
    def fire(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    @timed_state(duration=1, next_state="drive")
    def next(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Intake.pivotOnePosition = -7.5
        self.Intake.pivotTwoPosition = -7.5

    @timed_state(duration=1, next_state="lift")
    def drive(self):
        self.Intake.intakeMotorOne.set(self.Intake.intakeInSpeed)
        self.Intake.intakeMotorTwo.set(self.Intake.intakeInSpeed)
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)

    @timed_state(duration=0.7, next_state="drive2")
    def lift(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.pivotOnePosition = 0.1
        self.Intake.pivotTwoPosition = 0.1
    
    @timed_state(duration=1, next_state="start2")
    def drive2(self):
        self.DriveTrain.robotDrive.driveCartesian(-0.3, 0, 0)

    @timed_state(duration=2.5, next_state="fire2")
    def start2(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="stop")
    def fire2(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    @timed_state(duration=0.8, next_state="strafe")
    def stop(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Shooter.shooterMotor.set(0)

    @timed_state(duration=1.75, next_state="strafe_next")
    def strafe(self):
        self.DriveTrain.robotDrive.driveCartesian(0, -0.3, 0)

    @timed_state(duration=1, next_state="strafe_drive")
    def strafe_next(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Intake.pivotOnePosition = -7.5
        self.Intake.pivotTwoPosition = -7.5

    @timed_state(duration=1, next_state="strafe_lift")
    def strafe_drive(self):
        self.Intake.intakeMotorOne.set(self.Intake.intakeInSpeed)
        self.Intake.intakeMotorTwo.set(self.Intake.intakeInSpeed)
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)

    @timed_state(duration=0.7, next_state="strafe_back")
    def strafe_lift(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.pivotOnePosition = 0.1
        self.Intake.pivotTwoPosition = 0.1


    @timed_state(duration=1.9, next_state="strafe_drive2")
    def strafe_back(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0.3, 0)

    @timed_state(duration=1, next_state="strafe_start2")
    def strafe_drive2(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.DriveTrain.robotDrive.driveCartesian(-0.3, 0, 0)

    @timed_state(duration=2, next_state="strafe_fire2")
    def strafe_start2(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="strafe_stop")
    def strafe_fire2(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    @timed_state(duration=1)
    def strafe_stop(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Shooter.shooterMotor.set(0)

