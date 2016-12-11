from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class BeginWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.n_right_guesses = p.participant.vars['n_right_guesses']
            p.payoff = p.n_right_guesses*Constants.reward + p.participant.vars['final_pay_off']
            p.money = p.payoff.to_real_world_currency(self.session)
            p.set_grave_mistake()

class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }

class Auszahlung_Berechnung(Page):

    pass

class Questionaire(Page):
    form_model = models.Player
    form_fields = [
        'gender',
        'degree',
        'econ',
        'age'
    ]

class AskMistake(Page):
    def is_displayed(self):
        return self.player.set_grave_mistake()


page_sequence = [
    BeginWaitPage,
    AskMistake,
    Questionaire,
    Auszahlung_Berechnung,
    PaymentInfo]

