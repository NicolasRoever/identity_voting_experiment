from otree.api import * 
import itertools

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    AGREE_OPTIONS = [
        ('agree', 'Stimme zu'),
        ('neutral', 'Neutral'),
        ('disagree', 'Stimme nicht zu')
    ]



class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consent_form = models.BooleanField(label='Ich habe die Teilnehmebedingungen gelesen und bin mit der Teilnahme einverstanden.', 
        widget=widgets.CheckboxInput,
        blank=False)




    # Primer

    cultural_primer = models.LongStringField()

    word_count_primer = models.IntegerField()

    # Political Closeness
    slider_spd = models.IntegerField()
    slider_cdu = models.IntegerField()
    slider_afd = models.IntegerField()


    #Donation Decisions

    donation_afd = models.IntegerField(initial=5)
    donation_cdu = models.IntegerField(initial=5)
    donation_spd = models.IntegerField(initial=5)


    #Experimenter Demand Check
    experiment_purpose = models.LongStringField()

    #Time Spent
    time_after_consent = models.StringField()
    time_after_closeness_to_party = models.StringField()
    time_after_primer = models.StringField()
    time_after_donation_decisions = models.StringField()
    time_after_end_of_survey = models.StringField()
    time_for_study = models.StringField()



# FUNCTIONS


class Subsession(BaseSubsession):

    def creating_session(subsession):
        print("Creating session.")
        treatments = itertools.cycle([True, False])
        for player in subsession.get_players():
            player.participant.vars['treatment'] = next(treatments)
            player.participant.vars['progress'] = 1




