'''
A  collection of data science funcitons.

Mean, Median, and Mode are three kinds of statistical averages.
In the following I will be utilizing the python coding language to implement
three functions that take in a series of values and return either the Mean,
Median, or Mode, or all three.
'''


def mean(x):
    '''
    The mean for a given set of values is the sum of all of the values, devided
    by the number of values.
    '''
    mean_output = sum(x)/len(x)
    return mean_output


def median(x):
    '''
    The median for a given set of values is the middle most value in sorted
    list of values.
    '''
    sorted_x = sorted(x)
    x_len = len(x)
    index = (x_len - 1) // 2

    if (x_len % 2):
        return sorted_x[index]
    else:
        return (sorted_x[index] + sorted_x[index + 1])/2.0


def mode(x):
    '''
    The mode for a given set of values is the value that appears the most
    frequently in a given list of values.
    '''
    most = max(list(map(x.count, x)))
    return list(set(filter(lambda y: x.count(y) == most, x)))


def meanMedianMode(numbers):
    return ('Mean', mean(numbers), '\n', 'Median', median(numbers), '\n',
            'Mode', mode(numbers))
