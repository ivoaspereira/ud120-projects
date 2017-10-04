#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    for pred, a, net_w in zip(predictions, ages, net_worths):
        cleaned_data.append((a, net_w, pred - net_w))
        # Sort the data by the 2nd index (third element, which is the error)
        cleaned_data.sort(key=lambda i: i[2]) 

    return cleaned_data[:81] # returns the first 81 elements (or 90% of the original length)


