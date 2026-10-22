from nb.nb import NaiveBayes
import pandas as pd
import numpy as np


# Create data from docs.txt
data = {
    'author': [0, 0, 0, 1, 1],
    'text' : ["just plain boring", "entirely predictable and lacks energy", "no surprises and very few laughs", "very powerful", "the most fun film of the summer"]

}

df = pd.DataFrame(data)

# Setup
df = pd.DataFrame(data)
nb = NaiveBayes(df,1)

# train
nb.train()

def test_nb_class():
    # Actual prior from textbook
    # Check priors
    priors = nb.priors
    priors_0 = priors[0]
    priors_1 = priors[1]

    assert priors_0 == 3/5
    assert priors_1 == 2/5

def test_nb_likelihoods():
    # Check likelihoods
    likelihoods = nb.likelihoods

    # "Predictable" likelihoods
    like_predictable_0 = nb.likelihoods[0, nb.vocabulary['predictable']]
    like_predictable_1 = nb.likelihoods[1, nb.vocabulary['predictable']]
    assert like_predictable_0 == (2/34)
    assert like_predictable_1 == (1/29)

    # "No" likelihoods
    like_no_0 = nb.likelihoods[0, nb.vocabulary['no']]
    like_no_1 = nb.likelihoods[1, nb.vocabulary['no']]
    assert like_no_0 == (2/34)
    assert like_no_1 == (1/29)

    # "fun" likelihoods
    like_fun_0 = nb.likelihoods[0, nb.vocabulary['fun']]
    like_fun_1 = nb.likelihoods[1, nb.vocabulary['fun']]
    assert like_fun_0 == (1/34)
    assert like_fun_1 == (2/29)

def test_nb_sum():
    # Sum along the axis is = 1
    for row in nb.likelihoods:
        assert np.sum(row, axis = 0) == 1