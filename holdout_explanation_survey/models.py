from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'holdout_explanation_survey'
    players_per_group = None
    num_rounds = 1
    p = 0.1
    prev = 1 - p
    cbar = 20
    v = 30


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    social_distance_text = models.TextField(max_length = 400)
    def copy_text_toParticipant(self):
        self.participant.vars['text'] = self.social_distance_text
    pass
