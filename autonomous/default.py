from robotpy_ext.autonomous import StatefulAutonomous, state, timed_state

class Autonomous(StatefulAutonomous):
    MODE_NAME = "DEFAULT"

    def intialize(self):
        self.intial_called = None