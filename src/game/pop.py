from .pop_state import PopState


class Pop:
    def __init__(self, state: PopState, illness_date: int, mask_on: bool, quarantined: bool, age: int, happiness: int):
        self.state = state
        self.illness_date = illness_date
        self.mask_on = mask_on
        self.quarantined = quarantined
        self.age = age
        self.happiness = happiness

    def apply_modifier(self, modifier):
        if 'all' in modifier:
            self.happiness = self.happiness + modifier['all']
        elif 'wearing_mask' in modifier and self.mask_on:
            self.happiness = self.happiness + modifier['wearing_mask']
        elif 'not_wearing_mask' in modifier and not self.mask_on:
            self.happiness = self.happiness + modifier['not_wearing_mask']
        elif 'young' in modifier and self.age < 50:
            self.happiness = self.happiness + modifier['young']
        elif 'old' in modifier and self.age > 49:
            self.happiness = self.happiness + modifier['old']

    def remove_modifier(self, modifier):
        if 'all' in modifier:
            self.happiness = self.happiness - modifier['all']
        elif 'wearing_mask' in modifier and self.mask_on:
            self.happiness = self.happiness - modifier['wearing_mask']
        elif 'not_wearing_mask' in modifier and not self.mask_on:
            self.happiness = self.happiness - modifier['not_wearing_mask']
        elif 'young' in modifier and self.age < 50:
            self.happiness = self.happiness - modifier['young']
        elif 'old' in modifier and self.age > 49:
            self.happiness = self.happiness - modifier['old']