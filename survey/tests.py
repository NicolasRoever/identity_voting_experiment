from otree.api import Currency as c, currency_range, expect, Bot, Submission, SubmissionMustFail
from . import pages





class PlayerBot(Bot):

    def play_round(self):

         #---Consent---#

        yield pages.Consent, {
             'consent_form': True
       }
         

        #---Primer Page---#


        if self.player.participant.vars.get('treatment') == True:


            yield pages.PrimerTreatment, {
                'cultural_primer': 'This is a sample response for the individual question.'
            }

            expect(self.player.cultural_primer, 'This is a sample response for the individual question.')

        else:
            

            yield pages.PrimerActiveControl, {
                'cultural_primer': 'This is a sample response for the individual question.'
            }

            expect(self.player.cultural_primer, 'This is a sample response for the individual question.')

                
     #---Donation Question---#
        
        yield SubmissionMustFail(pages.DonationDecisions, {
            'donation_afd': '1',
            'donation_cdu': '10',
            'donation_spd': '12'
        })


        yield pages.DonationDecisions, {
            'donation_afd': '1',
            'donation_cdu': '10',
            'donation_spd': '4'
        }

        expect(self.player.donation_afd, 1)
        expect(self.player.donation_cdu, 10)
        expect(self.player.donation_spd, 4)


        #---Closeness to Party---#


    




# class PlayerBot(Bot):
   

#     def play_round(self):

#         #---Consent---#

#         yield pages.Consent, {
#             'consent_form': True
#         }

#         #---Political Opinions---#

#         yield SubmissionMustFail(pages.PoliticalOpinions, {
#             "political_q_1": 'agree', 
#             "political_q_2": 'neutral',
#             "political_q_3": 'disagree',
#             "political_q_4": 'agree',
#             "political_q_5": 'neutral',
#             "political_q_6": 'disagree',
#         })

#         yield pages.PoliticalOpinions, {
#             "political_q_1": 'agree', 
#             "political_q_2": 'neutral',
#             "political_q_3": 'disagree',
#             "political_q_4": 'agree',
#             "political_q_5": 'neutral',
#             "political_q_6": 'disagree',
#             "political_q_7": 'agree',
#             "political_q_8": 'neutral',
#             "political_q_9": 'disagree',
#             "political_q_10": 'agree'

#         }

#         #Check that the answers were saved correctly
#         expect(self.player.political_q_1, 'agree')
#         expect(self.player.political_q_2, 'neutral')

         



#         #---Primer Page---#


#         if self.player.participant.vars.get('treatment') == True:


#             yield SubmissionMustFail(pages.PrimerTreatment, {
#                 'cultural_primer_individual': 'This is a sample response for the individual question.',
#             })

#             yield pages.PrimerTreatment, {
#                 'cultural_primer_individual': 'This is a sample response for the individual question.',
#                 'cultural_primer_society': 'This is a sample response for the society question.'
#             }

#             expect(self.player.cultural_primer_individual, 'This is a sample response for the individual question.')


#         else:
            

#             yield SubmissionMustFail(pages.PrimerActiveControl, {
#                 'cultural_primer_individual': 'This is a sample response for the individual question.',
#             })

#             yield pages.PrimerActiveControl, {
#                 'cultural_primer_individual': 'This is a sample response for the individual question.',
#                 'cultural_primer_society': 'This is a sample response for the society question.'
#             }

#             expect(self.player.cultural_primer_individual, 'This is a sample response for the individual question.')

        
#      #---Donation Question---#
        
#         yield SubmissionMustFail(pages.DonationDecisions, {
#             'donation_afd': '1',
#             'donation_cdu': '10',
#             'donation_spd': '12'
#         })


#         yield pages.DonationDecisions, {
#             'donation_afd': '1',
#             'donation_cdu': '10',
#             'donation_spd': '4'
#         }

#         expect(self.player.donation_afd, 1)
#         expect(self.player.donation_cdu, 10)
#         expect(self.player.donation_spd, 4)



#          #---PoliticiansAfDSPD---#


#         yield SubmissionMustFail(pages.PoliticiansAfDSPD, {
#             'choice_muetzenich_frohmeier': '100'
#         })
        


#         yield pages.PoliticiansAfDSPD, {
#             'choice_muetzenich_frohmeier': '100',
#             'reason_choice_muetzenich_frohmeier': 'This is a sample response for the reason choice question.',
#             'muetzenich_name': '',
#             'muetzenich_statement': '',
#             'muetzenich_no_statement_choice': 'True',
#             'frohmeier_name': 'Jens Spahn',
#             'frohmeier_statement': 'This is a sample response for the statement question for frohmeier.',
#             'frohmeier_no_statement_choice': 'False'
#         }

#         expect(self.player.choice_muetzenich_frohmeier, 100)
#         expect(self.player.reason_choice_muetzenich_frohmeier, 'This is a sample response for the reason choice question.')
#         expect(self.player.muetzenich_name, '')
#         expect(self.player.muetzenich_statement, '')
#         expect(self.player.muetzenich_no_statement_choice, True)
#         expect(self.player.frohmeier_name, 'Jens Spahn')
#         expect(self.player.frohmeier_statement, 'This is a sample response for the statement question for frohmeier.')
#         expect(self.player.frohmeier_no_statement_choice, False)


#         #---PoliticiansAfDCDU---#

#         yield pages.PoliticiansAfDCDU, {
#             'choice_kraft_wiener': '83',
#             'reason_choice_kraft_wiener': 'This is a sample response for the reason choice question.',
#             'wiener_name': 'Nicolas Roever',
#             'wiener_statement': 'This is a sample response for the statement question for wiener.',
#             'wiener_no_statement_choice': 'false',
#             'kraft_name': '',
#             'kraft_statement': '',
#             'kraft_no_statement_choice': 'true'
#         }

#         expect(self.player.choice_kraft_wiener, 83.0)
#         expect(self.player.reason_choice_kraft_wiener, 'This is a sample response for the reason choice question.')
#         expect(self.player.wiener_name, 'Nicolas Roever')
#         expect(self.player.wiener_statement, 'This is a sample response for the statement question for wiener.')
#         expect(self.player.wiener_no_statement_choice, False)
#         expect(self.player.kraft_name, '')
#         expect(self.player.kraft_statement, '')
#         expect(self.player.kraft_no_statement_choice, True)


       

#         #---Mechanism Question---#

#         yield SubmissionMustFail(pages.MechanismQuestion, {
#             'issue_1_importance': '100',
#             'issue_2_importance': '20',
#             'issue_3_importance': '20',
#             'issue_4_importance': '20',
#             'issue_5_importance': '10',
#             'issue_6_importance': '10'
#         })

#         yield pages.MechanismQuestion, {
#             'issue_1_importance': '20',
#             'issue_2_importance': '20',
#             'issue_3_importance': '20',
#             'issue_4_importance': '20',
#             'issue_5_importance': '10',
#             'issue_6_importance': '10'

#         }

#         expect(self.player.issue_1_importance, 20)
#         expect(self.player.issue_2_importance, 20)
#         expect(self.player.issue_3_importance, 20)
#         expect(self.player.issue_4_importance, 20)
#         expect(self.player.issue_5_importance, 10)
#         expect(self.player.issue_6_importance, 10)
#         expect(self.player.issue_7_importance, 0)

#         #---Estimation Question---#

#         yield pages.EstimationQuestion

#         #---Experimenter Demand Check---#

#         yield pages.ExperimenterDemand, {
#             'experiment_purpose': 'This is a sample response for the experiment purpose question.'
#         }

#         expect(self.player.experiment_purpose, 'This is a sample response for the experiment purpose question.')

#            #---Demographics---#

#         yield pages.Demographics, {
#             'age': 20,
#             'gender': 'Male',
#             'income': '1000-2000'
#         }
    

   

