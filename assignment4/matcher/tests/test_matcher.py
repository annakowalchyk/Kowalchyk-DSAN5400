from matcher.name_matcher import ExactMatch, Jaccard, LevenshteinScore, Tfidf_matcher
import pandas as pd
import pytest

def test_exact():
    names = pd.read_csv(f"tests/data/test_names.tsv", sep="\t")

    # Row 0: Test exact match
    name1 = names["name1"].iloc[0]
    name2 = names["name2"].iloc[0]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 1

    # Row 1: Missing single letter
    name1 = names["name1"].iloc[1]
    name2 = names["name2"].iloc[1]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 0

    # Row 2: One incorrect letter
    name1 = names["name1"].iloc[2]
    name2 = names["name2"].iloc[2]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 0

    # Row 3: Completely incorrect name
    name1 = names["name1"].iloc[3]
    name2 = names["name2"].iloc[3]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 0

    # Row 4: Incorrect capitalization
    name1 = names["name1"].iloc[4]
    name2 = names["name2"].iloc[4]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 0

    # Row 5: Extra letter
    name1 = names["name1"].iloc[5]
    name2 = names["name2"].iloc[5]
    exact_match = ExactMatch(name1, name2)
    score = exact_match.score(name1, name2)
    assert score == 0

def test_jaccard():
    names = pd.read_csv(f"tests/data/test_names.tsv", sep="\t")

    # Row 0: Test exact match
    name1 = names["name1"].iloc[0]
    name2 = names["name2"].iloc[0]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 1

    # Row 1: Missing single letter (threshold 50%)
    name1 = names["name1"].iloc[1]
    name2 = names["name2"].iloc[1]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 1

    # Row 2: One incorrect letter
    name1 = names["name1"].iloc[2]
    name2 = names["name2"].iloc[2]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 0.5

    # Row 3: Completely incorrect name
    name1 = names["name1"].iloc[3]
    name2 = names["name2"].iloc[3]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 0

    # Row 4: Incorrect capitalization
    name1 = names["name1"].iloc[4]
    name2 = names["name2"].iloc[4]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 0

    # Row 5: Extra letter 
    name1 = names["name1"].iloc[5]
    name2 = names["name2"].iloc[5]
    jac = Jaccard(name1, name2)
    score = jac.score(name1, name2)
    assert score == 1

def test_levenshtein():
    names = pd.read_csv(f"tests/data/test_names.tsv", sep="\t")

    # Row 0: Test exact match
    name1 = names["name1"].iloc[0]
    name2 = names["name2"].iloc[0]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    assert score == 1

    # Row 1: Missing single letter (threshold 50%)
    name1 = names["name1"].iloc[1]
    name2 = names["name2"].iloc[1]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    actual = 1 - (1 / (14+13))
    assert score == actual

    # Row 2: One incorrect letter
    name1 = names["name1"].iloc[2]
    name2 = names["name2"].iloc[2]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    actual = 1 - (2 / (4 + 4))
    assert score == actual

    # Row 3: Completely incorrect name
    name1 = names["name1"].iloc[3]
    name2 = names["name2"].iloc[3]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    assert score == 0

    # Row 4: Incorrect capitalization
    name1 = names["name1"].iloc[4]
    name2 = names["name2"].iloc[4]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    assert score == 0

    # Row 5: Extra letter 
    name1 = names["name1"].iloc[5]
    name2 = names["name2"].iloc[5]
    lev = LevenshteinScore(name1, name2)
    score = lev.score(name1, name2)
    actual = 1 - (1 / (4+5))
    assert score == actual


def test_tfidf():
    names = pd.read_csv(f"tests/data/test_names.tsv", sep="\t")

    training_names = pd.concat([
    names["name1"],
    names["name2"]
    ]).tolist()

    tfidf_match = Tfidf_matcher()
    tfidf_match.fit_vector(training_names)

    # Row 0: Test exact match
    name1 = names["name1"].iloc[0]
    name2 = names["name2"].iloc[0]
    score = tfidf_match.score(name1, name2)
    assert score == pytest.approx(1)

    # Row 1: Missing single letter (threshold 50%)
    name1 = names["name1"].iloc[1]
    name2 = names["name2"].iloc[1]
    score = tfidf_match.score(name1, name2)
    assert score > 0 and score < 1

    # Row 2: One incorrect letter
    name1 = names["name1"].iloc[2]
    name2 = names["name2"].iloc[2]
    score = tfidf_match.score(name1, name2)
    assert score > 0  and score < 1

    # Row 3: Completely incorrect name
    name1 = names["name1"].iloc[3]
    name2 = names["name2"].iloc[3]
    score = tfidf_match.score(name1, name2)
    assert score == 0

    # Row 4: Incorrect capitalization
    name1 = names["name1"].iloc[4]
    name2 = names["name2"].iloc[4]
    score = tfidf_match.score(name1, name2)
    assert score > 0.50

    # Row 5: Extra letter 
    name1 = names["name1"].iloc[5]
    name2 = names["name2"].iloc[5]
    score = tfidf_match.score(name1, name2)
    assert score > 0 and score < 1

