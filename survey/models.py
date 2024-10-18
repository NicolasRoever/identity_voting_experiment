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

    age = models.IntegerField(label='Wie alt sind Sie?', min=13, max=125)
    prolific_id = models.CharField(label='Bitte geben Sie hier Ihre Prolific ID ein: ', blank=True)

    consent_form = models.BooleanField(label='Ich habe die Teilnehmebedingungen gelesen und bin mit der Teilnahme einverstanden.', 
        widget=widgets.CheckboxInput,
        blank=False)

    gender = models.StringField(
        choices=[['Male', 'Mann'], ['Female', 'Frau'], ['Other', 'Divers']],
        label='Welches Geschlecht haben Sie?',
        widget=widgets.RadioSelect,
    )
   
    income = models.StringField(
        choices=[['<1000', '<1000€'], ['1000-2000', '1000-2000€'], ['2000-3000', '2000-3000€'], ['3000-4000', '3000-4000€'], ['>4000', '>4000€']],
        label='Wie hoch ist Ihr monatliches Nettoeinkommen?'
    )

    # Define the fields for each survey question
    political_q_1 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Die traditionelle Familie aus Vater, Mutter und Kindern soll stärker als andere Lebensgemeinschaften gefördert werden."
    )
    political_q_2 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Der gesetzliche Mindestlohn soll erhöht werden."
    )
    political_q_3 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Auf hohe Vermögen soll wieder eine Steuer erhoben werden."
    )
    political_q_4 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="In Veröffentlichungen des Landes sollen Schreibweisen, die neben der männlichen und weiblichen auch andere Geschlechtsidentitäten abbilden, verboten werden."
    )
    political_q_5 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Das Land Brandenburg soll Frauenhäuser stärker finanziell unterstützen."
    )
    political_q_6 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Sozialwohnungen sollen vorrangig an Deutsche vergeben werden."
    )
    political_q_7 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Die EU soll sich dafür einsetzen, dass Schwangerschaftsabbrüche in allen Mitgliedstaaten straffrei möglich sind."
    )
    political_q_8 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Mehr Krankenhäuser sollen in öffentlicher Trägerschaft sein."
    )
    political_q_9 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Überschüsse im Bundeshaushalt sollen vorrangig zum Abbau von Schulden eingesetzt werden."
    )

    political_q_10 = models.StringField(
        choices=C.AGREE_OPTIONS,
        label="Empfängerinnen und Empfängern von Bürgergeld, die Jobangebote ablehnen, sollen weiterhin Leistungen gekürzt werden können.."
    )

    slider_taxes = models.IntegerField(blank=True)
    slider_gays = models.IntegerField(blank=True)
    slider_old_people = models.IntegerField(blank=True)


    # Primer

    cultural_primer = models.LongStringField()

    word_count_individual = models.IntegerField()
    word_count_society = models.IntegerField()

    # Political Closeness
    slider_spd = models.IntegerField(blank=True)
    slider_cdu = models.IntegerField(blank=True)
    slider_afd = models.IntegerField(blank=True)

    # Politican Choices

    frohmeier_name = models.StringField(blank=True, initial='')
    frohmeier_statement = models.LongStringField(blank=True, initial='')
    frohmeier_no_statement_choice = models.BooleanField( blank=True)

    muetzenich_name = models.StringField(blank=True)
    muetzenich_statement = models.LongStringField(blank=True)
    muetzenich_no_statement_choice = models.BooleanField( blank=True)

    choice_muetzenich_frohmeier = models.FloatField()
    reason_choice_muetzenich_frohmeier = models.LongStringField()

    wiener_name = models.StringField(blank=True)
    wiener_statement = models.LongStringField(blank=True)
    wiener_no_statement_choice = models.BooleanField(blank=True)

    kraft_name = models.StringField(blank=True, initial='')
    kraft_statement = models.LongStringField(blank=True, initial='')
    kraft_no_statement_choice = models.BooleanField( blank=True)

    choice_kraft_wiener = models.FloatField()
    reason_choice_kraft_wiener = models.LongStringField()

    #Donation Decisions

    donation_afd = models.IntegerField(initial=5)
    donation_cdu = models.IntegerField(initial=5)
    donation_spd = models.IntegerField(initial=5)

    # Mechnanism Question
    issue_1_importance = models.IntegerField(initial=0, blank=True)
    issue_2_importance = models.IntegerField(initial=0, blank=True)
    issue_3_importance = models.IntegerField(initial=0, blank=True)
    issue_4_importance = models.IntegerField(initial=0, blank=True)
    issue_5_importance = models.IntegerField(initial=0, blank=True)
    issue_6_importance = models.IntegerField(initial=0, blank=True)
    issue_7_importance = models.IntegerField(initial=0, blank=True)
    issue_8_importance = models.IntegerField(initial=0, blank=True)
    issue_9_importance = models.IntegerField(initial=0, blank=True)
    issue_10_importance = models.IntegerField(initial=0, blank=True)

    #Experimenter Demand Check
    experiment_purpose = models.LongStringField()

    #Time Spent
    time_after_consent = models.StringField()
    time_after_closeness_to_party = models.StringField()
    time_after_political_opinions = models.StringField()
    time_after_primer = models.StringField()
    time_after_politician_choice_afd_spd = models.StringField()
    time_after_politician_choice_afd_cdu = models.StringField()
    time_after_donation_decisions = models.StringField()
    time_after_mechanism_question = models.StringField()
    time_after_estimation_question = models.StringField()
    time_after_experimenter_demand = models.StringField()
    time_after_demographics = models.StringField()
    time_after_end_of_survey = models.StringField()



# FUNCTIONS


class Subsession(BaseSubsession):

    def creating_session(subsession):
        print("Creating session.")
        treatments = itertools.cycle([True, False])
        for player in subsession.get_players():
            player.participant.vars['treatment'] = next(treatments)
            player.participant.vars['progress'] = 1




