

class Law:
    def __init__(self, name, infection_chance_modifiers, happiness_modifiers, scope, exclusive_with):
        self.name = name
        self.infection_chance_modifiers = infection_chance_modifiers
        self.happiness_modifiers = happiness_modifiers
        self.scope = scope
        self.exclusive_with = exclusive_with
