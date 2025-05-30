from typing import Optional

from project import MercedesTeam
from project import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: Optional[RedBullTeam] = None
        self.mercedes_team: Optional[MercedesTeam] = None

    @property
    def team_name(self):
        allowed_team_names = ["Red Bull", "Mercedes"]
        return allowed_team_names

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        allowed_names = self.team_name
        if team_name not in allowed_names:
            raise ValueError("Invalid team name!")
        if team_name == allowed_names[0]:
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == allowed_names[1]:
            self.mercedes_team = MercedesTeam(budget)
        return f"{team_name} has joined the new F1 season."

    #   if team_name == "Red Bull":
    #        self.red_bull_team = RedBullTeam(budget)

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception("Not all teams have registered for the season.")

        winner = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{winner} is ahead at the {race_name} race.")
