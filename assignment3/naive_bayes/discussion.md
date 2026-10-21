DISCUSSION QUESTIONS

## (A) 
The solution provided seems to assume that the author is always separated by an underscore and is the last element. This is in comparison to mine which simply checks if the author (kennedy or johnson) exist anywhere in the filepath then assigns accordingly. I think that my way is more robust because it checks the entire filepath rather than making this assumption. The creation of the vocabulary dictionary appears simpler in the final solution by using significantly less nested for loops and instead, creating the dictionary on its assignment. This seems to be a constant trend throughout the comparison and an area I could improve in. I need to work on simplifying my code when appropriate similar to the solution. Regardless, the codes have similarities throughout like with developing the vocabulary, getting n_docs, n_classes and the entire testing method. 

## (C) PYTEST RESULTS
** The result displays 1 test passed. The reason it is only 1 test is because the directions state to make a single function test_nb_classes. Pytest will only display 1 pass/failure although it does run every test in the function.
================================================== test session starts ==================================================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/akowala/DSAN5400/Kowalchyk-DSAN5400/assignment3/naive_bayes
configfile: pytest.ini
plugins: anyio-4.14.2
collected 1 item                                                                                                        

tests/test_naive_bayes.py .                                                                                       [100%]

=================================================== 1 passed in 0.50s ===================================================

## (E) RESULTS FOR SYSTEM

** ALL ARE DONE ON 20newsgroups-initial.xml **

### System (with stemming)
Whitespace Tokenizer: ['3', '5653', '1127', '3319', '8935', '2552', '16515', '14398', '16638', '8772']
Off the Shelf Tokenizer: ['3', '5653', '1127', '3319', '8935', '2552', '16515', '14398', '16638', '8772']
N-Gram Tokenizer: ['1127', '3', '2552', '14398', '5653', '16515', '16638', '8772', '8935', '3319']

### System (without stemming)
Whitespace Tokenizer: ['3', '5653', '1127', '3319', '8935', '2552', '16515', '14398', '16638', '8772']
Off the Shelf Tokenizer: ['3', '5653', '1127', '3319', '8935', '2552', '16515', '14398', '16638', '8772']
N-Gram Tokenizer: ['8935', '1127', '14398', '16638', '5653', '16515', '3', '3319', '8772', '2552']

Comments: Each tokenizer pulled 10 document ids and all document ids are consistent for each tokenizer with and without stemming. Therefore, it is likely that all 10 of these documents each contain the word 'system'.

## (F)

### Compatability (with stemming)
Whitespace Tokenizer: ['14398', '8772']
Off the Shelf Tokenizer: ['14398', '8772']
N-Gram Tokenizer: ['14398', '8772']

### Compatability (without stemming)
Whitespace Tokenizer: ['14398', '8772']
Off the Shelf Tokenizer: ['14398', '8772']
N-Gram Tokenizer: ['14398', '8772']

Comments: Each tokenizer pulled 2 document ids and all document ids are consistent for each tokenizer with and without stemming. Therefore, it is likely that documents 14398 and 8772 both contain the word 'compatability'. For a word of this size, n-gram results can be inaccurate as the 4 character tokens may appear in any order. For example the words 'comp' and 'abil' may appear in the document without actually being the full word 'compatability'. 

## (G)

### System and Compatibility (with stemming)
Whitespace Tokenizer: {'8772', '14398'}
Off the Shelf Tokenizer: {'8772', '14398'}
N-Gram Tokenizer: {'14398', '8772'}

### System and Compatibility (without stemming)
Whitespace Tokenizer: {'8772', '14398'}
Off the Shelf Tokenizer: {'8772', '14398'}
N-Gram Tokenizer: {'14398', '8772'}

Comments: Every tokenizer with and without stemming found the document ids 14398 and 8772 to contain both 'system' and 'compatability'. Therefore, it is likely that these two documents contain both of these words since each tokenizer is in agreement. Because none of the tokenizers consider order, it is important to realize why the n-gram tokenizer does not match the whitespace and off the shelf tokenizer order. 