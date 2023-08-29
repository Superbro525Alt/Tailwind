import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    if len(data) % 2 == 0:
        return mean([data[int(len(data) / 2)], data[int(len(data) / 2) - 1]])
    else:
        return data[math.floor(len(data) / 2)]

def mode(data):
    return max(data, key=data.count)

def variance(data):
    return sum([(x - mean(data)) ** 2 for x in data]) / len(data)

def standard_deviation(data):
    return math.sqrt(variance(data))

def z_score(data, x):
    return (x - mean(data)) / standard_deviation(data)

def z_scores(data):
    return [z_score(data, x) for x in data]

def percentile(data, p):
    return data[math.floor(len(data) * p)]

def quartiles(data):
    return [percentile(data, 0.25), percentile(data, 0.5), percentile(data, 0.75)]

def interquartile_range(data):
    return quartiles(data)[2] - quartiles(data)[0]

def outliers(data):
    return [x for x in data if x < quartiles(data)[0] - 1.5 * interquartile_range(data) or x > quartiles(data)[2] + 1.5 * interquartile_range(data)]

def remove_outliers(data):
    return [x for x in data if x not in outliers(data)]

def covariance(data1, data2):
    return sum([(x - mean(data1)) * (y - mean(data2)) for x, y in zip(data1, data2)]) / len(data1)

def correlation(data1, data2):
    return covariance(data1, data2) / (standard_deviation(data1) * standard_deviation(data2))

def least_squares_regression(data1, data2):
    return covariance(data1, data2) / variance(data1)

def least_squares_regression_line(data1, data2):
    return lambda x: least_squares_regression(data1, data2) * x + mean(data2) - least_squares_regression(data1, data2) * mean(data1)
