from .pop_state import PopState


class Pop:
    def __init__(self, state: PopState, illness_date: int, mask_on: bool, quarantined: bool, age: int, happiness: int):
        self.state = state
        self.illness_date = illness_date
        self.mask_on = mask_on
        self.quarantined = quarantined
        self.age = age
        self.happiness = happiness
