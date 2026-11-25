## Name Matching
This code completes the task of Fuzzy Name Matching using various algorithms to produce a score ranging from 0 to 1 describing similarity of two names. Exact matches receive a score of 1 while no matching characteristics receive a score of 0. Exact Match, Jaccard Similarity, Levenshtein, Cosine Similarity and Jaro-Winkler algorithms are all evaluated and compared using precision, recall and F1. Thresholds are determined based on the intersection of precision and recall to balance the tradeoff. 

### Coding Structure Tree
```
matcher/ 
    data/ 
        queries.tsv 
        annotated-index.tsv 
        annotated-index-train.tsv 
        annotated-index-test.tsv 
    matcher/ 
        __init__.py 
        bin/ 
            __init__.py 
            main.py 
            old_main.py
        name_matcher.py 
        utils/ 
            __init__.py 
            parse_tsv.py 
        eval/ 
            __init__.py 
            eval.py 
        tests/ 
            data/ 
                test_names.tsv 
            __init__.py 
            test_matcher.py 
    .gitignore 
    README.md 
    setup.py 
    pytest.ini 
    discussion.md 
    logs.txt 
    environment.yml
```

### File Information
- data -> raw data downloaded from the assignment folder, additional files include the train and test sets
- matcher -> Subfolder
- main.py -> Main script to run
- old_main.py -> Old script before main was restructured to better interface
- name_matcher.py -> Contains NameMatchScorer Class and all algorithm inheriting subclasses.
- utils ->  utility functions
- parse_tsv -> Iterator to parse the tsv file
- eval.py -> Function to evaluate algorithm precision, recall and F1 score
- __init__.py ->  instructs Python to treat the folder as a package
- test_matcher -> Unit tests for each of the required algorithms
- test_names.tsv -> Simple name tests to be used for the unit tests
- setup.py -> orchestrate the correct installation of the project
- .gitignore -> Files for git to ignore
- logs.txt -> Written logs for algorithm once running
- environment.yml -> Necessary packages needed to run

### Installation
Set up conda environment using the environment.yml file.

### Usage
Run from the root directory of the project. Use this command: 

For plotting
python -m matcher.bin.main -f <dataset_path> -s <scoring_algorithm> -t 0.5 --plot

For evaluating
python -m matcher.bin.main -f <dataset_path> -s <scoring_algorithm> -t 0.5 -e -p

**Flags**

-f, --file Path to the TSV dataset containing name pairs. Required.

-s, --scoring Select the scoring algorithm. Required.

-t, --threshold Similarity threshold used to classify matches. Defaults to 0.5.

-e, --evaluate Calculate precision, recall, and F1.

--plot Generate precision, recall, and F1 curves across similarity thresholds using training data.

-p, --parallel Perform scoring using four multiprocessing workers.

**Available Scoring Algorithms**
- exact
- jaccard
- levenshtein
- tfidf
- jaro

**Example Commands**
1. Run exact matching with evaluation

python -m matcher.bin.main -f data/annotated-index-test.tsv -s exact -e

2. Generate a Jaccard threshold plot

python -m matcher.bin.main -f data/annotated-index-test.tsv -s jaccard --plot

3. Evaluate Levenshtein similarity at a specified threshold

python -m matcher.bin.main -f data/annotated-index-test.tsv -s levenshtein -t 0.75 -e

4. Evaluate TF-IDF cosine similarity

python -m matcher.bin.main -f data/annotated-index-test.tsv -s tfidf -t 0.65 -e

5. Evaluate Jaro-Winkler similarity (bonus)

python -m matcher.bin.main -f data/annotated-index-test.tsv -s jaro -t 0.85 -e

6. Run Jaccard with multiprocessing (bonus)

python -m matcher.bin.main -f data/annotated-index-test.tsv -s jaccard -p -e

**Output**
Generates a TSV file containing the names, scores and true match. Results are saved to data/results_<scoring_algorithm>.tsv

UNIT TESTS: Navigate to matcher folder and run the following command:
pytest

*Note that you can not plot with exact because it is not used to choose an optimal threshold*

### License
Using Visual Studio Code operated on WSL:Ubuntu. 
