from otree.api import *
import itertools
import time
import random
from datetime import datetime

from .python_functions import count_words_in_string, apply_screener_criterion, calculate_time_spent


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent_form']
    def before_next_page(self):
        self.player.time_after_consent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")



class EndOfSurvey(Page):
    pass



    #Screener Questions
class ScreenerQuestion(Page):
    form_model = 'player'


    def get_form_fields(player):
        form_fields = ['political_q_2', 'political_q_3', 'political_q_6', 'political_q_7']
        random.shuffle(form_fields)
        return form_fields


    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_screener_question = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.participant.part_of_main_sample = apply_screener_criterion(self.player.political_q_6, self.player.political_q_7)



class DonationDecisions(Page):
    form_model = 'player'
    form_fields = ['donation_afd', 'donation_cdu', 'donation_spd']


    def error_message(self, values):

        if values["donation_afd"] + values["donation_cdu"] + values["donation_spd"] > 15:
            return "Sie können maximal 15 Euro spenden."
        
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_donation_decisions = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def vars_for_template(self):
        # Define the sliders and shuffle them
        sliders = [
            {'name': 'donation_spd', 'label': 'SPD', 'for': 'id_donation_spd', 'id': 'donation_spd', 'value': 5},
            {'name': 'donation_cdu', 'label': 'CDU', 'for': 'id_donation_cdu', 'id': 'donation_cdu', 'value': 5},
            {'name': 'donation_afd', 'label': 'AfD', 'for': 'id_donation_afd', 'id': 'donation_afd', 'value': 5},
        ]
        random.shuffle(sliders)  # Randomize the order for each player

        return {
            'sliders': sliders,
            'progress_percentage': self.participant.progress / 8 * 100
        }
    




class PrimerTreatment(Page):
    form_model = 'player'
    form_fields = ['cultural_primer']

    template_name = 'global/Primer.html'

    def vars_for_template(self):
        return {
            'picture_path': 'images/CSD.jpeg',
            'picture_description': "Christopher Street Day 2023 in Köln", 
            'question_primer': "Welche Emotionen verbinden Sie mit dem Christopher Street Day? Wie wichtig halten Sie den Christopher Street Day für unsere Gesellschaft?",
            'question_society': "Wie wichtig sind ihrer Meinung nach Veranstaltungen wie der Christopher Street Day für unsere Gesellschaft?", 
            'text_event_description': "Der Christopher Street Day findet jährlich in vielen Städten statt. Er erinnert an die Stonewall-Aufstände von 1969, die den Beginn der modernen LGBTQ+-Bewegung markieren. Der Politiker Karl Mandl  (CDU) beschreibt das Fest in Köln so: 'Köln steht für Selbstbewusstsein und Toleranz. Mit dem CSD feiert sich die Stadt daher auch selbst. Es ist mir eine Herzensangelegenheit, an diesem fröhlichen und friedlichen Fest teilnehmen zu können.'",
            'progress_percentage': self.participant.progress / 8 * 100
        }
    
    @staticmethod
    def live_method(player, data):

        if data.get('formfieldName') == 'cultural_primer':
            words_in_primer = count_words_in_string(data.get('input', ''))
            player.word_count_primer = words_in_primer


    def is_displayed(player):
        return player.participant.treatment == True 
    

    def error_message(self, values):
        words_in_primer = count_words_in_string(values['cultural_primer'])
        self.player.word_count_primer = words_in_primer
        if words_in_primer < 20:
            return "Bitte schreiben Sie mindestens 20 Wörter."
    
    
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_primer = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
 

class ClosenessToParty(Page):
    form_model = 'player'
    form_fields = ['slider_spd', 'slider_cdu', 'slider_afd']

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_closeness_to_party = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.player.time_for_study = calculate_time_spent(start_time_str=self.player.time_after_consent, end_time_str=self.player.time_after_closeness_to_party)


    def vars_for_template(self):
        sliders = [
            {'name': 'slider_spd', 'label': 'SPD'},
            {'name': 'slider_cdu', 'label': 'CDU'},
            {'name': 'slider_afd', 'label': 'AfD'},
        ]
        random.shuffle(sliders)

        return {
            'progress_percentage': self.participant.progress / 8 * 100,
            'sliders': sliders
        }
    

class PayPal(Page):
    form_model = 'player'
    form_fields = ['paypal_email']




page_sequence = [ Consent, ScreenerQuestion, PrimerTreatment, DonationDecisions, ClosenessToParty, PayPal, EndOfSurvey ]





    