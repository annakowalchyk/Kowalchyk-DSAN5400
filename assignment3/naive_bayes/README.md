## Naive Bayes Modeling
This code focuses on careful project organization and importation of code to implement Naive Bayes. The model takes an input of speeches from Johnson, Kennedy and unlabled. Using the Naive Bayes class, the data is loaded and separated by author appropriately. Through a series of prior and liklihood calculations and train/test methods, the code returns a list of 0 or 1 as predictions for the authors of the unlabeled data. In this code, 0 represents Kennedy while 1 represents Johnson. 

### About the Naive Bayes Model
This Naive Bayes classifier performs authorship identification over some speeches by President Lyndon B. Johnson and President John F. Kennedy 

### Coding Structure Tree
assignment3/ 
nb/ 
 data/ 
  johnson/… 
  kennedy/… 
  unlabeled/… 
 nb/ 
  bin/ 
   __init__.py 
   main.py 
  __init__.py 
  nb.py 
             utils/ 
               __init__.py 
             load_data.py  
 tests/ 
  data/ 
   docs.txt 
  __init__.py 
  test_naive_bayes.py 
.gitignore 
pytest.ini 
README.md 
discussion.md 
setup.py 
environment.yml 
index/ 
 index.py 

### File Information
data -> raw text data
nb directory -> NaiveBayes class
nb.py -> Contain the functions that deal with the training and 
testing of the Naive Bayes classifier.

utils ->  utility functions

__init__.py ->  instructs Python to treat the folder as a package

tests -> Unit tests
setup.py -> orchestrate the correct installation of the project

.gitignore -> Files for git to ignore

### Installation
Set up conda environment using the environment.yml file. Must install the utils and nb as package. No extra packages are necessary. 

### Usage
Must first install packages using:
python -m pip install -e .

Then you can continue to the other command lines to run the program.

UNIT TESTS: Navigate to naive_bayes folder and run pytest tests/

MAIN BIN: From naive_bayes folder run
python nb/bin/main.py -f data

**data folder is a subfolder of naive_bayes containing the speeches**

### License
Using Visual Studio Code operated on WSL:Ubuntu. 

