import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array([list[:3], list[3:6], list[-3:]])
    flatten_matrix = matrix.flatten()

    y_mean, y_variance, y_std, y_max, y_min, y_sum = [], [], [], [], [], []
    x_mean, x_variance, x_std, x_max, x_min, x_sum = [], [], [], [], [], []

    for column in matrix.T:
        y_mean.append(column.mean())
        y_variance.append(column.var())
        y_std.append(column.std())
        y_max.append(column.max())
        y_min.append(column.min())
        y_sum.append(column.sum())

    for row in matrix:
        x_mean.append(row.mean())
        x_variance.append(row.var())
        x_std.append(row.std())
        x_max.append(row.max())
        x_min.append(row.min())
        x_sum.append(row.sum())

    calculations = {
        'mean': [y_mean, x_mean, flatten_matrix.mean()],
        'variance': [y_variance, x_variance, flatten_matrix.var()],
        'standard deviation': [y_std, x_std, flatten_matrix.std()],
        'max': [y_max, x_max, flatten_matrix.max()],
        'min': [y_min, x_min, flatten_matrix.min()],
        'sum': [y_sum, x_sum, flatten_matrix.sum()]
    }

    return calculations
