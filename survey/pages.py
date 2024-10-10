from otree.api import *
import itertools

from .python_functions import count_words_in_string





class PoliticalOpinions(Page):
    form_model = 'player'
    form_fields = ['political_q_1', 'political_q_2', 'political_q_3', 'political_q_4', 'political_q_5', 'political_q_6', 'political_q_7', 'political_q_8', 'political_q_9', 'political_q_10']

     @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class PoliticiansAfDSPD(Page):
    form_model = 'player'
    form_fields = ['choice_muetzenich_frohmeier', 'reason_choice_muetzenich_frohmeier', 'muetzenich_name', 'muetzenich_statement', 'muetzenich_no_statement_choice', 'frohmeier_name', 'frohmeier_statement', 'frohmeier_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/Forhmaier_Muetzenich.mp4',
            'politician_1': 'Rolf Muetzenich (SPD)',
            'politician_1_name': 'muetzenich_name',
            'politician_1_statement': 'muetzenich_statement',
            'politician_1_no_statement_choice': 'muetzenich_no_statement_choice',
            'politician_2': 'Markus Frohmaier (AfD)',
            'politician_2_name': 'frohmeier_name',
            'politician_2_statement': 'frohmeier_statement',
            'politician_2_no_statement_choice': 'frohmeier_no_statement_choice',
            'choice': 'choice_muetzenich_frohmeier',
            'reason_choice': 'reason_choice_muetzenich_frohmeier'
        }
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1
    
class PoliticiansAfDCDU(Page):
    form_model = 'player'
    form_fields = ['choice_kraft_wiener', 'reason_choice_kraft_wiener', 'wiener_name', 'wiener_statement', 'wiener_no_statement_choice', 'kraft_name', 'kraft_statement', 'kraft_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/WernerKraft_KlausWiener.mp4',
            'politician_1': 'Wiener',
            'politician_1_name': 'wiener_name',
            'politician_1_statement': 'wiener_statement',
            'politician_1_no_statement_choice': 'wiener_no_statement_choice',
            'politician_2': 'Kraft',
            'politician_2_name': 'kraft_name',
            'politician_2_statement': 'kraft_statement',
            'politician_2_no_statement_choice': 'kraft_no_statement_choice',
            'choice': 'choice_kraft_wiener',
            'reason_choice': 'reason_choice_kraft_wiener'
        }
    
   
    def error_message(self, values):
        print(values)
        if values.get('wiener_no_statement_choice') == None and values['wiener_statement'] == '':
            return 'Bitte geben Sie ein Statement für den Politiker Wiener ein oder wählen Sie "Ich möchte kein Statement schreiben".'
        
        if values["kraft_no_statement_choice"] == None and values["kraft_statement"] == '':
            return 'Bitte geben Sie ein Statement für den Politiker Kraft ein oder wählen Sie "Ich möchte kein Statement schreiben".'
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1
        


class DonationDecisions(Page):
    form_model = 'player'
    form_fields = ['donation_afd', 'donation_cdu', 'donation_spd']


    def error_message(self, values):

        if values["donation_afd"] + values["donation_cdu"] + values["donation_spd"] > 15:
            return "Sie können maximal 15 Euro spenden."
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1
    

class MechanismQuestion(Page):
    form_model = 'player'
    form_fields = ['issue_1_importance', 'issue_2_importance', 'issue_3_importance', 'issue_4_importance', 'issue_5_importance', 'issue_6_importance', 'issue_7_importance', 'issue_8_importance', 'issue_9_importance', 'issue_10_importance']

    def error_message(self, values):
        if sum(values.values()) != 100:
            return "Die Summe der Punkte muss 100 ergeben."
        
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1

class ExperimenterDemand(Page):
    form_model = 'player'
    form_fields = ['experiment_purpose']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1


class PrimerTreatment(Page):
    form_model = 'player'
    form_fields = ['cultural_primer_individual', 'cultural_primer_society']

    template_name = 'global/Primer.html'

    def vars_for_template(self):
        return {
            'picture_path': 'images/CSD.jpeg',
            'picture_description': "Christopher Street Day 2023 in Köln", 
            'question_individual': "Nehmen Sie am Christopher Street Day in ihrer Nähe teil? Wenn ja, warum? Wenn nein, warum nicht?",
            'question_society': "Wie wichtig sind ihrer Meinung nach Veranstaltungen wie der Christopher Street Day für unsere Gesellschaft?", 
        }
    
    @staticmethod
    def live_method(player, data):

        if data.get('formfieldName') == 'cultural_primer_individual':
            words_in_individual_data = count_words_in_string(data.get('input', ''))
            player.word_count_individual = words_in_individual_data


        if data.get('formfieldName') == 'cultural_primer_society':
            words_in_society_data = count_words_in_string(data.get('input', ''))
            player.word_count_society = words_in_society_data


    def is_displayed(player):
        return player.participant.treatment == True
    
    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1



   # def error_message(self, values):
    #    # Perform your validation here
     #   if self.player.field_maybe_none('word_count_individual') < 20:
      #      return 'Bitte geben Sie mindestens 20 Wörter in der ersten Frage ein.'
       ##    return 'Bitte geben Sie mindestens 20 Wörter in der zweiten Frage ein.'

 

class PrimerActiveControl(Page):
    form_model = 'player'
    form_fields = ['cultural_primer_individual', 'cultural_primer_society']

    template_name = 'global/Primer.html'

    def is_displayed(player):
        return player.participant.treatment == False

    

    def vars_for_template(self):
        return {
            'picture_path': 'images/karneval.jpg',
            'picture_description': "Karneval 2023 in Köln", 
            'question_individual': "Nehmen Sie am Karneval/Fasching in ihrer Nähe teil? Wenn ja, warum? Wenn nein, warum nicht?",
            'question_society': "Wie wichtig sind ihrer Meinung nach Veranstaltungen wie der Karneval/Fasching für unsere Gesellschaft?", 


        }
    
    
    def live_method(self, data):
        # Handle the data sent from the client
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.participant.progress += 1


page_sequence = [ PoliticalOpinions, PrimerActiveControl, PrimerTreatment, PoliticiansAfDSPD,PoliticiansAfDCDU, DonationDecisions, 
                    MechanismQuestion, ExperimenterDemand, ]