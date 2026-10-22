DISCUSSION QUESTIONS

## (A) 
The solution provided seems to assume that the author is always separated by an underscore and is the last element. This is in comparison to mine which simply checks if the author (kennedy or johnson) exists anywhere in the filepath, then assigns accordingly. I think that my way is more robust because it checks the entire filepath rather than making this assumption. This is an area the solution could improve. The creation of the vocabulary dictionary appears simpler in the final solution by using significantly less nested for loops and instead, creating the dictionary on its assignment. This seems to be a constant trend throughout  and an area I could improve in. I need to work on simplifying my code when appropriate as it becomes more readable. Regardless, the codes have similarities throughout especially when developing the vocabulary, getting n_docs, n_classes and the entire testing method which are nearly identical.

## (C) PYTEST RESULTS
The result displays 3 test passed. The directions ask for both one function and 3 passing tests. Because 1 function will not display the 3 passed, I decided to create 3 functions to make it align with the directions better.
========================================================================================================= test session starts ==========================================================================================================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /home/akowala/DSAN5400/Kowalchyk-DSAN5400/assignment3/naive_bayes
configfile: pytest.ini
plugins: anyio-4.14.2
collected 3 items                                                                                                                                                                                                                      

tests/test_naive_bayes.py ...                                                                                                                                                                                                    [100%]

========================================================================================================== 3 passed in 0.28s ===========================================================================================================

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

### AI Usage
### Question 1:
(a) I used ChatGPT Pro with medium thinking level. 
(b) https://chatgpt.com/share/6ad96da4-92d4-83ea-b770-e4b772578dc6, https://chatgpt.com/share/6ad96d31-6078-83ea-b69d-2efdabe3f9b5 , 
(c) I used AI throughout the assignment for feedback. After completing a section I was unsure about, I sent ChatGPT the prompt containing the TODO and asked for constructive feedback on what I did well and how I can improve to match the assignment specification. I specified to ChatGPT to not provide me with a solution or code and reminded ChatGPT when it was forgotten. In response, ChatGPT provided me with hints on how I can improve. I would then send updated iterations until what I had was correct. In other places where I was confident in my code and easily tested it by hand, I did not use ChatGPT because sometimes ChatGPT is inaccurate or overcomplicates things. I was able to verify through testing what my code was doing and therefore used ChatGPT for question clarification and small coding errors. Finally, at the end of the assignment, I sent my entire project and asked for a grade against the given rubric as well as suggestions for improvement. After reading through the suggestions, I decided what I should change or not. One area I could not decide about was whether to have three functions for the unit test or 1. ChatGPT helped me decide that 3 would be best even though the instructions are confusing. All changes were made by me if necessary and I understand the code produced/each part of the assignment. I used AI to help with iteration and more of a learn/correct iterative process. 

### Question 2:
(a) AI provided me with guidance on things I should consider with my code rather than give me solutions. This allowed me to modify my code to fix things I had not yet considered. I further tested all code by running the files and checking fror errors. I used ChatGPT primarily for the ngram to help better my understanding as I was confused initially to how it worked. From there I learned that the tokens can overlap which I was not accounting for in my code. 
(b) I made modifications like structure to my code to make it more concise or altered it for robustness and accuracy. I made these changes after reading the suggestion, thinking about the next steps, testing and then comparing the results to see if it worked. I often took ChatGPTs suggestions one step further in implementation to match it to what I liked and what I thought best fit the assignment. When I was confused on if I was completing a question correctly, I asked ChatGPT which gave me the academic confidence to continue rather than spending significant amount of time on one area for it not to match the assignment specification. 

### Question 3:
(a) I learned a lot about the different types of tokenizers, specifically ngram as menitoned above and reminded myself how important pseudo code is. I often thought about each TODO, wrote it out in plain language then implemented the code. Furthermore, I built a better understanding of the Naive Bayes classifier and learned how to best organize/structure my assignment. A lot of my time was spent rearranging the files, installing the nb package and learning that syntax. 
(b) My learning process was improved because I did the intial thinking and developing then submitted to ChatGPT for feedback. By only asking for feedback, I gained a new perspective on how I can improve then made changes as necessary. This allowed me to see errors and correct mistakes before I continued to make them. Additionally, it ensured I was meeting the assignments intent. 
(c) I would have felt less confident in my submission but also I do not think I would have gained as much from this assignment. ChatGPT brought up strong suggestions that I would not have otherwise thought about. Additionally, it helped solidify and clarify the different tokenization techniques. 