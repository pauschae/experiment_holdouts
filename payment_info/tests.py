from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):
        if self.player.grave_mistake:
            yield(views.AskMistake)
        yield(views.Questionaire, {'gender' : 'weiblich', 'age' : 19, 'econ': 'Ja', 'degree' : 'Bachelor'})
        yield(views.Auszahlung_Berechnung)
        yield(views.PaymentInfo)
        pass

