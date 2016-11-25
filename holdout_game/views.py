from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class BeginWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            # check if the  player plays treatment or controll
            con_first = ((self.round_number == 1) and (player.controll_first))
            con_second = ((self.round_number == 2) and (not player.controll_first))
            player.controll_now = (con_first or con_second)

class message_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['message']
    pass

class message_treatment(Page):
    def is_displayed(self):
       return not self.player.controll_now
    form_model = models.Player
    form_fields = ['message_t']
    pass

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for player in self.group.get_players():
            #save treatment message in message
            if player.message_t == "Ich habe keine Kosten aus der Reform. Du kannst mir vertrauen.":
                player.message = 0
            #save treatment message in message
            if player.message_t == "Die Reform kostet mich 20 Taler. Du kannst mir vertrauen.":
                player.message = 20
        #set pay-offs
        self.group.set_payoffs()
        pass

class guess_controll(Page):
    def is_displayed(self):
       return self.player.controll_now
    form_model = models.Player
    form_fields = ['kompensation_guess']

class guess_treatment(Page):
    def is_displayed(self):
       return not self.player.controll_now
    form_model = models.Player
    form_fields = ['kompensation_guess']

class Results(Page):
    pass

class PrivateInfo(Page):
    pass

class  Erklaerung_controll(Page):
    def is_displayed(self):
         return self.player.controll_now
    pass

class  Erklaerung_treatment(Page):
    def is_displayed(self):
        disp = not self.player.controll_now
        return disp
    pass

class  Einfuehrung(Page):
    pass

#Kontrollfragen

class Kontrollfrage1_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q1']

class Kontrollfrage2_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q2']

class Kontrollfrage3_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q3']

class Kontrollfrage1_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q1']

class Kontrollfrage2_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q2']

class Kontrollfrage3_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q3']

page_sequence = [
    BeginWaitPage,
    Erklaerung_controll,
    Erklaerung_treatment,
    Kontrollfrage1_controll,
    Kontrollfrage2_controll,
    Kontrollfrage3_controll,
    Kontrollfrage1_treatment,
    Kontrollfrage2_treatment,
    Kontrollfrage3_treatment,
    PrivateInfo,
    message_controll,
    message_treatment,
    guess_controll,
    guess_treatment,
    ResultsWaitPage,
    Results
]
