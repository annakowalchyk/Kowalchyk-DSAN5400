import numpy as np

class NaiveBayes:
    def __init__(self, df, alpha):
        self.df = df
        self.alpha = alpha

    # Train Method
    def train(self):
        """
            Takes as input a pandas DataFrame containing Federalist
            files text to determine priors and likelihoods
            """
        vocabulary = {}
        tokens = self.df.text.str.lower().str.split()
        index = 0
        for tok in tokens:
            for t in tok:
                # If token is unique
                if t not in vocabulary:
                    vocabulary[t] = index # Assign token an index for dictionary
                    index += 1 # Increase index to make it unique for next token
        n_docs = self.df.shape[0] # Accesses rows
        # print(df["author"].tolist())
        n_classes = self.df["author"].nunique() # Number of classes -> authors
        # Compute the priors
        # Number of documents written by author / number of documents 
        prob_0 = (self.df["author"] == 0).sum() / n_docs
        prob_1 = (self.df["author"] == 1).sum() / n_docs
        priors = [prob_0, prob_1]

        # Matrix containing all 0s called training_matrix of size
        #  (n_docs, len(vocabulary)), then fill it with the counts of each word
        #  for each document. This is the bag-of-words matrix for all the documents

        # Fill with counts of each word (lowercase) using dictionary index
        training_matrix = [[0 for _ in range(len(vocabulary))] for _ in range(n_docs)]
        index = 0
        for text in self.df["text"]:
            words = text.lower().split()
            for word in words:
                # print(word)
                dict_index = vocabulary.get(word)
                # print(dict_index)
                # print(dict_index)
                # Increase count of word
                training_matrix[index][dict_index] += 1
            index += 1
                
        # Get word counts for both classes
        word_counts_per_class = [[0 for _ in range(len(vocabulary))] for _ in range(n_classes)]
        for row in range(len(training_matrix)):
            for col in range(len(training_matrix[row])):
                if self.df.at[row, "author"] == 0:
                    word_counts_per_class[0][col] = word_counts_per_class[0][col] + training_matrix[row][col]
                else:
                    word_counts_per_class[1][col] = word_counts_per_class[1][col] + training_matrix[row][col]

            
        # TODO Initialize a matrix to store the likelihoods
        likelihoods = np.zeros((n_classes, len(vocabulary)))
        print(likelihoods.shape)
        # Probability of a word, given the class
        
        # Fill it in using Lidstone smoothing
        for row in range(len(likelihoods)):
            # sum of word counts for each class
            sum_count_class = sum(word_counts_per_class[row])
            for col in range(len(likelihoods[row])):
                # word count
                count_word_given_class = word_counts_per_class[row][col]
                likelihoods[row][col] = (count_word_given_class + self.alpha) / (sum_count_class + self.alpha * len(vocabulary))


        self.vocabulary = vocabulary
        self.priors = priors
        self.likelihoods = likelihoods
    # Test Method
    def test(self, df):
        """
        Takes as input a pandas DataFrame representing the disputed Federalist
        Papers and returns predictions for every text document
        """
        class_predictions = []
        for text in df['text']:
            test_vector = np.zeros(shape=(len(self.vocabulary)))
            for token in text.split():
                # skip the words that do not appear in the training corpus
                if token in self.vocabulary:
                    idx = self.vocabulary[token]
                    test_vector[idx] += 1
            # compute predictions p(y|test)
            preds = test_vector.dot(np.log(self.likelihoods).T) + np.log(self.priors)
            yhat = np.argmax(preds)
            class_predictions.append(yhat)
        self.class_predictions = class_predictions
