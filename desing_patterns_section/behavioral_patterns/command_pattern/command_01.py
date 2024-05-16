from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Command to turn the light on
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


# Concrete Command to turn the light off
class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


# Receiver class
class Light:
    def on(self):
        print("The light is on")

    def off(self):
        print("The light is off")


# Invoker class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()


# Client code
if __name__ == "__main__":
    # Create receiver
    light = Light()

    # Create commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    # Create invoker
    remote = RemoteControl()

    # Set and execute command to turn the light on
    remote.set_command(light_on)
    remote.press_button()
    remote.press_undo()

    # Set and execute command to turn the light off
    remote.set_command(light_off)
    remote.press_button()
    remote.press_undo()
