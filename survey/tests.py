from otree.api import Currency as c, currency_range, expect, Bot, Submission
from . import pages




class PlayerBot(Bot):
   

    def play_round(self):
        yield Submission(pages.Primer, {
            'cultural_primer_individual': 'This is a sample response for the individual question. ',
            'cultural_primer_society': 'This is a sample response for the society question. '
        }, check_html=False)

        # Verify that the data was saved correctly
        expect(self.player.cultural_primer_individual, 'This is a sample response for the individual question. ')
        expect(self.player.cultural_primer_society, 'This is a sample response for the society question. ' )

        