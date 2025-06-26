import math
def sigmoid(x):
    '''
    Sigmoid function, AKA logistic function, is one of the most basic activation functions.
    This function aims to compute the input into an output ranging from 0 to 1
    :param x: input number
    :return: output number
    '''
    return 1/(1+math.exp(-x))

def ReLU(x):
    '''
    ReLU or Rectified Linear Unit is an activation function returning:
    - 0 if the input is a negative number
    - itself if the input is a positive number
    :param x: input number
    :return: output number
    '''
    if x <= 0:
        return 0
    else:
        return x

def ELU(x):
    '''
    ELU stands for Exponential Linear Unit, is an activation function used in neural network.
    :param x:
    :return:
    '''
    if x <= 0:
        return 0.01(math.exp(x) -1)
    else:
        return x