## Discussion Questions

By : Anna Kowalchyk

### Question B:
With only access to prior probabilities I would expect the guess to favor Johnson. This is because there is a higher probability that the author is Johnson based on the training set alone because it sees almost double the amount of documents written by Johnson. More specifically, 2/3 of the documents given for training are written by Johnson. 

### Question C: Exploratory Analysis
While scrolling through the data, it seems that Kennedy's text is more of him speaking whereas Johnson's text is long but often includes questions from a narrator. This is not actually Johnson speaking and therefore can lead to errors in training the model because it is referring to someone else's phrasing rather than Johnson's. Additionally, Kennedy seems to address specific people in the beginning of his speeches compared to Johnson who keeps it broad by stating 'Good afternoon ladies and gentleman' or something of similar sorts. Both authors express gratitude in various ways and use 'I' to assert responsibility. Kennedy also ends with some sort of thank you and salutation dependent on the time of day. This appears to be less common with text written by Johnson. 


### Question E:
The two probability estimates are:
    P(class = 0) = 0.353
    P(class = 1) = 0.647

The shape of the matrix storing the likelihoods is the (number of classes x number of words (length of the vocabulary)). More specfically it is (2x22961).

When varrying the smoothing hyperparameter to 0, it leads to zero probability error and seems to only guess class = 0. A 0 hyperparemeter can result in overfitting. On the contrary, with a high hyperparameter the model only predicts class = 1 which leads to underfitting. 

### Question F:

Predicted Authors:

speech_14_kennedy.txt -> 0 - Kennedy 
speech_8_johnson.txt -> 0 - Kennedy
speech_7_johnson.txt -> 1 - Johnson
speech_5_johnson.txt -> 1 - Johnson
speech_12_kennedy.txt -> 0 - Kennedy
speech_6_johnson.txt -> 0 - Kennedy
speech_10_johnson.txt -> 1 - Johnson
speech_13_kennedy.txt -> 0 - Kennedy
speech_11_kennedy.txt -> 0 - Kennedy
speech_9_kennedy.txt -> 0 - Kennedy


## PROBLEM 2:

The scikit-learn predictions seen below seems to be more even with predicting between Johnson and Kennedy. In other words, the model did not just select Kennedy because it thought it would be a safer option. Instead, it selected Johnson more times than my model which leads to less Johnson text being incorrectly classified as Kennedy. 

scikit-learn Predictions:

speech_14_kennedy.txt -> 0 - Kennedy 
speech_8_johnson.txt -> 1 - Johnson
speech_7_johnson.txt -> 1 - Johnson
speech_5_johnson.txt -> 1 - Johnson
speech_12_kennedy.txt -> 0 - Kennedy
speech_6_johnson.txt -> 0 - Kennedy
speech_10_johnson.txt -> 1 - Johnson
speech_13_kennedy.txt -> 0 - Kennedy
speech_11_kennedy.txt -> 0 - Kennedy
speech_9_kennedy.txt -> 0 - Kennedy

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
    The model never predicted a Kennedy text as Johnson (class = 0). However, it struggled to correctly predict Johnson's text (class = 1) as it incorrectly classified Kennedy as the author for 2 out of the 5 Johnson text given. 

Scikit-learn (conf_scikit.jpg):
    This model was better at predicting Johnson's work as it got one more correct than my model. However, it was the same for Kennedy's text in that it was accurate for every text given. 

## AI USAGE

### Question 1:
(a) I used ChatGPT Pro with medium thinking level. 
(b) https://chatgpt.com/share/6ab5977d-b608-83ea-b543-fa3b3b5da374 , https://chatgpt.com/share/6ab5978b-217c-83ea-87f5-87516ebdf8d8 
(c) I used AI throughout the assignment for feedback. After completing a section I was unsure about, I sent ChatGPT the prompt containing the TODO and asked for constructive feedback on what I did well and how I can improve to match the assignment specification. I specified to ChatGPT to not provide me with a solution or code. In other places where I was confident in my code and easily tested it by hand, I did not use ChatGPT because sometimes ChatGPT is inaccurate or overcomplicates things. Because I could verify it was doing what it was supposed to, there was no need. Finally, at the end of the assignment, I send my entire project and asked for a grade against the given rubric as well as suggestions for improvement. After reading through the suggestions, I decided what I should change or not. All changes were made by me if necessary. 

### Question 2:
(a) AI provided me with guidance on things I should consider with my code rather than give me solutions. This allowed me to modify my code to fix things I had not yet considered. I further tested all code using input() and print statements throughout until I got it to a stable place. AI did not generate any of the code I have put down. 
(b) I made modifications like structure to my code to make it more concise or sometimes equations because I was missing a log which allowed for a stronger model. I made these changes after reading the suggestion, testing and then comparing to see what worked better. I often took ChatGPTs suggestions one step further in implementation to match it to what I liked. 

### Question 3:
(a) I relearned a lot about pandas dataframes, OOP and reminded myself how important pseudo code is. I often thought about each TODO, wrote it out in plain language then implemented the code. Furthermore, I built a better understanding of the Naive Bayes classifier. 
(b) My learning process was improved because I did the intial thinking and developing then submitted to ChatGPT for feedback. By only asking for feedback, I gained a new perspective on how I can improve then made changes as necessary. This allowed me to see errors and correct mistakes before I continued to make them. 
(c) I would have felt less confident in my submission but also I do not think I would have gained as much from this assignment. ChatGPT brought up strong suggestions that I would not have otherwise thought about. Additionally, it helped solidify and clarify the reasonings behind some of these equations and methods. 