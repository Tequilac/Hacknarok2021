import json

from .law import *
from .law_scope import *


def load_law(file):
    data = json.load(open(file))
    name = data['name']
    scope = LawScope[data['scope']]
    infection_chance_modifiers = data['infection_chance_modifiers']
    happiness_modifiers = data['infection_chance_modifiers']
    return Law(name, infection_chance_modifiers, happiness_modifiers, scope)
