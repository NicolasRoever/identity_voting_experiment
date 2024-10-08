from otree.api import * 

class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    AGREE_OPTIONS = [
        ('agree', 'Stimme zu'),
        ('neutral', 'Neutral'),
        ('disagree', 'Stimme nicht zu')
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    crt_bat = models.IntegerField(
        label='''
        A bat and a ball cost 22 dollars in total.
        The bat costs 20 dollars more than the ball.
        How many dollars does the ball cost?'''
    )
    crt_widget = models.IntegerField(
        label='''
        If it takes 5 machines 5 minutes to make 5 widgets,
        how many minutes would it take 100 machines to make 100 widgets?
        '''
    )
    crt_lake = models.IntegerField(
        label='''
        In a lake, there is a patch of lily pads.
        Every day, the patch doubles in size.
        If it takes 48 days for the patch to cover the entire lake,
        how many days would it take for the patch to cover half of the lake?
        '''
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


    # Primer

    cultural_primer_individual = models.LongStringField(blank=True)
    cultural_primer_society = models.LongStringField(blank=True)

    # Politican Choices

    frohmeier_name = models.StringField(blank=True)
    frohmeier_statement = models.LongStringField(blank=True)
    frohmeier_no_statement_choice = models.BooleanField(initial=False, blank=True)

    muetzenich_name = models.StringField(blank=True)
    muetzenich_statement = models.LongStringField(blank=True)
    muetzenich_no_statement_choice = models.BooleanField(initial=False, blank=True)

    choice_muetzenich_frohmeier = models.FloatField(blank=True)
    reason_choice_muetzenich_frohmeier = models.LongStringField(blank=True)

    wiener_name = models.StringField(blank=True)
    wiener_statement = models.LongStringField(blank=True)
    wiener_no_statement_choice = models.BooleanField(initial=False, blank=True)

    kraft_name = models.StringField(blank=True)
    kraft_statement = models.LongStringField(blank=True)
    kraft_no_statement_choice = models.BooleanField(initial=False, blank=True)

    choice_kraft_wiener = models.FloatField(blank=True)
    reason_choice_kraft_wiener = models.LongStringField(blank=True)

    #Donation Decisions

    donation_afd = models.IntegerField(initial=5)
    donation_cdu = models.IntegerField(initial=5)
    donation_spd = models.IntegerField(initial=5)

    # Mechnanism Question
    issue_1_importance = models.IntegerField(initial=0)
    issue_2_importance = models.IntegerField(initial=0)
    issue_3_importance = models.IntegerField(initial=0)
    issue_4_importance = models.IntegerField(initial=0)
    issue_5_importance = models.IntegerField(initial=0)
    issue_6_importance = models.IntegerField(initial=0)
    issue_7_importance = models.IntegerField(initial=0)
    issue_8_importance = models.IntegerField(initial=0)
    issue_9_importance = models.IntegerField(initial=0)
    issue_10_importance = models.IntegerField(initial=0)

    #Experimenter Demand Check
    experiment_purpose = models.LongStringField()



# FUNCTIONS

