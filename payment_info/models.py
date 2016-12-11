from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1
    reward = 5
    cbar = 20

class Subsession(BaseSubsession):

    def before_session_starts(self):
        for p in self.get_players():
            p.payoff = 0



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    n_right_guesses = models.PositiveIntegerField()
    gender = models.CharField(
        choices = [
            "weiblich",
            "männlich",
            "keine Angabe"
        ])
    degree = models.CharField(
        choices = [
            "Abitur",
            "Bachelor",
            "Master",
            "Promotion"
        ])
    econ = models.CharField(
        choices = [
            "Ja",
            "Nein"
        ])
    age =  models.PositiveIntegerField(min = 15, max = 40)
    money = models.PositiveIntegerField()

    #I use the grave mistaes variable in order to aks players whether they intentionally played a dominated action
    grave_mistake = models.BooleanField()
    grave_mistake_on_purpose = models.CharField(
        choices = [
            "Ja",
            "Nein"
        ])
    def set_grave_mistake(self):
        self.grave_mistake = False
        for p in self.in_previous_rounds():
            if p.costs == Constants.cbar and p.message == 0:
                self.grave_mistake = True


