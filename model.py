"""Defines a model class to predict basic statistics."""

import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import OneHotEncoder
from typing import Tuple

data = pd.read_csv("prem_data_2021-22.csv")  # reads in the data
encoder = OneHotEncoder()  # init one hot encoder
ohe_home_teams = pd.DataFrame(
    encoder.fit_transform(data[["HomeTeam"]]).toarray(),
    columns=encoder.get_feature_names_out(["HomeTeam"]),
)  # fits the encoded ohe values to the DataFrame
ohe_away_teams = pd.DataFrame(
    encoder.fit_transform(data[["AwayTeam"]]).toarray(),
    columns=encoder.get_feature_names_out(["AwayTeam"]),
)
ohe_home_teams.columns = ohe_home_teams.columns.str.replace(
    "HomeTeam_", ""
)  # remove the prefixes that are auto added
ohe_away_teams.columns = ohe_away_teams.columns.str.replace("AwayTeam_", "")


class Model:
    def __init__(self, hometeam, awayteam):
        """Initializes the teams into the model class."""
        self.hometeam = hometeam  # init home team
        self.awayteam = awayteam  # init away team

    def get_goals(self) -> Tuple[float, float]:
        """Gets FT goals prediction for each team."""
        # prepare the features and targets
        home_features = ohe_home_teams  # fits the encoded ohe values to the DataFrame
        home_targets = data["FTHG"]  # prepare the targets using FTHG data
        away_features = ohe_away_teams
        away_targets = data["FTAG"]

        # train the model for home and away goals
        # init a (Multi-Layer Perceptron Regressor) for the home team
        regr_home = MLPRegressor(
            hidden_layer_sizes=(100,), max_iter=1000
        )  # hidden layer has 100 neurons, training process will stop after 1000 iterations if it hasn't already converged
        regr_home.fit(
            home_features, home_targets
        )  # train the model for home team with features and targets
        regr_away = MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000)
        regr_away.fit(away_features, away_targets)

        # prepare the input for prediction
        home_teams_encoded = (
            [0] * len(ohe_home_teams.columns)
        )  # init list of zeros with the same length as the number of columns in the ohe teams DataFrame
        home_teams_encoded[ohe_home_teams.columns.get_loc(self.hometeam)] = (
            1  # finds index of the column that matches the current home team, sets that element in the list to 1
        )
        home_teams_encoded = pd.DataFrame(
            [home_teams_encoded], columns=ohe_home_teams.columns
        )  # converts the list to a DataFrame with the same column names as the one-hot encoded home teams DataFrame
        away_teams_encoded = [0] * len(ohe_away_teams.columns)
        away_teams_encoded[ohe_away_teams.columns.get_loc(self.awayteam)] = 1
        away_teams_encoded = pd.DataFrame(
            [away_teams_encoded], columns=ohe_away_teams.columns
        )

        # predict the goals for home and away teams
        home_goals = regr_home.predict(
            home_teams_encoded
        )  # use the model to predict the number of goals based on the encoded home team data
        away_goals = regr_away.predict(away_teams_encoded)
        return round(home_goals[0], 2), round(
            away_goals[0], 2
        )  # return the prediction as a tuple

    def get_shots(self) -> Tuple[float, float]:
        """Gets FT shots prediction for each team."""
        # prepare the features and targets
        home_features = ohe_home_teams
        home_targets = data["HS"]  # prepare the targets using HS (Home Shots) data
        away_features = ohe_away_teams
        away_targets = data["AS"]  # prepare the targets using AS (Away Shots) data

        # train the model for home and away goals
        regr_home = MLPRegressor(
            hidden_layer_sizes=(100,), max_iter=1000
        )  # init a MLP model for the home team
        regr_home.fit(
            home_features, home_targets
        )  # train the model for home team with features and targets
        regr_away = MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000)
        regr_away.fit(away_features, away_targets)

        # prepare the input for prediction
        home_teams_encoded = [0] * len(ohe_home_teams.columns)
        home_teams_encoded[ohe_home_teams.columns.get_loc(self.hometeam)] = 1
        home_teams_encoded = pd.DataFrame(
            [home_teams_encoded], columns=ohe_home_teams.columns
        )  # convert to DataFrame and set column names
        away_teams_encoded = [0] * len(ohe_away_teams.columns)
        away_teams_encoded[ohe_away_teams.columns.get_loc(self.awayteam)] = 1
        away_teams_encoded = pd.DataFrame(
            [away_teams_encoded], columns=ohe_away_teams.columns
        )  # convert to DataFrame and set column names

        # predict the shots for home and away teams
        home_shots = regr_home.predict(home_teams_encoded)
        away_shots = regr_away.predict(away_teams_encoded)
        return round(home_shots[0], 2), round(
            away_shots[0], 2
        )  # return the prediction as a tuple

    def get_fouls(self) -> Tuple[float, float]:
        """Gets FT fouls prediction for each team."""
        # prepare the features and targets
        home_features = ohe_home_teams
        home_targets = data["HF"]  # prepare the targets using HF (Home Fouls) data
        away_features = ohe_away_teams
        away_targets = data["AF"]  # prepare the targets using AF (Away Fouls) data

        # train the model for home and away goals
        regr_home = MLPRegressor(
            hidden_layer_sizes=(100,), max_iter=1000
        )  # init a MLP model for the home team
        regr_home.fit(
            home_features, home_targets
        )  # train the model for home team with features and targets
        regr_away = MLPRegressor(hidden_layer_sizes=(100,), max_iter=1000)
        regr_away.fit(away_features, away_targets)

        # prepare the input for prediction
        home_teams_encoded = [0] * len(ohe_home_teams.columns)
        home_teams_encoded[ohe_home_teams.columns.get_loc(self.hometeam)] = 1
        home_teams_encoded = pd.DataFrame(
            [home_teams_encoded], columns=ohe_home_teams.columns
        )  # convert to DataFrame and set column names
        away_teams_encoded = [0] * len(ohe_away_teams.columns)
        away_teams_encoded[ohe_away_teams.columns.get_loc(self.awayteam)] = 1
        away_teams_encoded = pd.DataFrame(
            [away_teams_encoded], columns=ohe_away_teams.columns
        )  # convert to DataFrame and set column names

        # predict the fouls for home and away teams
        home_fouls = regr_home.predict(home_teams_encoded)
        away_fouls = regr_away.predict(away_teams_encoded)
        return round(home_fouls[0], 2), round(
            away_fouls[0], 2
        )  # return the prediction as a tuple
