from abc import ABC, abstractmethod


# this is command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


#this is Concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class TVOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.on()


class TVOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.off()


#this is Receiver classes
class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class TV:
    def on(self):
        print("TV is on")

    def off(self):
        print("TV is off")


# Invoker class
class RemoteControl:
    def __init__(self):
        self.commands = []

    def register_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()


# Client code
light = Light()
tv = TV()

light_on_command = LightOnCommand(light)
light_off_command = LightOffCommand(light)
tv_on_command = TVOnCommand(tv)
tv_off_command = TVOffCommand(tv)

remote_control = RemoteControl()
remote_control.register_command(light_on_command)
remote_control.register_command(tv_on_command)
remote_control.register_command(light_off_command)
remote_control.register_command(tv_off_command)

remote_control.execute_commands()