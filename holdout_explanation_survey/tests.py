from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Einfuehrung)
        yield (views.Questionaire, {'social_distance_text' : 'Test'})
