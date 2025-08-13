import numpy as np

def calculate(list):
    arr = np.array([[list[0],list[1],list[2]],[list[3],list[4],list[5]],[list[6],list[7],list[8]]])
    
    #Mean Calculation
    vertical_mean = np.mean(arr, axis=0)
    horizontal_mean = np.mean(arr, axis=1)
    flattened_mean = np.mean(arr)

    #Variance Calcultation
    vertical_variance = np.var(arr, axis=0)
    horizontal_variance = np.var(arr, axis=1)
    flattened_variance = np.var(arr)

    #Standard Deviation Calculation
    vertical_std = np.std(arr, axis=0)
    horizontal_std = np.std(arr, axis=1)
    flattened_std = np.std(arr)

    #Max Calculation
    vertical_max = np.max(arr, axis=0)
    horizontal_max = np.max(arr, axis=1)
    flattened_max = np.max(arr)

    #Min Calculation
    vertical_min = np.min(arr, axis=0)
    horizontal_min = np.min(arr, axis=1)
    flattened_min = np.min(arr)

    #Sum Calculation
    vertical_sum = np.sum(arr, axis=0)
    horizontal_sum = np.sum(arr, axis=1)
    flattened_sum = np.sum(arr)

    result = {
        'mean': [vertical_mean, horizontal_mean, flattened_mean],
        'variance': [vertical_variance, horizontal_variance, flattened_variance],
        'standard deviation': [vertical_std, horizontal_std, flattened_std],
        'max': [vertical_max, horizontal_max, flattened_max],
        'min': [vertical_min, horizontal_min, flattened_min],
        'sum': [vertical_sum, horizontal_sum, flattened_sum]
    }

    return result

print(calculate([0,1,2,3,4,5,6,7,8]))
