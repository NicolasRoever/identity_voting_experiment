

def count_words_in_string(text):
    words = text.split()
    return len(words)



def apply_screener_criterion(answer_question_6, answer_question_7):
    """ A person is included in the sample if they answer either question 6 with 'agree' and question 7 with 'disagree'. They are also included if they answer both questions this way, but they need to answer at least one in this way. 

    Returns True if the person is included, False otherwise.
    
    """
    if answer_question_6 == 'agree' and answer_question_7 == 'disagree':
        return True
    
    elif answer_question_6 == 'agree' or answer_question_7 == 'disagree':
        return True
    else:
        return False