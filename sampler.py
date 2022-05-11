
import numpy as np


class Sampler():

    def __init__(self):
        pass


class MetropolisHastings(Sampler):
    """
    Metropolis-Hastings sampler class

    Attributes
    ----------
    model : MaterialModel
        Material model class (linear elastic
                              linear elastic-perfectly plastic
                              linear elastic-linear hardening
                              linear elastic-nonlinear hardening)

    data : ndarray
        Experimental stress-strain data

    Methods
    -------
    
    Notes
    -----
    """

    def __init__(self, model, data):
        self.model = model
        self.data = data

    def sample(self):
        x_p = self.draw_proposal()
        pi_x_i = self.calculate_posterior(x_i)
        pi_x_p = self.calculate_posterior(x_p)
        self.accept_or_reject()

    def accept_or_reject(self):
        alpha = self.calculate_acceptance_ratio()
        u = self.generate_uniform_random_number()
        # Accept if u < alpha
        # Reject if u > alpha

    def calculate_acceptance_ratio(self):
        return min(1, pi_x_p, pi_x_i)

    def generate_uniform_random_number():
        return np.random.uniform(low=0.0, high=1.0)

    def calculate_posterior(self, model):
        """
        Calculate the posterior

        Parameters
        ----------
        model : MaterialModel class
            Material model class

        Returns
        -------

        """
        return model.posterior(self.data)

    def draw_proposal(self, model):
        return model.proposal_distribution()

