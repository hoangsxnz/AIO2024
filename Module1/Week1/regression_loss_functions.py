import random
import math


def regression(num_samples, loss_name):
    assert num_samples.isnumeric(), "number of samples must be an integer number"
    assert loss_name in ['MAE', 'MSE', 'RMSE'], f"{loss_name} is not supported"

    num_samples = int(num_samples)

    print(
        f"Input number of samples (interger number) which are generated: {num_samples}")
    print(f"Input loss name: {loss_name}")

    s = 0
    loss = 0

    for _ in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        if loss_name == 'MAE':
            loss = abs(target - predict)
            s += loss
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss = (target - predict) ** 2
            s += loss

        print(
            f"loss name: {loss_name}, sample: {_}, pred: {predict}, target: {target}, loss: {loss}")

    if loss_name == 'MAE' or loss_name == 'MSE':
        print(f"final {loss_name}: {s/num_samples}")
    else:
        print(f"final {loss_name}: {math.sqrt(s/num_samples)}")
