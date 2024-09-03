from robotpy_ext.autonomous import StatefulAutonomous, state, timed_state

class Autonomous(StatefulAutonomous):
    MODE_NAME = "RED_ONE_NOTE_STAGE"
    # tx: 7.12 ty: 8.8

    def intialize(self):
        self.intial_called = None

    @timed_state(duration=2, first=True, next_state="fire")
    def start(self):
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="wait")
    def fire(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    # if another member of alliance wants to grab note
    @timed_state(duration=8, next_state="small_back")
    def wait(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)

    @timed_state(duration=0.4, next_state="rotate")
    def small_back(self):
        # self.Intake.pivotOnePosition = -7.5
        # self.Intake.pivotTwoPosition = -7.5
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)
        
    # positive is blue
    @timed_state(duration=0.7, next_state="next")
    def rotate(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0.3)

    @timed_state(duration=1, next_state="backup")
    def next(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)

    @timed_state(duration=2, next_state="pause")
    def backup(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(self.Intake.intakeInSpeed)
        self.Intake.intakeMotorTwo.set(self.Intake.intakeInSpeed)
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)
  
    @timed_state(duration=2)
    def stop(self):
        self.Intake.pivotOnePosition = 0.1
        self.Intake.pivotTwoPosition = 0.1
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
