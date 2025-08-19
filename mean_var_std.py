import numpy as np

def calculate(input):
    if len(input) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array([[input[0],input[1],input[2]],[input[3],input[4],input[5]],[input[6],input[7],input[8]]])
    
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
        'mean': [vertical_mean.tolist(), horizontal_mean.tolist(), flattened_mean.tolist()],
        'variance': [vertical_variance.tolist(), horizontal_variance.tolist(), flattened_variance.tolist()],
        'standard deviation': [vertical_std.tolist(), horizontal_std.tolist(), flattened_std.tolist()],
        'max': [vertical_max.tolist(), horizontal_max.tolist(), flattened_max.tolist()],
        'min': [vertical_min.tolist(), horizontal_min.tolist(), flattened_min.tolist()],
        'sum': [vertical_sum.tolist(), horizontal_sum.tolist(), flattened_sum.tolist()]
    }

    return result

print(calculate([0,1,2,3,4,5,6,7,8]))

#   result = {
#       'mean': [vertical_mean, horizontal_mean, flattened_mean],
#       'variance': [vertical_variance, horizontal_variance, flattened_variance],
#       'standard deviation': [vertical_std, horizontal_std, flattened_std],
#       'max': [vertical_max, horizontal_max, flattened_max],
#       'min': [vertical_min, horizontal_min, flattened_min],
#       'sum': [vertical_sum, horizontal_sum, flattened_sum]
#   }