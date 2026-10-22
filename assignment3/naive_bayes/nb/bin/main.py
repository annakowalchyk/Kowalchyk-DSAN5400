import argparse
from nb.utils.load_data import load_data
from nb.nb import NaiveBayes

if __name__ == "__main__":
    # Ask user for input
    parser = argparse.ArgumentParser(description="Naive Bayes Algorithm")
    parser.add_argument("-f", "--indir", required=True, help="Data directory")
    args = parser.parse_args()
    # Build dataframe
    training_df, test_df = load_data(args.indir)

    # Estimates for the priors and likelihoods
    nb_training = NaiveBayes(training_df,0.10)
    nb_training.train()
    nb_training.test(test_df)

    # Print predictions
    print([int(x) for x in nb_training.class_predictions])

