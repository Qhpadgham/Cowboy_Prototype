__author__ = 'Quin'

class Phase:
    def __init__(self):
        self.DisplayedObjects = ""
        self.InputScheme = ""
        self.EndConditions = ""

    class InputScheme:
        def __init__(self, actor):
            self.options_list = ["Moves", "Skip", "Retreat"]
            self.current_option = 0
            num_moves = len(actor.Moves)

        def change_option(self, input):
            if (input == "up"):
                self.current_option -= 1
            if (input == "down"):
                self.current_option += 1



