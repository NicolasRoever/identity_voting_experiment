from otree.api import *
import itertools
import time
import random

from .python_functions import count_words_in_string


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent_form']
    def before_next_page(self):
        self.player.time_after_consent = time.time() 


class EndOfSurvey(Page):
    pass


class PoliticalOpinions(Page):
    form_model = 'player'
    form_fields = ['political_q_1', 'political_q_2', 'political_q_3', 'political_q_4', 'political_q_5', 'political_q_6', 'political_q_7', 'political_q_8', 'political_q_9', 'political_q_10', ]

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_political_opinions = time.time()

    def vars_for_template(self):
        return {
            'progress_percentage': self.participant.progress / 8 * 100
        }
    
class EstimationQuestion(Page):
    form_model = 'player'
    form_fields = ['slider_taxes', 'slider_gays', 'slider_old_people']

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_estimation_question = time.time()
    def vars_for_template(self):
        return {
            'progress_percentage': self.participant.progress / 8 * 100
        }



class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'income']

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_demographics = time.time()
    def vars_for_template(self):
        return {
            'progress_percentage': self.participant.progress / 8 * 100
        }



class PoliticiansAfDSPD(Page):
    form_model = 'player'
    form_fields = ['choice_muetzenich_frohmeier', 'reason_choice_muetzenich_frohmeier', 'muetzenich_name', 'muetzenich_statement', 'muetzenich_no_statement_choice', 'frohmeier_name', 'frohmeier_statement', 'frohmeier_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/Forhmaier_Muetzenich.mp4',
            'heading': 'Meinung zu Politikern (1/2)',
            'politician_1': 'Rolf Mützenich (SPD)',
            'politician_1_name': 'muetzenich_name',
            'politician_1_statement': 'muetzenich_statement',
            'politician_1_no_statement_choice': 'muetzenich_no_statement_choice',
            'politician_2': 'Markus Frohmaier (AfD)',
            'politician_2_name': 'frohmeier_name',
            'politician_2_statement': 'frohmeier_statement',
            'politician_2_no_statement_choice': 'frohmeier_no_statement_choice',
            'choice': 'choice_muetzenich_frohmeier',
            'reason_choice': 'reason_choice_muetzenich_frohmeier', 
            'progress_percentage': self.participant.progress / 8 * 100
        }
    
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_politician_choice_afd_spd = time.time()


    

class PoliticiansAfDCDU(Page):
    form_model = 'player'
    form_fields = ['choice_kraft_wiener', 'reason_choice_kraft_wiener', 'wiener_name', 'wiener_statement', 'wiener_no_statement_choice', 'kraft_name', 'kraft_statement', 'kraft_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/WernerKraft_KlausWiener.mp4',
            'heading': 'Meinung zu Politikern (2/2)',
            'politician_1': 'Klaus Wiener (CDU)',
            'politician_1_name': 'wiener_name',
            'politician_1_statement': 'wiener_statement',
            'politician_1_no_statement_choice': 'wiener_no_statement_choice',
            'politician_2': 'Rainer Kraft (AfD)',
            'politician_2_name': 'kraft_name',
            'politician_2_statement': 'kraft_statement',
            'politician_2_no_statement_choice': 'kraft_no_statement_choice',
            'choice': 'choice_kraft_wiener',
            'reason_choice': 'reason_choice_kraft_wiener', 
             'progress_percentage': self.participant.progress / 8 * 100
        }
    
    def error_message(self, values):
      
        if values.get('wiener_no_statement_choice') == None and values['wiener_statement'] == '':
            return 'Bitte geben Sie ein Statement für den Politiker Wiener ein oder wählen Sie "Ich möchte kein Statement schreiben".'
        
        if values["kraft_no_statement_choice"] == None and values["kraft_statement"] == '':
            return 'Bitte geben Sie ein Statement für den Politiker Kraft ein oder wählen Sie "Ich möchte kein Statement schreiben".'
        
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_politician_choice_afd_cdu = time.time()

        
   



class DonationDecisions(Page):
    form_model = 'player'
    form_fields = ['donation_afd', 'donation_cdu', 'donation_spd']


    def error_message(self, values):

        if values["donation_afd"] + values["donation_cdu"] + values["donation_spd"] > 15:
            return "Sie können maximal 15 Euro spenden."
        
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_donation_decisions = time.time()

    def vars_for_template(self):

        # Define the sliders and shuffle them
        sliders = [
            {'name': 'donation_spd', 'label': 'SPD', 'value': 5},
            {'name': 'donation_cdu', 'label': 'CDU', 'value': 5},
            {'name': 'donation_afd', 'label': 'AfD', 'value': 5},
        ]
        random.shuffle(sliders)  # Randomize the order for each player

        return {'sliders': sliders, 
                'progress_percentage': self.participant.progress / 8 * 100}

        

    

class MechanismQuestion(Page):
    form_model = 'player'
    form_fields = ['issue_1_importance', 'issue_2_importance', 'issue_3_importance', 'issue_4_importance', 'issue_5_importance', 'issue_6_importance', 'issue_7_importance', 'issue_8_importance', 'issue_9_importance', 'issue_10_importance']

    def error_message(self, values):
        if sum(values.values()) != 100:
            return "Die Summe der Punkte muss 100 ergeben."
        
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_mechanism_question = time.time()
    def vars_for_template(self):
        return {
            'progress_percentage': self.participant.progress / 8 * 100
        }

        


class ExperimenterDemand(Page):
    form_model = 'player'
    form_fields = ['experiment_purpose']

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_experimenter_demand = time.time()
    def vars_for_template(self):
        return {
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
            words_in_individual_data = count_words_in_string(data.get('input', ''))
            player.word_count_individual = words_in_individual_data



    def is_displayed(player):
        return player.participant.treatment == True
    
    
    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_primer = time.time()



    
        
    


   # def error_message(self, values):
    #    # Perform your validation here
     #   if self.player.field_maybe_none('word_count_individual') < 20:
      #      return 'Bitte geben Sie mindestens 20 Wörter in der ersten Frage ein.'
       ##    return 'Bitte geben Sie mindestens 20 Wörter in der zweiten Frage ein.'

 

class ClosenessToParty(Page):
    form_model = 'player'
    form_fields = ['slider_spd', 'slider_cdu', 'slider_afd']

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_closeness_to_party = time.time()

    def vars_for_template(self):
        return {
            'progress_percentage': self.participant.progress / 8 * 100
        }

class PrimerActiveControl(Page):
    form_model = 'player'
    form_fields = ['cultural_primer']

    template_name = 'global/Primer.html'

    def is_displayed(player):
        return player.participant.treatment == False


    def vars_for_template(self):
        return {
            'picture_path': 'images/karneval.jpg',
            'picture_description': "Karneval 2023 in Köln", 
            'question_primer': "Welche Emotionen verbinden Sie mit dem Karneval? Wie wichtig halten Sie den Karneval für unsere Gesellschaft?",
            'question_society': "Wie wichtig sind ihrer Meinung nach Veranstaltungen wie der Karneval/Fasching für unsere Gesellschaft?", 
            'text_event_description': "Der Karneval ist ein Fest, das in vielen Städten jährlich stattfindet. Er erinnert an historische Traditionen und Bräuche und entstand ursprünglich als Fest vor Beginn der Fastenzeit. Der Politiker Klaus Mandel (CDU) beschreibt das Fest so: 'Das Brauchtum und unsere Karnevalsgesellschaften sind für das Zusammenleben der Generationen sehr wichtig. Karneval hat die Kraft zu verbinden und Menschen mitzunehmen.'",
            'progress_percentage': self.participant.progress / 8 * 100

        }
    
    
    def live_method(self, data):
        # Handle the data sent from the client
        pass

    def before_next_page(self):
        self.participant.progress += 1
        self.player.time_after_primer = time.time()

 

    


page_sequence = [DonationDecisions, ClosenessToParty,  Consent,  PrimerActiveControl, PrimerTreatment, EndOfSurvey ]