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