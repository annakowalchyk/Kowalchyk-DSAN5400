## Discussion Questions

By : Anna Kowalchyk

### Question B:
With only access to prior probabilities I would expect the guess to favor Johnson because there is a higher probability that the author is Johnson because it sees almost double the amount of documents written by Johnson. More specifically, 2/3 of the documents given are written by Johnson. 

### Question C: Exploratory Analysis
While scrolling through the data, it seems that Kennedy's text is more of him speaking whereas Johnson's text is long but often includes questions from a narrator. This is not actually Johnson speaking and therefore can lead to mistraining the model based on someone else's phrasing. Additionally, Kennedy seems to address specific people in the beginning of his speeches compared to Johnson who keeps it broad by stating 'Good afternoon ladies and gentleman' or something of similar sorts. Both authors express gratitude in various ways and use 'I' to assert responsibility. Kennedy also ends with some sort of thank you and salutation dependent on the time of day. This appears to be less common with text written by Johnson. 

Do one author’s documents tend to be shorter in length? What are the most common words used by each author? Do either of the authors tend to start or end their works in a consistent way?

### Question E:
The two prior probability estimates are:
    P(class = 0) = 0.353
    P(class = 1) = 0.647

The shape of the matrix storing the likelihoods is the (number of rows x number of words (length of the vocabulary)). More specfically it is (2x22961)

When varrying the smoothing hyperparameter to 0, it leads to zero probability error and seems to only guess class = 0 and can result in overfitting. On the other end, with a high hyperparameter the model predicts class = 1 leading to underfitting. 

### Question F:
Predicted Authors:
0 - Kennedy
0 - Kennedy
1 - Johnson
1 - Johnson
0 - Kennedy
0 - Kennedy
1 - Johnson
0 - Kennedy
0 - Kennedy
0 - Kennedy

## PROBLEM 2:

The scikit-learn predictions seen below seems to be more even with predicting between Johnson and Kennedy. What I mean by this is the model did not just select Kennedy because it thought it would be a safer option. Instead, it selected Johnson more times than my model. 

scikit-learn Predictions:
0 - Kennedy
1 - Johnson
1 - Johnson
1 - Johnson
0 - Kennedy
0 - Kennedy
1 - Johnson
0 - Kennedy
0 - Kennedy
0 - Kennedy

## PROBLEM 3:

### (A)

Accuracy:
    My model -> 0.80
    scikit-learn -> 0.90

F1-score
    My model -> 0.75
    scikit-learn -> 0.889

### (B)

My confusion matrix (conf.jpg):
    The model never predicted a Kennedy text as Johnson (class = 0). However, it could not accurately predict Johnson's text (class = 1) as it predicted Kennedy for 2 out of the 5 text given. 

Scikit-learn (conf_scikit.jpg):
    This model was better at predicting Johnson's work as it got one more correct than my model. However, it was the same for the Kennedy's text in that it was accurate for every text given. 

