import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


def build_dataframe(folder):
    """
    Takes as input a directory containing presidential speeches and returns two
    DataFrames storing the text from those files, one for the training data
    and one for the test data (unlabeled)
    :param folder: a path to a directory containing presidential speeches
    :return: a tuple of pandas DataFrames
    """
    path = Path(folder)
    df_train = pd.DataFrame(columns=["author"])
    df_test = pd.DataFrame(columns=["author"])
    author_to_id_map = {"kennedy": 0, "johnson": 1}

    def make_df_from_dir(dir_name, df):
        """
        Takes as input directory to construct df from and returns updated df
        :param dir_name: a Path to a directory
        :param df: an empty pandas DataFrame
        :return: updated pandas DataFrames
        """
        for f in path.glob(f"./{dir_name}/*.txt"):
            with open(f) as fp:
                text = fp.read()
                # TODO If the directory name is either kennedy or johnson,
                #  create a pandas DataFrame where the column "authors" is
                #  the directory name and there is a field "text" which
                #  contains the text from the opened file. Note that you want
                #  a single DataFrame, but you loop over numerous files.

                # If the directory name contains the author
                if dir_name in ("kennedy", "johnson"):
                    row = pd.DataFrame({"author": [dir_name], "text": [text]})
                    df = pd.concat([df,row], ignore_index = True)
                    
                else:
                    # TODO Otherwise, we want to create a DataFrame for the
                    #  unlabeled data in a similar fashion. But this is a
                    #  little different because we don't get the label from
                    #  the directory but instead from the file name. Again,
                    #  the field "author" should have the author's name and
                    #  the field "text" should contain the text.

                    # Naming the author based on the filename
                    if 'kennedy' in fp.name:
                        row = pd.DataFrame({"author": ['kennedy'], "text": [text]})
                        df = pd.concat([df,row], ignore_index = True)
                    else:
                        row = pd.DataFrame({"author": ['johnson'], "text": [text]})
                        df = pd.concat([df,row], ignore_index = True)

        # Saving df for analysis in markdown
        df.to_csv("df.csv", index=False)
        return df

    for p in path.iterdir():
        if p.name in ("kennedy", "johnson"):
            df_train = make_df_from_dir(p.name, df_train)
        elif p.name == "unlabeled":
            df_test = make_df_from_dir(p.name, df_test)
    # replace the strings for the author names with numeric codes (0, 1)
    df_train["author"] = df_train["author"].apply(lambda x: author_to_id_map.get(x))
    # do the same for the test data
    df_test["author"] = df_test["author"].apply(lambda x: author_to_id_map.get(x))
    return df_train, df_test


def train_nb(df, alpha=0.1):
    """
    Takes as input a pandas DataFrame containing Federalist
    files text to determine priors and likelihoods
    :param df: a pandas DataFrame
    :return: two numpy arrays for the priors and likelihoods
    """
    # TODO Create a dictionary that maps whitespace-separated tokens in the
    #  file to a unique index. Also, create variables for the number of
    #  documents and the number of classes. Use df.shape for the vocabulary
    #  and the nunique() method for the number of classes

    # Creates dictionary and ensures the words are in lower so that the same word maps to each other regardless of casing
    vocabulary = {}
    tokens = df.text.str.lower().str.split()
    index = 0
    for tok in tokens:
        for t in tok:
            # If token is unique
            if t not in vocabulary:
                vocabulary[t] = index # Assign token an index for dictionary
                index += 1 # Increase index to make it unique for next token
    n_docs = df.shape[0] # Accesses rows
    # print(df["author"].tolist())
    n_classes = df["author"].nunique() # Number of classes -> authors
    # TODO Compute the priors

    # Number of documents written by author / number of documents 
    prob_0 = (df["author"] == 0).sum() / n_docs
    prob_1 = (df["author"] == 1).sum() / n_docs
    priors = [prob_0, prob_1]

    # TODO Create a matrix containing all 0s called training_matrix of size
    #  (n_docs, len(vocabulary)), then fill it with the counts of each word
    #  for each document. This is the bag-of-words matrix for all the documents

    # Fill with counts of each word (lowercase) using dictionary index
    training_matrix = [[0 for _ in range(len(vocabulary))] for _ in range(n_docs)]
    index = 0
    for text in df["text"]:
        words = text.lower().split()
        for word in words:
            # print(word)
            dict_index = vocabulary.get(word)
            # print(dict_index)
            # print(dict_index)
            # Increase count of word
            training_matrix[index][dict_index] += 1
        index += 1
        
    # TODO Get word counts for both classes
    word_counts_per_class = [[0 for _ in range(len(vocabulary))] for _ in range(n_classes)]
    for row in range(len(training_matrix)):
        for col in range(len(training_matrix[row])):
            if df.at[row, "author"] == 0:
                word_counts_per_class[0][col] = word_counts_per_class[0][col] + training_matrix[row][col]
            else:
                word_counts_per_class[1][col] = word_counts_per_class[1][col] + training_matrix[row][col]

    
    # TODO Initialize a matrix to store the likelihoods
    likelihoods = np.zeros((n_classes, len(vocabulary)))
    print(likelihoods.shape)
    # Probability of a word, given the class
    # TODO Then fill it in using Lidstone smoothing
    for row in range(len(likelihoods)):
        # sum of word counts for each class
        sum_count_class = sum(word_counts_per_class[row])
        for col in range(len(likelihoods[row])):
            # word count
            count_word_given_class = word_counts_per_class[row][col]
            likelihoods[row][col] = (count_word_given_class + alpha) / (sum_count_class + alpha * len(vocabulary))

    return vocabulary, priors, likelihoods


def test(df, vocabulary, priors, likelihoods):
    """
    Takes as input a pandas DataFrame representing the disputed Federalist
    Papers and returns predictions for every text document
    :param df: a pandas DataFrame
    :return: a numpy array of predictions
    """
    class_predictions = []
    for text in df["text"]:
        words = text.lower().split()
        test_vector = np.zeros(shape=(len(vocabulary)))
        # TODO Fill test_vector with counts for the words that appear in the
        #  vocabulary
        for word in words:
            # Check to see if it is in the dictionary
            if word in vocabulary:
                # If in dictionary increase count at corresponding index
                index = vocabulary.get(word)
                test_vector[index] += 1
        # TODO Compute predictions p(y|text)
        # Formula from slides with log insertion for stability
        preds = np.log(priors) + np.sum((test_vector * np.log(likelihoods)), axis = 1)
        # TODO Then get your predictions, yhat
        # Formula from slides
        yhat = np.argmax(preds)
        class_predictions.append(yhat)
    return class_predictions


def sklearn_nb(training_df, test_df):
    """
    Performs Naive Bayes classification using scikit-learn implementation
    :param training_df: training data
    :param test_df: test data
    :return: predictions
    """
    vectorizer = CountVectorizer()

    # TODO Fit the vectorizer on the training set text
    vectorizer.fit(training_df["text"])

    # TODO Then transform the text using the vectorizer
    training_data = vectorizer.transform(training_df["text"])
    training_data.toarray()

    # Do the same for the test data
    test_data = vectorizer.transform(test_df["text"])
    test_data.toarray()

    nb_classifier = MultinomialNB()
    # TODO Fit the Naive Bayes classifier
    # x is data and y is labels
    nb_classifier.fit(training_data, training_df["author"])

    pred_nb = nb_classifier.predict(test_data)
    return pred_nb


def get_metrics(true, preds):
    """
    Takes gold labels and predictions to compute performance metrics
    :param true: array-like object
    :param preds: array-like object
    :return: a tuple of various performance metrics
    """
    # TODO Compute performance measures
    accuracy = metrics.accuracy_score(true["author"].astype(int), preds)
    f1_score = metrics.f1_score(true["author"].astype(int), preds)
    conf_matrix = metrics.confusion_matrix(true["author"].astype(int), preds)

    return accuracy, f1_score, conf_matrix


def plot_confusion_matrix(conf_matrix_data, labels):
    """
    Takes as input confusion matrix data from get_metrics() and prints out a
    confusion matrix
    :param conf_matrix_data:
    :return: None
    """
    plt.title("Confusion matrix")
    axis = sns.heatmap(conf_matrix_data, annot = True)
    axis.set_xticklabels(labels)
    axis.set_yticklabels(labels)
    axis.set(xlabel="Predicted", ylabel="True")
    # plt.show()
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Naive Bayes Algorithm")
    parser.add_argument("-f", "--indir", required=True, help="Data directory")
    args = parser.parse_args()
    training_df, test_df = build_dataframe(args.indir)
    # print(training_df["author"].nunique())
    # print(training_df)
    vocabulary, priors, likelihoods = train_nb(training_df)
    class_predictions = test(test_df, vocabulary, priors, likelihoods)
    acc, f1, conf = get_metrics(test_df, class_predictions)
    # print(conf)
    plot_confusion_matrix(conf, [0, 1])
    plt.savefig("conf.jpg")
    plt.close()
    # input()
    sklearn_preds = sklearn_nb(training_df, test_df)
    print(f"Sklearn Predictions: {sklearn_preds}")
    sklearn_metrics = get_metrics(test_df, sklearn_preds)
    print(f"My predictions: {[int(x) for x in class_predictions]}")
    print(f"My metrics: \n accuracy: {acc} \n f1: {f1}")
    print(f"SKLEARN Metrics: \n accuracy:{sklearn_metrics[0]} \n f1: {sklearn_metrics[1]}")
    plot_confusion_matrix(sklearn_metrics[2], [0, 1])
    plt.savefig("conf_scikit.jpg")
    # Save confusion matrix
