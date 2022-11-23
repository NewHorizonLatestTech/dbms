import numpy as np
import pandas as pd
from .sgd_regression import SGDRegressor

def sigmoid(x):
    ex = np.exp(x)
    return ex / (1 + ex)

class LogisticRegressor(SGDRegressor):
    """
    A class that represents a trainable logistic regression binary 
    classifier.
    Uses average negative log likelihood as the loss function.

    Attributes:
    ----------
    thresh (default=0.5)
        The threshold at which predictions from the logistic regressor
        change from 0 to 1. If thresh=None, then the model will output
        probabilities instead of classifications.
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

    def __init__(self, thresh=0.5, epochs=5, batch_size=1, learning_rate=0.001, l2_reg_weight=0, seed=0):
        """
        Initializes the LogisticRegressor.

        Parameters:
        ----------
        thresh (default=0.5)
            The threshold at which predictions from the logistic regressor 
            change from 0 to 1. If thresh=None, then the model will output
            probabilities instead of classifications.
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
        self.thresh = thresh
        super().__init__(epochs, batch_size=batch_size, learning_rate=learning_rate, l2_reg_weight=l2_reg_weight, seed=seed)

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
            gradient += (sigmoid(x @ self.theta) - batch_y[i]) * x
        gradient /= batch_X.shape[0]
        return gradient

    def train(self, X, y):
        """
        Trains the LogisticRegressor using stochastic gradient descent and the
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
        super().train(X, y)

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
        preds = sigmoid(X_ones @ self.theta)
        if self.thresh != None:
            preds = preds >= self.thresh
        return preds