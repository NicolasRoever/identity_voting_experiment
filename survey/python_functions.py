from datetime import datetime

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
    
def calculate_time_spent(start_time_str, end_time_str):
    """ Calculate the time spent in minutes and seconds between two timestamps. """
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    duration = end_time - start_time
    minutes, seconds = divmod(duration.seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"