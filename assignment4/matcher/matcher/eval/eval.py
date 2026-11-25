import pandas as pd
# Use off the shelf library to calculate precision, recall and F1
from sklearn.metrics import precision_score, recall_score, f1_score

def evaluate(results, metric):
    y_true = results["true"]
    y_pred = results["predicted"]

    # Calculate metrics that are asked
    if metric == "precision":
        return precision_score(y_true,y_pred)
    elif metric == "recall":
        return recall_score(y_true,y_pred)
    elif metric == "f1":
        return f1_score(y_true,y_pred)
    else:
        None