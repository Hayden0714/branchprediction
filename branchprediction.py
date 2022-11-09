from random import paretovariate
from random import random

def next_branch_outcome_loop():
    alpha = 2
    outcome = paretovariate(alpha)
    outcome = outcome > 2
    return outcome

def next_branch_outcome_random():
    outcome = random()
    outcome = outcome > 0.5
    return outcome

class Predictor:
    
    def __init__(self):
        self.state = 0
    
    def next_predict(self):
        """
        Use this method to return the prediction based off of the current
        state.
        """
        raise NotImplementedError("Implement this method")
        
    def incorrect_predict(self):
        """
        Use this method to set the next state if an incorrect predict
        occurred. (self.state = next_state)
        """
        raise NotImplementedError("Implement this method")
        
    def correct_predict(self):
        """
        Use this method to set the next state if an incorrect predict
        occurred. (self.state = next_state)
        """
        raise NotImplementedError("Implement this method")