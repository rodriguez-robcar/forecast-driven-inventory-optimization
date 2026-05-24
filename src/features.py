import numpy as np

def calculate_wape(y_true, y_pred):
    """
    Calculate the Weighted Absolute Percentage Error (WAPE) between true and predicted values.
    
    Parameters:
    y_true (array-like): The true values.
    y_pred (array-like): The predicted values.
    
    Returns:
    float: The WAPE value as a percentage.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # Calculate the absolute errors and the total actual demand
    absolute_errors = np.abs(y_true - y_pred)
    total_actual_demand = np.sum(np.abs(y_true))
    
    # Handle the case where total actual demand is zero to avoid division by zero
    if total_actual_demand == 0:
        return np.inf  # Return infinity if there is no actual demand
    
    # Calculate WAPE
    wape = np.sum(absolute_errors) / total_actual_demand * 100
    return wape
