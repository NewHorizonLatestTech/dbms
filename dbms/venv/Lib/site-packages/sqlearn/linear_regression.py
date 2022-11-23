import numpy as np
import pandas as pd
from .sgd_regression import SGDRegressor

class LinearRegressor(SGDRegressor):
    """
    A class that represents a trainable linear regressor.
    Uses mean squared error as the loss function.

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
    calc_gradient(self, batch_X, batch_y)
        A function that calculates the gradient of the loss function.
    sgd(self, batch_X, batch_y):
        Performs one step of stochastic gradient descent.
    train(self, X, y):
        Trains the model on a dataset and the corresponding labels.
    predict(self, X):
        Makes prediction from a dataframe of observations.
    get_weights(self):
        Returns the trained weights of the model.
    """

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
        gradient = 0
        for i, x in batch_X.iterrows():
            gradient += ((x @ self.theta) - batch_y[i]) * x
        gradient /= batch_X.shape[0]
        return gradient

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
        ones = pd.DataFrame(np.ones((X.shape[0], 1)))
        X_ones = pd.concat((ones, X), axis=1)
        preds = X_ones @ self.theta
        return preds
