

class Elections:
    def __init__(self, state, last_elections_result=100.0):
        self.state = state
        self.last_elections_result = last_elections_result

    def hold(self):
        all_pops_num = self.state.get_alive_pops_num()
        self.last_elections_result = sum([len(city.pops) * city.get_average_pops_happiness()
                                          for city in self.state.cities]) / all_pops_num
