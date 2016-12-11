from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants





class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Einfuehrung(Page):
    pass

class Questionaire(Page):
    def before_next_page(self):
        self.player.copy_text_toParticipant()
    form_model = models.Player
    form_fields = ['social_distance_text']


page_sequence = [
    Einfuehrung,
    Questionaire
]
