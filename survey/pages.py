from otree.api import *
class PoliticalOpinions(Page):
    form_model = 'player'
    form_fields = ['political_q_1', 'political_q_2', 'political_q_3', 'political_q_4', 'political_q_5', 'political_q_6', 'political_q_7', 'political_q_8', 'political_q_9', 'political_q_10']


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']

class Primer(Page):
    form_model = 'player'
    form_fields = ['cultural_primer_individual', 'cultural_primer_society']

class PoliticiansAfDSPD(Page):
    form_model = 'player'
    form_fields = ['choice_muetzenich_frohmeier', 'reason_choice_muetzenich_frohmeier', 'choice_kraft_wiener', 'reason_choice_kraft_wiener', 'muetzenich_name', 'muetzenich_statement', 'muetzenich_no_statement_choice', 'wiener_name', 'wiener_statement', 'wiener_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/WernerKraft_KlausWiener.mp4',
            'politician_1': 'Muetzenich',
            'politician_2': 'Frohmeier',
        }
    
class PoliticiansAfDCDU(Page):
    form_model = 'player'
    form_fields = ['choice_kraft_wiener', 'reason_choice_kraft_wiener', 'wiener_name', 'wiener_statement', 'wiener_no_statement_choice', 'kraft_name', 'kraft_statement', 'kraft_no_statement_choice']

    template_name =  'global/politicianDecision.html'

    def vars_for_template(self):
        return {
            'video_url': 'videos/WernerKraft_KlausWiener.mp4',
            'politician_1': 'Wiener',
            'politician_2': 'Kraft',
        }
class DonationDecisions(Page):
    form_model = 'player'
    form_fields = ['donation_afd', 'donation_cdu', 'donation_spd']

class MechanismQuestion(Page):
    form_model = 'player'
    form_fields = ['issue_1_importance', 'issue_2_importance', 'issue_3_importance', 'issue_4_importance', 'issue_5_importance', 'issue_6_importance', 'issue_7_importance', 'issue_8_importance', 'issue_9_importance', 'issue_10_importance']

class ExperimenterDemand(Page):
    form_model = 'player'
    form_fields = ['experiment_purpose']


page_sequence = [ExperimenterDemand, MechanismQuestion, PoliticalOpinions, Primer, PoliticiansAfDCDU, PoliticiansAfDSPD, DonationDecisions, Demographics]
