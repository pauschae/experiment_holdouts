import numpy, random
from itertools import compress

from otree.api import (
    models, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'holdout_game'
    players_per_group = 2
    num_rounds = 2
    p = 0.1
    prev = 1 - p
    cbar = 20
    v = 30


class Subsession(BaseSubsession):
    def before_session_starts(self):
        if self.round_number == 1:
            # counterbalance treatments
            n_groups = len(self.get_groups())
            order_list = n_groups * [True] + n_groups * [False]
            order_list = numpy.random.permutation(order_list).tolist()

            # player random variables
            for i, player in enumerate(self.get_players()):
                player.cost = numpy.random.choice([Constants.cbar, 0], 1, replace=False,
                                                  p=[Constants.p, 1 - Constants.p])
                player.controll_first = order_list[i]

            # regroup by treatment
            treatment_first_players = list(compress(range(2 * n_groups), order_list))
            treatment_second_players = list(compress(range(2 * n_groups), [not x for x in order_list]))

            # players cpunt from 1 so I have to add one
            treatment_first_players = [x + 1 for x in treatment_first_players]
            treatment_second_players = [x + 1 for x in treatment_second_players]

            global new_groups_first_players
            new_groups_first_players = list(range(n_groups // 2))

            for i in range(n_groups // 2):
                new_groups_first_players[i] = numpy.random.choice(a=treatment_first_players, size=2,
                                                                  replace=False).tolist()
                treatment_first_players.remove(new_groups_first_players[i][0])
                treatment_first_players.remove(new_groups_first_players[i][1])

            global new_groups_second_players
            new_groups_second_players = list(range(n_groups // 2))

            for i in range(n_groups // 2):
                new_groups_second_players[i] = numpy.random.choice(a=treatment_second_players, size=2,
                                                                   replace=False).tolist()
                treatment_second_players.remove(new_groups_second_players[i][0])
                treatment_second_players.remove(new_groups_second_players[i][1])

            new_groups = new_groups_first_players + new_groups_second_players
            self.set_group_matrix(new_groups)
        else:
            #copy variables from round 1
            for player in self.get_players():
                player.cost = player.in_round(1).cost
                player.controll_first = player.in_round(1).controll_first
            #regroup

            #first
            start = new_groups_second_players[len(new_groups_second_players)-1][1]
            for i in reversed(range(1, len(new_groups_second_players))):
                new_groups_second_players[i][1] = new_groups_second_players[i-1][1]
            new_groups_second_players[0][1] = start

            #second
            start = new_groups_first_players[len(new_groups_first_players)-1][1]
            for i in reversed(range(1, len(new_groups_second_players))):
                new_groups_first_players[i][1] = new_groups_first_players[i-1][1]
            new_groups_first_players[0][1] = start

            #save and regroup
            new_groups = new_groups_first_players + new_groups_second_players
            self.set_group_matrix(new_groups)


class Group(BaseGroup):
    total_costs = models.PositiveIntegerField(max=40, min=0)
    provision = models.BooleanField()

    def set_payoffs(self):
        self.total_costs = sum([p.message for p in self.get_players()])
        self.provision = self.total_costs < Constants.v
        for p in self.get_players():
            # set pay-offs from game
            if self.provision:
                if p.message == Constants.cbar:
                    p.payoff = 20 - p.cost
                elif (p.message == 0) and (self.total_costs == 0):
                    p.payoff = 15 - p.cost
                else:
                    p.payoff = 10 - p.cost
            # set pay-offs from guessing
            partner = p.get_partner()
            if (partner.cost == 0) and (partner.message == 0) and (p.guess == "nein"):
                p.right_guess = True
            if (partner.cost == 0) and (partner.message == 20) and (p.guess == "ja"):
                p.right_guess = True
            else:
                p.right_guess = False
        #calculate overall pay-off in round 2
        if self.round_number == 2:
            for p in self.get_players():
                #choose one round at random
                pay_off_round = random.choice([1,2])
                #save pay-off from that round in participant.vars
                p.participant.vars['final_pay_off'] = p.player_in_round(pay_off_round)
                #count number of right guesse
                p.participant.vars['n_right_guesses'] = 0
                for q in p.player_in_pervious_rounds:
                    p.participant.vars['n_right_guesses'] = p.participant.vars['n_right_guesses'] + int(q.right_guess)

class Player(BasePlayer):
    def get_partner(self):
        return self.get_others_in_group()[0]
    cost = models.PositiveIntegerField(
        choices=[0, Constants.cbar]
    )
    message_t = models.CharField(
        choices=["Ich habe keine Kosten aus der Reform. Du kannst mir vertrauen.",
                 "Die Reform kostet mich 20 Taler. Du kannst mir vertrauen."]
    )
    message = models.PositiveIntegerField(
        choices=[0, Constants.cbar]
    )
    controll_first = models.BooleanField()
    controll_now = models.BooleanField()
    kompensation_guess = models.CharField(
        choices=["ja", "nein"]
    )
    right_guess = models.BooleanField()
    q1 = models.CharField(
        choices=["Wahr", "Falsch"]
    )
    q2 = models.CharField(
        choices=["Wahr", "Falsch"]
    )
    q3 = models.CharField(
        choices=["Wahr", "Falsch"]
    )
    show = models.TextField()