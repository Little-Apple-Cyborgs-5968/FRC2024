from robotpy_ext.autonomous import StatefulAutonomous, state, timed_state

class Autonomous(StatefulAutonomous):
    MODE_NAME = "THREE_NOTE_MID_NOSTAGE"
    # too slow


    def intialize(self):
        self.intial_called = None

    @timed_state(duration=2, first=True, next_state="fire")
    def start(self):
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="next")
    def fire(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    @timed_state(duration=1, next_state="backup")
    def next(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Intake.pivotOnePosition = -7.5
        self.Intake.pivotTwoPosition = -7.5

    @timed_state(duration=2, next_state="pause")
    def backup(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(self.Intake.intakeInSpeed)
        self.Intake.intakeMotorTwo.set(self.Intake.intakeInSpeed)
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)

    @timed_state(duration=1, next_state="forward")
    def pause(self):
        self.Intake.pivotOnePosition = 0.1
        self.Intake.pivotTwoPosition = 0.1
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)

    @timed_state(duration=2.4, next_state="start2")
    def forward(self):
        self.DriveTrain.robotDrive.driveCartesian(-0.3, 0, 0)

    @timed_state(duration=2, next_state="fire2")
    def start2(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="strafe")
    def fire2(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)

    @timed_state(duration=1, next_state="next2")
    def strafe(self):
        self.DriveTrain.robotDrive.driveCartesian(0, -0.6, 0)

    @timed_state(duration=1, next_state="backup2")
    def next2(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Intake.pivotOnePosition = -7.5
        self.Intake.pivotTwoPosition = -7.5

    @timed_state(duration=2, next_state="lift")
    def backup2(self):
        self.Shooter.shooterMotor.set(0)
        self.Intake.intakeMotorOne.set(self.Intake.intakeInSpeed)
        self.Intake.intakeMotorTwo.set(self.Intake.intakeInSpeed)
        self.DriveTrain.robotDrive.driveCartesian(0.3, 0, 0)

    @timed_state(duration=2, next_state="reverse_strafe")
    def lift(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.pivotOnePosition = 0.1
        self.Intake.pivotTwoPosition = 0.1

    @timed_state(duration=1, next_state="forward2")
    def reverse_strafe(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0.6, 0)

    @timed_state(duration=2.4, next_state="start3")
    def forward2(self):
        self.DriveTrain.robotDrive.driveCartesian(-0.3, 0, 0)

    @timed_state(duration=2, next_state="fire3")
    def start3(self):
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Shooter.shooterMotor.set(self.Shooter.shooterSpeed)

    @timed_state(duration=1, next_state="stop")
    def fire3(self):
        self.Intake.intakeMotorOne.set(-self.Intake.intakeOutSpeed)
        self.Intake.intakeMotorTwo.set(-self.Intake.intakeOutSpeed)


    @timed_state(duration=2)
    def stop(self):
        self.Intake.intakeMotorOne.set(0)
        self.Intake.intakeMotorTwo.set(0)
        self.Shooter.shooterMotor.set(0)
        self.DriveTrain.robotDrive.driveCartesian(0, 0, 0)

    

