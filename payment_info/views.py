from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class BeginWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.n_right_guesses = p.participant.vars['n_right_guesses']
            p.payoff_final_wguess = p.n_right_guesses*10 + p.participant.vars['final_pay_off']



class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.participant
        return {
            'redemption_code': participant.label or participant.code,
        }

class Auszahlung_Berechnung(Page):

    pass


page_sequence = [
    BeginWaitPage,
    Auszahlung_Berechnung,
    PaymentInfo]

