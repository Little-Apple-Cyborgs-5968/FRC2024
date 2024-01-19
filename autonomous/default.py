from robotpy_ext.autonomous import StatefulAutonomous, state, timed_state

class Autonomous(StatefulAutonomous):
    MODE_NAME = "DEFAULT"

    def intialize(self):
        self.intial_called = None

    @timed_state(duration=1 , first=True)
    def start(self):
        pass