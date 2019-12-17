from controller.Program import Program
from ui.UI import UI


class Main:

    @staticmethod
    def main():
        program = Program()

        ui = UI(program)
        ui.start()
