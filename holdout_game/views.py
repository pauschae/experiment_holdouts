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
        #get message from partner
        for p in self.group.get_players():
            p.show = p.get_partner().participant.vars['text']


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


#Question 1 Kontrollgruppe
class Kontrollfrage1_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q1']

class Kontrollfrage1_controll_RightAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now and (self.player.q1 == "Wahr")

class Kontrollfrage1_controll_WrongAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now and (self.player.q1 == "Falsch")


#Question 2 Kontrollgruppe
class Kontrollfrage2_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q2']

class Kontrollfrage2_controll_RightAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now and (self.player.q2 == "Falsch")

class Kontrollfrage2_controll_WrongAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now and (self.player.q2 == "Wahr")


#Question 3 Kontrollgruppe
class Kontrollfrage3_controll(Page):
    def is_displayed(self):
        return self.player.controll_now
    form_model = models.Player
    form_fields = ['q3']

class Kontrollfrage3_controll_RightAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now and (self.player.q3 == "Falsch")

class Kontrollfrage3_controll_WrongAnswer(Page):
    def is_displayed(self):
        return self.player.controll_now  and (self.player.q3 == "Falsch")

#Question 1 Treatment
class Kontrollfrage1_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q1']

class Kontrollfrage1_treatment_RightAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now) and (self.player.q1 == "Wahr")

class Kontrollfrage1_treatment_WrongAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now) and (self.player.q1 == "Falsch")


#Question 2 Treatment
class Kontrollfrage2_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q2']

class Kontrollfrage2_treatment_RightAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now) and (self.player.q2 == "Falsch")

class Kontrollfrage2_treatment_WrongAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now) and (self.player.q2 == "Wahr")


#Question 3 Treatment
class Kontrollfrage3_treatment(Page):
    def is_displayed(self):
        return (not self.player.controll_now)
    form_model = models.Player
    form_fields = ['q3']

class Kontrollfrage3_treatment_RightAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now) and (self.player.q3 == "Falsch")

class Kontrollfrage3_treatment_WrongAnswer(Page):
    def is_displayed(self):
        return (not self.player.controll_now)  and (self.player.q3 == "Falsch")


class otherPlayer(Page):
    pass

page_sequence = [
    BeginWaitPage,
    Erklaerung_controll,
    Erklaerung_treatment,
    Kontrollfrage1_controll,
    Kontrollfrage1_controll_RightAnswer,
    Kontrollfrage1_controll_WrongAnswer,
    Kontrollfrage2_controll,
    Kontrollfrage2_controll_RightAnswer,
    Kontrollfrage2_controll_WrongAnswer,
    Kontrollfrage3_controll,
    Kontrollfrage3_controll_RightAnswer,
    Kontrollfrage3_controll_WrongAnswer,
    Kontrollfrage1_treatment,
    Kontrollfrage1_treatment_RightAnswer,
    Kontrollfrage1_treatment_WrongAnswer,
    Kontrollfrage2_treatment,
    Kontrollfrage2_treatment_RightAnswer,
    Kontrollfrage2_treatment_WrongAnswer,
    Kontrollfrage3_treatment,
    Kontrollfrage3_treatment_RightAnswer,
    Kontrollfrage3_treatment_WrongAnswer,
    otherPlayer,
    PrivateInfo,
    message_controll,
    message_treatment,
    guess_controll,
    guess_treatment,
    ResultsWaitPage
]
