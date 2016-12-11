from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    def play_round(self):
        control = (self.player.controll_first and self.subsession.round_number == 1) or (not self.player.controll_first and self.subsession.round_number == 2)
        #controll rounds
        if control:
            if self.subsession.round_number == 1:
                yield (views.Erklaerung)
            yield (views.Erklaerung_controll)
            #generate question data
            q1 = random.choice(['wahr', 'falsch'])
            q2 = random.choice(['wahr', 'falsch'])
            q3 = random.choice(['wahr', 'falsch'])

            #q1
            yield (views.Kontrollfrage1_controll, {'q1' : q1})
            if q1 == 'wahr':
                yield (views.Kontrollfrage1_controll_RightAnswer)
            else:
                yield(views.Kontrollfrage1_controll_WrongAnswer)

            #q2
            yield (views.Kontrollfrage2_controll, {'q2' : q2})
            if q2 == 'falsch':
                yield (views.Kontrollfrage2_controll_RightAnswer)
            else:
                yield (views.Kontrollfrage2_controll_WrongAnswer)


            #q3
            yield (views.Kontrollfrage3_controll, {'q3' : q3})
            if q3 == 'falsch':
                yield (views.Kontrollfrage3_controll_RightAnswer)
            else:
                yield (views.Kontrollfrage3_controll_WrongAnswer)

            #going on
            yield(views.otherPlayer)
            yield(views.know_partner, {'know_partner' : 'ja'})
            yield(views.PrivateInfo_controll)
            yield(views.message_controll, {'message_c' : random.choice(['ja', 'nein'])})
            yield(views.guess_controll, {'kompensation_guess' : random.choice(['ja', 'nein']), 'guess_prob': 0.5})
        if not control:
            if self.subsession.round_number == 1:
                yield (views.Erklaerung)
            yield (views.Erklaerung_treatment)
            # generate question data
            q1 = random.choice(['wahr', 'falsch'])
            q2 = random.choice(['wahr', 'falsch'])
            q3 = random.choice(['wahr', 'falsch'])

            # q1
            yield (views.Kontrollfrage1_treatment, {'q1' : q1})
            if q1 == 'wahr':
                yield (views.Kontrollfrage1_treatment_RightAnswer)
            else:
                yield (views.Kontrollfrage1_treatment_WrongAnswer)

            # q2
            yield (views.Kontrollfrage2_treatment, {'q2' : q2})
            if q2 == 'falsch':
                yield (views.Kontrollfrage2_treatment_RightAnswer)
            else:
                yield (views.Kontrollfrage2_treatment_WrongAnswer)

            # q3
            yield (views.Kontrollfrage3_treatment, {'q3' : q3})
            if q3 == 'falsch':
                yield (views.Kontrollfrage3_treatment_RightAnswer)
            else:
                yield (views.Kontrollfrage3_treatment_WrongAnswer)

            # going on
            yield (views.otherPlayer)
            yield (views.know_partner, {'know_partner' : 'ja'})
            yield (views.PrivateInfo_treatment)
            yield (views.message_treatment, {'message_t' : random.choice(["Ich habe keine Kosten aus der Reform. Du kannst mir vertrauen.",
                 "Die Reform kostet mich " + str(Constants.cbar)  + " Taler. Du kannst mir vertrauen."])})
            yield (views.guess_treatment, {'kompensation_guess' : random.choice(['ja', 'nein']), 'guess_prob': 0.5})

        if self.subsession.round_number == 2:
            yield(views.show_message_t)


