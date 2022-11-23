import numpy as np
import pandas as pd
from .model_interface import Model
import random

class SGDRegressor(Model):
    """
    A parent class for a regression model that's trained using stochastic 
    gradient descent and optional L2 regularization. 
    
    The functions calc_gradient and predict are not implemented.

    Attributes:
    ----------
    epochs (default=5)
        The number of passes the model makes through the dataset.
    batch_size (default=1)
        The number of observations used to calculate the gradient during
        the process of stochastic gradient descent.
    learning_rate (default=0.001)
        The rate at which the model changes during stochastic gradient
        descent.
    l2_reg_weight (default=0)
        The weight used for the L2 regularization. Use 0 for no L2
        regularization.
    seed (default=0)
        The seed used for random processes.
    
    Functions:
    ----------
    calc_gradient(self, batch_X, batch_y) [NOT IMPLEMENTED]
        A function that calculates the gradient of the loss function.
    sgd(self, batch_X, batch_y):
        Performs one step of stochastic gradient descent.
    train(self, X, y):
        Trains the model on a dataset and the corresponding labels.
    predict(self, X): [NOT IMPLEMENTED]
        Makes prediction from a dataframe of observations.
    get_weights(self):
        Returns the trained weights of the model.
    """

    def __init__(self, epochs=5, batch_size=1, learning_rate=0.001, l2_reg_weight=0, seed=0):
        """
        Initializes the model.

        Parameters:
        ----------
        epochs (default=5)
            The number of passes the model makes through the dataset.
        batch_size (default=1)
            The number of observations used to calculate the gradient during
            the process of stochastic gradient descent.
        learning_rate (default=0.001)
            The rate at which the model changes during stochastic gradient
            descent.
        seed (default=0)
            The seed used for random processes.
        """
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.l2_reg_weight = l2_reg_weight
        self.seed = seed
        random.seed(self.seed)
        self.theta = None
        self.trained = False

    def calc_gradient(self, batch_X, batch_y):
        """
        A function to calculate the gradient of the loss function.
        
        Parameters:
        ----------
        batch_X 
            A dataframe of a batch of observations without labels
        batch_y
            A dataframe (or series) of the labels of those observations.

        Returns:
        ----------
        gradient
            The calculated gradient.
        """
        pass

    def sgd(self, batch_X, batch_y):
        """
        Performs one step of stochastic gradient descent.

        Parameters:
        ----------
        batch_X
            A dataframe containing a batch of observations.
        batch_y
            A dataframe (or series) containing the labels
            for batch_X
        """
        gradient = self.calc_gradient(batch_X, batch_y)
        self.theta = self.theta - (self.learning_rate*gradient + self.l2_reg_weight*self.theta)

    def train(self, X, y):
        """
        Trains the model using stochastic gradient descent and the
        initialized hyperparameters.

        Parameters:
        ----------
        X
            A dataframe containing rows representing observations 
            without a label column. Strictly numeric.
        y
            A dataframe (or series) containing the labels for each
            observation in X.
        """
        ones = pd.DataFrame(np.ones((X.shape[0], 1)))
        ones.index = X.index
        X_ones = pd.concat((ones, X), axis=1)
        m = X_ones.shape[0]
        n = X_ones.shape[1]
        if not self.trained:
            self.theta = pd.Series(np.zeros(n))
            self.theta = self.theta.set_axis(X_ones.columns)
            self.trained = True
        for epoch in range(self.epochs):
            for batch in range(m):
                batch_i = random.sample(range(m), self.batch_size)
                batch_X = X_ones.iloc[batch_i]
                batch_y = y.iloc[batch_i]
                self.sgd(batch_X, batch_y)

    def predict(self, X):
        """
        Makes predictions from a dataframe of observations.

        Parameters:
        ----------
        X
            A dataframe (or series) containing observations.

        Returns:
        ----------
        y
            The predicted labels of the observations.
        """
        pass

    def get_weights(self):
        """
        Returns the trained weights of the SGDRegressor.
        Can also be accessed by the attribute 'theta'.

        Returns:
        ----------
        w
            The trained weights of the model.
        """
        return self.theta
