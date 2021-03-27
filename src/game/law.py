

class Law:
    def __init__(self, name, infection_chance_modifiers, happiness_modifiers, scope):
        self.name = name
        self.infection_chance_modifiers = infection_chance_modifiers
        self.happiness_modifiers = happiness_modifiers
        self.scope = scope
