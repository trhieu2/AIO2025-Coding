import random
from lib2to3.pgen2.token import NUMBER


def cal_ae(y, y_hat):
    '''
    Calculate the absolute error
    :param y: ground truth
    :param y_hat: predicted value
    :return: absolute value
    '''
    return abs(y - y_hat)

def cal_se(y, y_hat):
    '''
    Calculate the square error
    :param y: ground truth
    :param y_hat: predicted value
    :return: square error
    '''
    return (y-y_hat)**2

def cal_loss():
    num_samples = input("Input number of samples generated: ")

    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    loss_name = input("Input loss name: ")

    final_loss = 0

    num_samples = int(num_samples)

    for i in range(num_samples):
        pred_val = random.uniform(0,10)
        target_val = random.uniform(0,10)

        if loss_name == 'MAE':
            loss = cal_ae(pred_val,target_val)
        if loss_name == 'MSE':
            loss = cal_se(pred_val,target_val)

        final_loss += loss

    final_loss /= num_samples

    print(final_loss)
    return final_loss

if __name__ == '__main__':
    _ = cal_loss()