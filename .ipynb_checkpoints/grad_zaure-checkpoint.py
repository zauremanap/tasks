def loss_func(x):
    return 4*x**3 + 4*x + 7

def gradient(x):
    return 12*x**2 + 3

def gradient_descent(start, learn_rate, iter):
    x = start
    trajectory = [x]
    for i in range(iter):
        grad = gradient(x)
        x = x - learn_rate * grad
        trajectory.append(x)
    return x, trajectory

start = 1
learn_rate = 0.1
iter = 3

x, trajectory = gradient_descent(start, learn_rate, iter)
print(x)
print(trajectory)
