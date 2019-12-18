from controller.Program import Program
from ui.UI import UI


class Main:
    program = Program()
    ui = UI(program)
    ui.start()
