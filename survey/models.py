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
    ], 





class Group(BaseGroup):
    pass


class Player(BasePlayer):

    consent_form = models.BooleanField(label='Ich habe die Teilnehmebedingungen gelesen und bin mit der Teilnahme einverstanden.', 
        widget=widgets.CheckboxInput,
        blank=False)


    #Demographics
    gender = models.StringField(
    choices=[['Male', 'Mann'], ['Female', 'Frau'], ['Other', 'Divers']],
    label='Welches Geschlecht haben Sie?'
    )
   
    income = models.StringField(
        choices=[['<1000', '<1000€'], ['1000-2000', '1000-2000€'], ['2000-3000', '2000-3000€'], ['3000-4000', '3000-4000€'], ['>4000', '>4000€']],
        label='Wie hoch ist Ihr monatliches Nettoeinkommen?'
    )

    education = models.StringField(
        choices=[
            ['none', 'Kein Schulabschluss'],
            ['hauptschule', 'Hauptschulabschluss'],
            ['realschule', 'Realschulabschluss'],
            ['abitur', 'Abitur'],
            ['university', 'Hochschulabschluss'],
            ['other', 'Sonstiger Abschluss']
        ],
        label='Was ist Ihr höchster Bildungsabschluss?'
    )


    #Important Topics 
    important_topics_tax = models.BooleanField(
        label='Aehnliche Auffassung bei Steuerpolitik',

        widget=widgets.CheckboxInput,
    )
    important_topics_debt = models.BooleanField(
        label='Aehnliche Auffassung wie viele Schulden der Staat haben sollte',

        widget=widgets.CheckboxInput,
    )
    important_topics_integration = models.BooleanField(
        label='Aehnliche Auffassung wie Integration fremder Kulturen funktionieren sollte',
        widget=widgets.CheckboxInput,
    )
    important_topics_family = models.BooleanField(
        label='Aehnliche Auffassung wie Familie stärker gefördert werden sollte',
        widget=widgets.CheckboxInput,
    )

    #Closest Party
    closest_party = models.StringField(
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
        label="In Deutschland sollten Schwangerschaftsabbrüche in allen Bundesländern straffrei möglich und zugänglich sein."
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
    word_count_primer = models.IntegerField(initial=0)

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
    time_after_screener_question = models.StringField()
    time_after_demographics = models.StringField()
    time_after_paypal = models.StringField()

    #paypal
    paypal_email = models.StringField(label='PayPal E-Mail-Adresse:')



# FUNCTIONS
class Subsession(BaseSubsession):

    def creating_session(subsession):
        treatments = itertools.cycle([True, False])
        for player in subsession.get_players():
            player.participant.vars['treatment'] = next(treatments)
            player.participant.vars['progress'] = 1
        
            if player.participant.vars['treatment'] == True:
                player.participant.vars['totalsteps'] = 5
            else:
                player.participant.vars['totalsteps'] = 4



