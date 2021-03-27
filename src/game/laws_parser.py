import json

from .law import *
from .law_scope import *


def load_law(file):
    data = json.load(open(file))
    name = data['name']
    scope = LawScope[data['scope']]
    infection_chance_modifiers = data['infection_chance_modifiers']
    happiness_modifiers = data['infection_chance_modifiers']
    exclusive_with = None
    if 'exclusive_with' in data:
        exclusive_with = data['exclusive_with']
    wearing_mask = None
    if 'wearing_mask' in data:
        wearing_mask = data['wearing_mask']
    return Law(name, infection_chance_modifiers, happiness_modifiers, scope, exclusive_with, wearing_mask)
