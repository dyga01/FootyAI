#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Names:
# Benedek Kaibas
# Aidan Dyga
# Ethan Nyachae


################################################################################

import time
import sys
from model import Model

################################################################################


# Follow These Directions to Run the Code

# cd source
# source env/bin/activate
# python artifact.py


################################################################################


class FootyAI:
    def __init__(self):
        self.team1 = ""
        self.team2 = ""
        self.teams = [
            "arsenal",
            "aston villa",
            "brentford",
            "brighton",
            "burnley",
            "chelsea",
            "crystal palace",
            "everton",
            "leeds",
            "leicester city",
            "liverpool",
            "manchester city",
            "manchester united",
            "newcastle",
            "norwich city",
            "southampton",
            "tottenham hotspurs",
            "watford",
            "west ham",
            "wolves",
        ]
        self.team_name_mapping = {
            "arsenal": "Arsenal",
            "aston villa": "Aston Villa",
            "brentford": "Brentford",
            "brighton": "Brighton",
            "burnley": "Burnley",
            "chelsea": "Chelsea",
            "crystal palace": "Crystal Palace",
            "everton": "Everton",
            "leeds": "Leeds",
            "leicester city": "Leicester",
            "liverpool": "Liverpool",
            "manchester city": "Man City",
            "manchester united": "Man United",
            "newcastle": "Newcastle",
            "norwich city": "Norwich",
            "southampton": "Southampton",
            "tottenham hotspurs": "Tottenham",
            "watford": "Watford",
            "west ham": "West Ham",
            "wolves": "Wolves",
        }

    def get_teams(self):
        while True:
            self.team1 = input("\nTeam 1: ").lower()
            self.team2 = input("Team 2: ").lower()
            if self.team1 in self.teams and self.team2 in self.teams:
                return self.team1, self.team2
            else:
                print(
                    "\nOne or both of the teams you entered are not in the list of teams."
                )

    def convert_teams(self):
        if not self.team1 or not self.team2:
            raise ValueError("Both team1 and team2 must be non-empty strings")
        return self.team_name_mapping[self.team1], self.team_name_mapping[self.team2]

    @staticmethod
    def determine_winner(team1, team2, goals):
        if goals[0] > goals[1]:
            return team1
        elif goals[1] > goals[0]:
            return team2
        else:
            return "Draw"

    @staticmethod
    def animate_loading():
        chars = "/—\|"
        for char in chars:
            sys.stdout.write("\r" + "loading results..." + char)
            time.sleep(0.1)
            sys.stdout.flush()

    def main(self):
        print(
            "\n************************* Welcome to FootyAI *************************\n"
        )
        print("Predict soccer match statistics from the 2021-22 Premier League Season")
        self.get_teams()
        teams = self.convert_teams()
        model = Model(teams[0], teams[1])
        print("")
        self.animate_loading()
        print("")
        goals = model.get_goals()
        shots = model.get_shots()
        fouls = model.get_fouls()
        winner = self.determine_winner(self.team1, self.team2, goals)
        print(f"\n************ {self.team1} vs. {self.team2} ************\n")
        print(f"Winner: {winner}\n")
        print(f"Goals -> {self.team1}: {goals[0]}, {self.team2}: {goals[1]}\n")
        print(f"Shots -> {self.team1}: {shots[0]}, {self.team2}: {shots[1]}\n")
        print(f"Fouls -> {self.team1}: {fouls[0]}, {self.team2}: {fouls[1]}\n")


if __name__ == "__main__":
    FootyAI().main()
