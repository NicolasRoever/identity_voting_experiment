from otree.api import Currency as c, currency_range, expect, Bot, Submission, SubmissionMustFail
from . import pages



class PlayerBot(Bot):

    def play_round(self):



         #---Consent---#

        yield pages.Consent, {
             'consent_form': True
       }
        
        #---Screener---#

        yield pages.ScreenerQuestion, {
            'political_q_6': 'agree',
            'political_q_7': 'disagree',
            'political_q_2': 'agree',
            'political_q_3': 'disagree'
            
        }
         

        #---Primer Page---#


        if self.player.participant.vars.get('treatment') == True:


            yield SubmissionMustFail(pages.PrimerTreatment, {
                'cultural_primer': 'This is a sample response for the individual question.'
            })


            
            yield pages.PrimerTreatment, {
                'cultural_primer': 'This is a sample response for the individual question. This is a sample response for the individual question. This is a sample response for the individual question.'
            }
            
            expect(self.player.cultural_primer, 'This is a sample response for the individual question. This is a sample response for the individual question. This is a sample response for the individual question.')
                
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

        yield pages.ClosenessToParty



        #---Demographics---#

        yield pages.Demographics, {
            'gender': 'Male',
            'income': '1000-2000',
            'education': 'university'
        }

        #---Paypal---#

        yield SubmissionMustFail(pages.PayPal)

        yield pages.PayPal, {
            'paypal_email': 'valid-email@example.com'
        }

        expect(self.player.paypal_email, 'valid-email@example.com')


    


