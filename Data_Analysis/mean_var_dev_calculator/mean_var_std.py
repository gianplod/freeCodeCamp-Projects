import numpy as np

def calculate(num_list):

    if len(num_list) != 9: 

        raise ValueError("List must contain nine numbers.")
    
    else:
        
        num_array = np.array(num_list).reshape((3,3))
        
        mean = [list(num_array.mean(axis=0)), list(num_array.mean(axis=1)), num_array.mean()]
        variance = [list(num_array.var(axis=0)), list(num_array.var(axis=1)), num_array.var()]
        std_dev = [list(num_array.std(axis=0)), list(num_array.std(axis=1)), num_array.std()]
        maxs = [list(num_array.max(axis=0)), list(num_array.max(axis=1)), num_array.max()]
        mins = [list(num_array.min(axis=0)), list(num_array.min(axis=1)), num_array.min()]
        sums = [list( num_array.sum(axis=0)), list(num_array.sum(axis=1)), num_array.sum()]

        calculations = {
            'mean' : mean,
            'variance' : variance,
            'standard deviation' : std_dev,
            'max' : maxs,
            'min' : mins,
            'sum' : sums
        }
    
        return calculations

    