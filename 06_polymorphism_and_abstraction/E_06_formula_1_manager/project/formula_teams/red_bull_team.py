from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def team_data(self):
        expenses = 250000
        sponsors = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
        return expenses, sponsors
